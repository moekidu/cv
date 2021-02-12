#! /usr/bin/env python

from netmiko import ConnectHandler

def connect_to_device(hostname):
    print(f"Connecting to device | {hostname}")
    net_d = ConnectHandler(host=hostname, username='ntc', password='ntc123', device_type='cisco_ios')
    return net_d

def save_config(device, hostname):
    print(f"Saving configuration | {hostname}")
    device.send_command("wr mem")

def backup_config(device, hostname):
    print(f"Backing up configuration | {hostname}")
    device.send_command("term len 0")
    config = device.send_command("show run")
    return config

def write_to_file(hostname, show_run):
    print(f"Writing config to file | {hostname}\n")
    with open("/home/ntc/scripts/{hostname}.cfg", "w") as config_file:
        config_file.write(show_run)

def main():
    devices = ['csr1', 'csr2', 'csr3']

    for device in devices:

        net_device = connect_to_device(device)

        save_config(net_device, device)

        config = backup_config(net_device, device)

        write_to_file(device, config)

        net_device.disconnect()

main()
