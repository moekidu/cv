#! /usr/bin/env python

def get_vlans():
    return [1, 5, 10, 20]

vlans = get_vlans()

print(vlans)

def vlan_exists(vlan_id):
    return vlan_id in [1, 5, 10, 20]

print(vlan_exists(10))
print(vlan_exists(12))
