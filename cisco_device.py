from netmiko import ConnectHandler
from pprint import pprint 
import environment


AD_USERNAME = environment.AD_USERNAME
AD_PASSWORD = environment.AD_PASSWORD
VERBOSE = environment.VERBOSE
DEBUG = environment.DEBUG


class CiscoDevice():

    def __init__(self, hostname):
        """
        The constructor for the CiscoDevice class.

        Args:
            hostname (str): The hostname or IP address of the remote device.
        """

        self.hostname = hostname
        self.cisco_device = { 
                "device_type": "cisco_ios",
                "host": hostname,
                "username": AD_USERNAME,
                "password": AD_PASSWORD,
                "secret": AD_PASSWORD,
            }

    def execute_command(self, command, parser=None):

        """
        Executes a command on the remote device and returns the output.
        Optionally, the output can be parsed using either the 'genie' or
        'textfsm' parser.

        Args:
            command (str): The command to be executed on the remote device.
            parser (str, optional): The parser to use for the command output. 
                Either 'genie' or 'textfsm'. Defaults to None.

        Returns:
            Union[str, Dict, List[List[str]]]: The output of the command, parsed
            or unparsed depending on the value of the 'parser' argument.

        Raises:
            ValueError: If an invalid parser is selected.
            TypeError: If an invalid command is passed.
            ConnectionError: If there is a problem connecting to the device.
        """
        try:
            if parser == 'genie':
                with ConnectHandler(**self.cisco_device) as net_connect:
                    return net_connect.send_command(command, use_genie=True)
                
            if parser == 'textfsm':
                with ConnectHandler(**self.cisco_device) as net_connect:
                    return net_connect.send_command(command, use_textfsm=True)
            elif parser is None or parser == '':
                with ConnectHandler(**self.cisco_device) as net_connect:
                    return net_connect.send_command(command)
            else:
                raise ValueError(f"Invalid parser selected: {parser}")
        except ValueError as e:
            raise e
        except TypeError as e:
            raise e
        except ConnectionError as e:
            raise e
        except Exception as e:
            raise e

    def find_prompt(self):

        with ConnectHandler(**self.cisco_device) as net_connect:
                    prompt =  net_connect.find_prompt()
                    
                    if prompt.endswith('#'):
                        return True
                    elif prompt.endswith('>'):
                        return False
                    else:
                        # handle unexpected prompt format
                        raise ValueError(f"Unexpected prompt format: {prompt}")
                    
                
    def get_show_version(self, parser=None):
        """
        Retrieve the version information from a network device.

        This method retrieves the version information of a network device by sending the "show version" command to the device. The output of the command can be parsed using either the "genie" or "textfsm" parser. If no parser is specified, the raw output of the command is returned.

        Args:
        parser (str, optional): The parser to use for parsing the output of the "show version" command. Valid values are "genie" or "textfsm". If no parser is specified, the raw output of the command is returned.

        Returns:
        str: The version information of the network device. If a parser is specified, the parsed output of the "show version" command is returned. If no parser is specified, the raw output of the command is returned.
        """
        command = "show version"
        return self.execute_command(command, parser)
    
    def get_chassis_info(self, parser='genie'):
        command = "show version"
        return self.execute_command(command, parser)['version']['chassis']

    def get_chassis(self, parser='genie'):
        command = "show chassis"
        return self.execute_command(command, parser)
    

    def get_image_id_info(self, parser='genie'):
        command = "show version"
        return self.execute_command(command, parser)['version']['image_id']

    def get_platform_info(self, parser='genie'):
        command = "show version"
        return self.execute_command(command, parser)['version']['platform']
    
    def get_platform(self, parser='genie'):
        command = "show platform"
        return self.execute_command(command, parser) 

                
    def get_number_of_sw_stack_info(self, parser='genie'):
        command = "show version"
        response = self.execute_command(command, parser)['version']['switch_num']
        return len(response.keys())

    def get_modes_of_sw_stack_info(self, parser='genie'):
        command = "show version"
        response = self.execute_command(command, parser)['version']['switch_num']
        switch_stack_modes={}
        for sw_id in response.keys():
            switch_stack_modes[sw_id]=response[sw_id]['mode']
        return switch_stack_modes
    
    def get_os_version_info(self, parser='genie'):
        command = "show version"
        return self.execute_command(command, parser)['version']['version']
    

    def get_interface_description(self, parser=None):
        """
        Retrieve the interface descriptions from a network device.

        This method retrieves the descriptions of the interfaces on a network device by sending the "show interfaces description" command to the device. The output of the command can be parsed using either the "genie" or "textfsm" parser. If no parser is specified, the raw output of the command is returned.

        Args:
        parser (str, optional): The parser to use for parsing the output of the "show interfaces description" command. Valid values are "genie" or "textfsm". If no parser is specified, the raw output of the command is returned.

        Returns:
        Union[str, Dict, List[List[str]]]: The interface descriptions of the network device. If a parser is specified, the parsed output of the "show interfaces description" command is returned. If no parser is specified, the raw output of the command is returned.
        """
        command = "show interfaces description"
        return self.execute_command(command, parser)
    
    def get_interface_description_individual(self, parser='genie', interface=None):
        command = "show interfaces description"
        response = self.execute_command(command, parser)
        if interface is None:
            raise KeyError("interface is not specified")
        try:
            return response['interfaces'][interface]['description']
        except KeyError:
            raise ValueError(f"interface {interface} not found")
        
    def get_ip_interface_brief(self, parser=None):
        command = "show ip interface brief"
        return self.execute_command(command, parser)
    
    def get_interface_status(self, parser=None):
        command = "show interfaces status"
        return self.execute_command(command, parser)
        
    def get_interfaces_status(self, parser=None):
        command = "show interfaces"
        return self.execute_command(command, parser)

    def get_interfaces_summary(self, parser=None):
        command = "show interfaces summary"
        return self.execute_command(command, parser)


    def get_cdp_neighbor(self, parser=None):
        command = "show cdp neighbor"
        return self.execute_command(command, parser)

    def get_cdp_interface(self, parser=None):
        command = "show cdp interface"
        return self.execute_command(command, parser)

    def get_lldp_neighbor(self, parser=None):
        command = "show lldp neighbor"
        return self.execute_command(command, parser)


    def get_ps_info(self, parser=None):
        command = "show environment power all"
        return self.execute_command(command, parser)
    
    def get_stack_info(self, parser=None):
        command = "show switch stack-ports"
        return self.execute_command(command, parser)

    def get_mac_address_table(self, parser=None):
        command = "show mac address-table"
        return self.execute_command(command, parser)

    def get_mac_address_table_count(self, parser=None):
        command = "show mac address-table count"
        return self.execute_command(command, parser)

    def get_vlans(self, parser=None):
        command = "show vlan"
        return self.execute_command(command, parser)

    def get_arp(self, parser=None):
        command = "show ip arp"
        return self.execute_command(command, parser)

    def get_routing_table_info(self, parser=None):
        command = "show ip route"
        return self.execute_command(command, parser)
    
    def get_ip_protocols(self, parser=None):
        command = "show ip protocols"
        return self.execute_command(command, parser)
    
    def get_eigrp_neighbors(self, parser=None):
        command = "show ip eigrp neighbors"
        return self.execute_command(command, parser)
    
    def get_eigrp_interfaces(self, parser=None):
        command = "show ip eigrp interfaces"
        return self.execute_command(command, parser)

    def get_inventory_info(self, parser=None):
        command = "show inventory"
        return self.execute_command(command, parser)
    
    def get_licence(self, parser=None):
        command = "show license"
        return self.execute_command(command, parser)
    
    def get_licence_status(self, parser=None):
        command = "show license status"
        return self.execute_command(command, parser)
    
    def get_ntp_associations(self, parser=None):
        command = "show ntp associations"
        return self.execute_command(command, parser)

    def get_power_inline(self, parser=None):
        command = "show power inline"
        return self.execute_command(command, parser)

    def get_power_inline_interface(self, parser=None, interface=None):
        command = "show power inline " + interface
        return self.execute_command(command, parser)

    def get_snmp(self, parser=None):
        command = "show snmp"
        return self.execute_command(command, parser)

    def get_snmp_group(self, parser=None):
        command = "show snmp group"
        return self.execute_command(command, parser)
    
    def get_snmp_user(self, parser=None):
        command = "show snmp user"
        return self.execute_command(command, parser)
    
    def get_switch_info(self, parser=None):
        command = "show switch"
        return self.execute_command(command, parser)

    def get_switch_detail(self, parser=None):
        command = "show switch detail"
        return self.execute_command(command, parser)

    def get_tacacs(self, parser=None):
        command = "show tacacs"
        return self.execute_command(command, parser)

    def get_access_lists(self, parser=None):
        command = "show access-lists"
        return self.execute_command(command, parser)

    def get_arp(self, parser=None):
        command = "show arp"
        return self.execute_command(command, parser)

    def get_arp_summary(self, parser=None):
        command = "show arp summary"
        return self.execute_command(command, parser)

    def get_clock(self, parser=None):
        command = "show clock"
        return self.execute_command(command, parser)

    def get_vrf_detail(self, parser=None):
        command = "show vrf detail"
        return self.execute_command(command, parser)

    def get_ip_vrf_detail(self, parser=None):
        command = "show ip vrf detail"
        return self.execute_command(command, parser)





