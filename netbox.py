import requests
import json

class NetBoxAPI:
    def __init__(self, url, token):
        self.url = url.rstrip("/")
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.token}"
        }

    def get(self, path):
        resp = requests.get(f"{self.url}/{path}/", headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def post(self, path, data):
        resp = requests.post(f"{self.url}/{path}/", headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()

    def put(self, path, data):
        resp = requests.put(f"{self.url}/{path}/", headers=self.headers, json=data)
        resp.raise_for_status()
        return resp.json()

    def delete(self, path):
        resp = requests.delete(f"{self.url}/{path}/", headers=self.headers)
        status_code = resp.status_code
        resp.raise_for_status()
        return status_code, resp.json()

    def get_devices(self):
        return self.get("dcim/devices")

    def get_device(self, device_id):
        return self.get(f"dcim/devices/{device_id}")

    def create_device(self, name, device_type, site, status="active"):
        data = {
            "name": name,
            "device_type": device_type,
            "site": site,
            "status": status
        }
        return self.post("dcim/devices", data)

    def update_device(self, device_id, data):
        return self.put(f"dcim/devices/{device_id}", data)

    def delete_device(self, device_id):
        status_code, resp = self.delete(f"dcim/devices/{device_id}")
        if status_code == 204:
            return f"Device {device_id} deleted successfully."
        try:
            return resp.json()
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON response received. Content: {resp.content}")
            return []
        
    def get_interfaces(self):
        return self.get("dcim/interfaces")

    def get_interface(self, interface_id):
        return self.get(f"dcim/interfaces/{interface_id}")

    def create_interface(self, name, device, type, mac_address, mgmt_only=False):
        data = {
            "name": name,
            "device": device,
            "type": type,
            "mac_address": mac_address,
            "mgmt_only": mgmt_only
        }
        return self.post("dcim/interfaces", data)

    def update_interface(self, interface_id, data):
        return self.put(f"dcim/interfaces/{interface_id}", data)

    def delete_interface(self, interface_id):
        return self.delete(f"dcim/interfaces/{interface_id}")

    def get_ip_addresses(self):
        return self.get("ipam/ip-addresses")

    def get_ip_address(self, ip_address_id):
        return self.get(f"ipam/ip-addresses/{ip_address_id}")

    def create_ip_address(self, address, interface, status="active"):
        data = {
            "address": address,
            "interface": interface,
            "status": status
        }
        return self.post("ipam/ip-addresses", data)

    def update_ip_address(self, ip_address_id, data):
        return self.put(f"ipam/ip-addresses/{ip_address_id}", data)

    def delete_ip_address(self, ip_address_id):
        return self.delete(f"ipam/ip-addresses/{ip_address_id}")

    def get_sites(self):
        resp = self.get("dcim/sites")
        print(resp.content) # Print the response content to help diagnose the issue
        return resp.json()

    def create_site(self, name, slug, status="active"):
        data = {
            "name": name,
            "slug": slug,
            "status": status
        }
        return self.post("dcim/sites", data)

    def update_site(self, site_id, data):
        return self.put(f"dcim/sites/{site_id}", data)

    def delete_site(self, site_id):
        resp =  self.delete(f"dcim/sites/{site_id}")
        try:
            return resp.json()
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON response received. Content: {resp.content}")
            return []
        
    def get_racks(self):
        return self.get("dcim/racks")

    def get_rack(self, rack_id):
        return self.get(f"dcim/racks/{rack_id}")
    
    def create_rack(self, name, site, status="active"):
        data = {
            "name": name,
            "site": site,
            "status": status
        }
        return self.post("dcim/racks", data)

    def update_rack(self, rack_id, data):
        return self.put(f"dcim/racks/{rack_id}", data)
    
    def delete_rack(self, rack_id):
        return self.delete(f"dcim/racks/{rack_id}")


