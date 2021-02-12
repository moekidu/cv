from netmiko import ConnectHandler
from getpass import getpass
import argparse

def connect_to_device(hostname, username, password, device_type):
    message = "Connecting to device"
    print_logger(message, hostname)
    net_d = ConnectHandler(host=hostname, username=username, password=password, device_type=device_type)

    return net_d

def deploy_commands(device, hostname, config_file):
    print("Sending commands from file | {}".format(hostname))
    device.send_config_from_file(config_file)

def print_logger(message, hostname):
    print("{} | {}".format(message, hostname))

def main(device, username, password, device_type):
    config_file = './snmp.cfg'

    net_device = connect_to_device(device, username, password, device_type)

    deploy_commands(net_device, device, config_file)

    print_logger("Disconnecting from device", device)
    net_device.disconnect()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Collect device and data'
                                     ' file information to configure a device')
    parser.add_argument('-i', '--ip',
                        help='Enter the IP address or hostname of the device',
                        required=True)
    parser.add_argument('-d', '--device_type', help='Enter the device type',
                        required=True)
    parser.add_argument('-u', '--username', help='Enter the username',
                        required=True)
    parser.add_argument('-p', '--password', help='Enter the password',
                        required=True)

    # parse all args and render
    args = parser.parse_args()

    device = args.ip
    username = args.username
    password = args.password
    device_type = args.device_type

    main(device, username, password, device_type)
