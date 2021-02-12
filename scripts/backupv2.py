#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1', 'csr2', 'csr3']

for device in devices:

    print(f"Connecting to {device}")
    net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')

    print(f"Saving configuration {device}")
    net_device.send_command("wr mem")

    print(f"Backing up configuration {device}")
    net_device.send_command("term len 0")
    config = net_device.send_command("show run")

    print(f"Writing configuration to file {device}\n")
    with open(f"/home/ntc/scripts/{device}.cfg", "w") as config_file: 
        config_file.write(config)

    net_device.disconnect()
