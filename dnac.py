from dnacentersdk import DNACenterAPI
import json
import urllib3
import environment


# Disable HTTPS Certificate warning
urllib3.disable_warnings()


class DNA_Center():

    username = environment.AD_USERNAME
    password = environment.AD_PASSWORD
    base_url = environment.DNAC_URL


    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None
        self.api = None
        
    def authenticate(self):
        try:
            self.api = DNACenterAPI(base_url=self.base_url, username=self.username, password=self.password, verify=False)
            self.token = self.api._session.headers["X-Auth-Token"]
        except:
            raise ValueError("Failed to authenticate to DNA Center.")
        
    def get_devices(self):
        try:
            devices = self.api.devices.get_device_list()
            return devices
        except:
            raise ValueError("Failed to get list of devices.")
        
    def get_device_by_id(self, device_id):
        try:
            device = self.api.devices.get_device_by_id(device_id=device_id)
            return device
        except:
            raise ValueError("Failed to get device by ID.")
        
    def get_device_interfaces(self, device_id):
        try:
            interfaces = self.api.devices.get_interfaces_by_device_id(device_id=device_id)
            return interfaces
        except:
            raise ValueError("Failed to get interfaces for device.")
        
    def get_site_health(self, site_id):
        try:
            health = self.api.sites.get_site_health(site_id=site_id)
            return health
        except:
            raise ValueError("Failed to get site health.")
        
    def get_topology(self):
        try:
            topology = self.api.topology.get_physical_topology()
            return topology
        except:
            raise ValueError("Failed to get topology.")
        
    def add_vlan(self, vlan_name, vlan_id):
        try:
            vlan = self.api.networks.create_vlan(vlan_name=vlan_name, vlan_id=vlan_id)
            return vlan
        except:
            raise ValueError("Failed to create VLAN.")
        
    def add_network(self, network_name, network_address, network_mask):
        try:
            network = self.api.networks.create_network(name=network_name, ip_address=network_address, mask=network_mask)
            return network
        except:
            raise ValueError("Failed to create network.")
        
    def get_clients(self):
        try:
            clients = self.api.clients.get_overall_client_health()
            return clients
        except:
            raise ValueError("Failed to get client health.")
            
    def get_pnp_device_count(self):
        try:
            count = self.api.pnp.get_device_count()
            return count
        except:
            raise ValueError("Failed to get PnP device count.")
            
    def get_pnp_devices(self):
        try:
            devices = self.api.pnp.get_devices()
            return devices
        except:
            raise ValueError("Failed to get PnP devices.")
        
    def claim_pnp_device(self, serial_number, site_id):
        try:
            payload = {"deviceClaimList": [{"deviceId": serial_number, "siteId": site_id}]}
            response = self.api.pnp.claim_devices(json.dumps(payload))
            return response
        except:
            raise ValueError("Failed to claim PnP device.")
        
    def unclaim_pnp_device(self, serial_number):
        try:
            payload = {"deviceClaimList": [{"deviceId": serial_number}]}
            response = self.api.pnp.unclaim_devices(json.dumps(payload))
            return response
        except:
            raise ValueError("Failed to unclaim PnP device.")
        
    def get_pnp_device_info(self, serial_number):
        try:
            device = self.api.devices.get_device_by_serial_number(serial_number=serial_number)
            return device
        except Exception as e:
            raise ValueError(f"Failed to get PnP device info: {str(e)}")
        
    def get_pnp_workflow_tasks(self, workflow_id):
        try:
            tasks = self.api.pnp.get_workflow_tasks(workflow_id=workflow_id)
            return tasks
        except:
            raise ValueError("Failed to get PnP workflow tasks.")
        
    def get_pnp_workflow_count(self):
        try:
            count = self.api.pnp.get_workflow_count()
            return count
        except:
            raise ValueError("Failed to get PnP workflow count.")
        
    def start_pnp_workflow(self, project_id, workflow_name, devices):
        try:
            payload = {
                "type": "Default",
                "duration": "PT2M",
                "settings": {
                    "data": {
                        "project_id": project_id,
                        "workflow_name": workflow_name,
                        "devices": devices
                    }
                }
            }
            response = self.api.pnp.start_workflow(json.dumps(payload))
            return response
        except:
            raise ValueError("Failed to start PnP workflow.")

