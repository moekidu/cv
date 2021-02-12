#! /usr/bin/env python

from netmiko import ConnectHandler

print("Connecting to CSR1")
csr1 = ConnectHandler(host='csr1', username='ntc', password='ntc123', device_type='cisco_ios')
print("Saving configuration CSR1")
csr1.send_command("wr mem")
print("Backing up configuration CSR1")
csr1_config = csr1.send_command("show run")
print("Writing configuration to file CSR1\n")
with open("/home/ntc/scripts/csr1.cfg", "w") as config_file: 
    config_file.write(csr1_config)

print("Connecting to CSR2")
csr2 = ConnectHandler(host='csr2', username='ntc', password='ntc123', device_type='cisco_ios')
print("Saving configuration CSR2")
csr2.send_command("wr mem")
print("Backing up configuration CSR2")
csr2_config = csr1.send_command("show run")
print("Writing configuration to file CSR2\n")
with open("/home/ntc/scripts/csr2.cfg", "w") as config_file: 
    config_file.write(csr2_config)
