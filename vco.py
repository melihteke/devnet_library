import requests
import urllib3

urllib3.disable_warnings()


class VcoApi:
    """
    A class for interacting with the Velocloud Orchestrator (VCO) API.
    """
    def __init__(self, base_url, username, password):
        """
        Initializes a new instance of the VcoApi class.

        :param base_url: The base URL of the VCO API.
        :param username: The username to use for authentication.
        :param password: The password to use for authentication.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({"Content-Type": "application/json"})

    def list_edge_configs(self):
        """
        Retrieves a list of all edge configurations.

        :return: A JSON response containing the list of edge configurations.
        """
        url = f"{self.base_url}/config/edge"
        response = self.session.get(url)
        return response.json()

    def get_edge_config(self, edge_id):
        """
        Retrieves the configuration for a specific edge.

        :param edge_id: The ID of the edge to retrieve the configuration for.
        :return: A JSON response containing the edge configuration.
        """
        url = f"{self.base_url}/config/edge/{edge_id}"
        response = self.session.get(url)
        return response.json()

    def update_edge_config(self, edge_id, config):
        """
        Updates the configuration for a specific edge.

        :param edge_id: The ID of the edge to update the configuration for.
        :param config: The updated configuration to apply.
        :return: A JSON response containing the updated edge configuration.
        """
        url = f"{self.base_url}/config/edge/{edge_id}"
        response = self.session.put(url, json=config)
        return response.json()

    def list_enterprise_configs(self):
        """
        Retrieves a list of all enterprise configurations.

        :return: A JSON response containing the list of enterprise configurations.
        """
        url = f"{self.base_url}/config/enterprise"
        response = self.session.get(url)
        return response.json()

    def get_enterprise_config(self, enterprise_id):
        """
        Retrieves the configuration for a specific enterprise.

        :param enterprise_id: The ID of the enterprise to retrieve the configuration for.
        :return: A JSON response containing the enterprise configuration.
        """
        url = f"{self.base_url}/config/enterprise/{enterprise_id}"
        response = self.session.get(url)
        return response.json()

    def update_enterprise_config(self, enterprise_id, config):
        """
        Updates the configuration for a specific enterprise.

        :param enterprise_id: The ID of the enterprise to update the configuration for.
        :param config: The updated configuration to apply.
        :return: A JSON response containing the updated enterprise configuration.
        """
        url = f"{self.base_url}/config/enterprise/{enterprise_id}"
        response = self.session.put(url, json=config)
        return response.json()

    def list_vces(self):
        """
        Retrieves a list of all VCEs.

        :return: A JSON response containing the list of VCEs.
        """
        url = f"{self.base_url}/edges"
        response = self.session.get(url)
        return response.json()

    def get_vce_info(self, edge_id):
        """
        Retrieves information about a specific VCE.

        :param edge_id: The ID of the VCE to retrieve information for.
        :return: A JSON response containing information about the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/info"
        response = self.session.get(url)
        return response.json()

    def create_vce(self, config):
        url = f"{self.base_url}/edges"
        response = self.session.post(url, json=config)
        return response.json()

    def delete_vce(self, edge_id):
        url = f"{self.base_url}/edge/{edge_id}"
        response = self.session.delete(url)
        return response.json()

    def reboot_vce(self, edge_id):
        url = f"{self.base_url}/edge/{edge_id}/reboot"
        response = self.session.post(url)
        return response.json()

    def get_edge_health(self, edge_id):
        url = f"{self.base_url}/edge/{edge_id}/health"
        response = self.session.get(url)
        return response.json()

    def list_enterprises(self):
        url = f"{self.base_url}/enterprise"
        response = self.session.get(url)
        return response.json()

    def get_enterprise_info(self, enterprise_id):
        url = f"{self.base_url}/enterprise/{enterprise_id}/info"
        response = self.session.get(url)
        return response.json()

    def create_enterprise(self, name, description):
        url = f"{self.base_url}/enterprise"
        data = {"name": name, "description": description}
        response = self.session.post(url, json=data)
        return response.json()

    def delete_enterprise(self, enterprise_id):
        url = f"{self.base_url}/enterprise/{enterprise_id}"
        response = self.session.delete(url)
        return response.json()
    
    def update_vce_config(self, edge_id, config):
        """
        Updates the configuration for a specific VCE.

        :param edge_id: The ID of the VCE to update the configuration for.
        :param config: The updated configuration to apply.
        :return: A JSON response containing the updated VCE configuration.
        """
        url = f"{self.base_url}/edge/{edge_id}"
        response = self.session.patch(url, json=config)
        return response.json()

    def reboot_vce(self, edge_id):
        """
        Reboots a specific VCE.

        :param edge_id: The ID of the VCE to reboot.
        :return: A JSON response containing the result of the reboot operation.
        """
        url = f"{self.base_url}/edge/{edge_id}/action/reboot"
        response = self.session.post(url)
        return response.json()

    def activate_vce(self, edge_id):
        """
        Activates a specific VCE.

        :param edge_id: The ID of the VCE to activate.
        :return: A JSON response containing the result of the activation operation.
        """
        url = f"{self.base_url}/edge/{edge_id}/action/activate"
        response = self.session.post(url)
        return response.json()

    def deactivate_vce(self, edge_id):
        """
        Deactivates a specific VCE.

        :param edge_id: The ID of the VCE to deactivate.
        :return: A JSON response containing the result of the deactivation operation.
        """
        url = f"{self.base_url}/edge/{edge_id}/action/deactivate"
        response = self.session.post(url)
        return response.json()

    def get_vce_activation_key(self, edge_id):
        """
        Retrieves the activation key for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the activation key for.
        :return: A JSON response containing the activation key for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/activationKey"
        response = self.session.get(url)
        return response.json()

    def update_vce_activation_key(self, edge_id, activation_key):
        """
        Updates the activation key for a specific VCE.

        :param edge_id: The ID of the VCE to update the activation key for.
        :param activation_key: The new activation key to apply.
        :return: A JSON response containing the updated activation key for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/activationKey"
        response = self.session.put(url, json=activation_key)
        return response.json()

    def get_vce_configuration_template(self, edge_id):
        """
        Retrieves the configuration template for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the configuration template for.
        :return: A JSON response containing the configuration template for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/configTemplate"
        response = self.session.get(url)
        return response.json()

    def update_vce_configuration_template(self, edge_id, config_template):
        """
        Updates the configuration template for a specific VCE.

        :param edge_id: The ID of the VCE to update the configuration template for.
        :param config_template: The new configuration template to apply.
        :return: A JSON response containing the updated configuration template for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/configTemplate"
        response = self.session.put(url, json=config_template)
        return response.json()

    def get_vce_device_status(self, edge_id):
        """
        Retrieves the device status for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the device status for.
        :return: A JSON response containing the device status for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/deviceStatus"
        response = self.session.get(url)
        return response.json()

    def get_vce_edge_health(self, edge_id):
        """
        Retrieves the edge health for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the edge health for.
        :return: A JSON response containing the edge health for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/edgeHealth"
        response = self.session.get(url)
        return response.json()

    def get_vce_event_log(self, edge_id):
        """
        Retrieves the event log for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the event log for.
        :return: A JSON response containing the event log for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/eventLog"
        response = self.session.get(url)
        return response.json()

    def get_vce_tunnel_status(self, edge_id):
        """
        Retrieves the tunnel status for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the tunnel status for.
        :return: A JSON response containing the tunnel status for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/tunnelStatus"
        response = self.session.get(url)
        return response.json()

    def get_vce_link_status(self, edge_id):
        """
        Retrieves the link status for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the link status for.
        :return: A JSON response containing the link status for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/linkStatus"
        response = self.session.get(url)
        return response.json()

    def get_vce_interface_macs(self, edge_id):
        """
        Retrieves the MAC addresses for each interface on a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the interface MAC addresses for.
        :return: A JSON response containing the MAC addresses for each interface on the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/interfaceMac"
        response = self.session.get(url)
        return response.json()
    
    def get_vce_ha_info(self, edge_id):
        """
        Retrieves the high availability information for a specific VCE.

        :param edge_id: The ID of the VCE to retrieve the high availability information for.
        :return: A JSON response containing the high availability information for the VCE.
        """
        url = f"{self.base_url}/edge/{edge_id}/ha"
        response = self.session.get(url)
        return response.json()
    


''''
vco = VcoApi("<URL>", "username", "password")
edge_id = "1234567890"
config = {
    "configType": "fullConfig",
    "elementConfiguration": {
        "vpn": {
            "ipsec": {
                "enabled": True,
                "interfaces": {
                    "wan": {
                        "localId": "my-wan-ip-address",
                        "peerId": "remote-ip-address",
                        "sharedSecret": "my-shared-secret",
                        "enabled": True
                    }
                }
            }
        }
    }
}
response = vco.update_vce_config(edge_id, config)
print(response)
'''