import maclookup
import requests
from cisco_device import CiscoDevice
import time
from pprint import pprint


"""
This module contains two classes, `FindMacVendor` and `FindMacsAndVendorsDevice`, which can be used to find the vendor information for a given MAC address and map MAC addresses to their associated vendors and interfaces in a Cisco device.

Class `FindMacVendor` uses the `maclookup` API to obtain the vendor name for a given MAC address. The class has one parameter:
- `mac_address` (str): The MAC address for which the vendor needs to be looked up.

The class has one method:
- `check()`: Sends an HTTP GET request to the API endpoint and returns the vendor name as a string.

Class `FindMacsAndVendorsDevice` uses the `CiscoDevice` class to retrieve the MAC address table for a given device and then uses `FindMacVendor` to map MAC addresses to their associated vendors and interfaces. The class has one parameter:
- `device` (CiscoDevice): An instance of the `CiscoDevice` class, which is used to retrieve the MAC address table.

The class has one method:
- `check_vendors()`: Loops over the MAC address table, retrieves the vendor information for each MAC address using `FindMacVendor`, and stores the result as a dictionary. The keys of the dictionary are MAC addresses, and the values are lists of the vendor name and the interface on which the MAC address was learned.

Note: This module requires the `requests`, `cisco_device`, `time`, and `pprint` modules to be installed.
"""

class FindMacVendor():

    def __init__(self, mac_address) -> None:
        self.mac_address = mac_address
        self.base_url = "https://api.maclookup.app/v2/macs/" + mac_address + "/company/name"

    def check(self):
        payload={}
        headers = {}
        response = requests.request("GET", self.base_url, headers=headers, data=payload)
        return response.text


class FindMacsAndVendorsDevice():
    
    def __init__(self, device):

        self.variable = device.get_mac_address_table('genie')


    def check_vendors(self):
        dict = {}
        for vlan in self.variable["mac_table"]["vlans"].keys():
            for mac in self.variable["mac_table"]["vlans"][vlan]["mac_addresses"].keys():
                request_mac = FindMacVendor(mac)
                dict[mac] = [request_mac.check(), [str(key) for key in self.variable["mac_table"]["vlans"][vlan]['mac_addresses'][mac]["interfaces"].keys()][0]]
                time.sleep(0.1)
        
        return dict



class MacAddress:
    def __init__(self, mac_address):
        self.mac_address = mac_address

    def get_vendor(self):
        vendor = maclookup.lookup(self.mac_address)
        if vendor:
            return vendor
        else:
            return "Vendor not found"


'''
device = CiscoDevice("10.60.31.132")

B = FindMacVendor("58d5.0a99.48d5")

#A = FindMacsAndVendorsDevice(device)

K = B.check()

pprint(K.check(), indent=4)




mac = MacAddress("00:11:22:33:44:55")
vendor = mac.get_vendor()
print(vendor)


'''
