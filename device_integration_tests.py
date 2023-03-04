from cisco_device import CiscoDevice
import standards
import environment


class Cellular_Router_Tests():

    def __init__(self, device:object) -> None:
        
        self.device = device


    def check_os_version(self):
        pass

    def check_interface_description(self, interface=None):
        pass
    



class Access_Sw_Tests():

    TEST_NUMBER = 1
    
    def __init__(self, device:object) -> None:
        
        self.device = device


    def check_os_version(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : System OS Version Test - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_os_version_info()
        if response == standards.SW_9300_OS_VERSION:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'PASSED',
                    'response': response,
                    'test_name': 'Platform OS Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'FAILED',
                    'response': response,
                    'test_name': 'Platform OS Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
        

    def check_number_of_sw_per_stack(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Switch Stack Member Count - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_number_of_sw_stack_info()
        if response == standards.SW_NUM_OF_STACK_MEMBER:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'PASSED',
                    'response': response,
                    'test_name': 'Number of CDP Neighbor per device.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'FAILED',
                    'response': response,
                    'test_name': 'Number of CDP Neighbor per device.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
        
    def check_modes_of_sw_stack(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Switch Stack Mode Test - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_modes_of_sw_stack_info()
        if all(value == standards.SW_MODE for value in response.values()):
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'PASSED',
                    'response': str(response),
                    'test_name': 'Device Mode Test.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'FAILED',
                    'response': str(response),
                    'test_name': 'Device Mode Test.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
    
    def check_device_interface_status(self, interface=None):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Switch Interface Status Test- {interface} - \033[1;33m{self.device.hostname}\033[0m')
        if interface:
            response = self.device.get_ip_interface_brief('genie')['interface'][interface]
            if response['status'] == 'up' and response['protocol'] == 'up':
                Access_Sw_Tests.TEST_NUMBER +=1
                return {'test_status': 'PASSED',
                    'response': 'Status: ' + str(response['status']) + '  -  ' + ' Protocol : ' + str(response['protocol']),
                    'test_name': f'Device Interface {interface} Status Test.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
            else:
                Access_Sw_Tests.TEST_NUMBER +=1
                return {'test_status': 'FAILED',
                    'response': 'Status: ' + str(response['status']) + '  -  ' + ' Protocol : ' + str(response['protocol']),
                    'test_name': f'Device Interface {interface} Status Test.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
        return self.device.get_ip_interface_brief('genie')
    

    def check_cdp_neighbor_number(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Switch CDP Neighbor Number Test - \033[1;33m{self.device.hostname}\033[0m')
        response = len(self.device.get_cdp_neighbor('genie')['cdp']['index'].keys())
        if response > 2:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'PASSED',
                    'response': response,
                    'test_name': 'Number of CDP Neighbor per device.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'FAILED',
                    'response': response,
                    'test_name': 'Number of CDP Neighbor per device.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
        
    
    def check_cdp_cellular_router_interface(self):
        """
        Check if a cellular router is connected to the specified interface of the device via Cisco Discovery Protocol (CDP).

        Returns True if a cellular router with a platform name containing "C819" or "C1111" is detected on the specified interface GigabitEthernet1/0/9, otherwise returns False.

        Args:
         - self: The instance of the class calling this method.

        Returns:
        - bool: True if a cellular router is detected on the specified interface, False otherwise.
        """
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Switch POLR Interface Test - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_cdp_neighbor('genie')['cdp']['index']
        for dev in response.keys():
            if response[dev]['local_interface'] == 'GigabitEthernet1/0/9' and ("C819" in response[dev]['platform'] or "C1111" in response[dev]['platform']):
                Access_Sw_Tests.TEST_NUMBER +=1
                return {'test_status': 'PASSED',
                    'response': 'GigabitEthernet1/0/9 is connected to Cellular Router',
                    'test_name': 'Switch Stack POLR connection Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        Access_Sw_Tests.TEST_NUMBER +=1
        return {'test_status': 'FAILED',
                    'response': 'GigabitEthernet1/0/9 is not connected to Cellular Router',
                    'test_name': 'Switch Stack POLR connection Test.',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
    
    def check_psu_status(self):
        response = self.device.get_ps_info('genie')['slot']
        return response

    def check_platform(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Switch Platform Test \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_platform('genie')['slot']
        platform_list = []
        for dev in list(response.keys()):
            platform_list.append(list(response[dev]["rp"].keys()))
        for inner_list in platform_list:
            if standards.SW_9300_PLATFORM in inner_list[0] or standards.SW_3660_PLATFORM in inner_list[0]:
                Access_Sw_Tests.TEST_NUMBER +=1
                return {'test_status': 'PASSED',
                    'response': str(platform_list),
                    'test_name': 'Switch Platform Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
            else:
                Access_Sw_Tests.TEST_NUMBER +=1
                return {'test_status': 'FAILED',
                    'response': str(platform_list),
                    'test_name': 'Switch Platform Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
                
    def check_interface_description(self, interface=None):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Interface Description Test -  {interface} - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_interface_description_individual(interface=interface)
        if response == standards.int_description_dict[interface]:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'PASSED',
                    'response': response,
                    'test_name': f'{interface} description test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'FAILED',
                    'response': response,
                    'test_name': f'{interface} description test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }

    def check_aaa_configuration(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Device AAA Configuration Test - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.find_prompt()
        if response:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'PASSED',
                    'response': response,
                    'test_name': 'Device AAA Configuration Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            Access_Sw_Tests.TEST_NUMBER +=1
            return {'test_status': 'FAILED',
                    'response': response,
                    'test_name': 'Device AAA Configuration Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }

    def check_psu_status(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Device PSU Status Test - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_ps_info('textfsm')
        for d in response:
            if d['status'] != 'OK' or d['sys_pwr'] != 'Good':
                return {'test_status': 'FAILED',
                    'response': 'PSU statuses are NOT OK',
                    'test_name': 'Device PSU Status Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }
            return {'test_status': 'PASSED',
                    'response': 'All the PSU statuses are OK',
                    'test_name': 'Device PSU Status Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }

    def check_number_of_psu(self):
        if environment.VERBOSE:
            print(f'\033[1;32mTest-{Access_Sw_Tests.TEST_NUMBER}\033[0m : Device Active PSU Number Test - \033[1;33m{self.device.hostname}\033[0m')
        response = self.device.get_ps_info('textfsm')
        
        if int(len(response)) == int(self.device.get_number_of_sw_stack_info()):
            return {'test_status': 'PASSED',
                    'response': f'Active PSU number is {len(response)}',
                    'test_name': 'Device Active PSU Number Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FF000000'
                       }
        else:
            return {'test_status': 'FAILED',
                    'response': f'Active PSU number is {len(response)}',
                    'test_name':'Device Active PSU Number Test',
                     'bold':False,
                     'italic':False,
                     'font_color':'FFFF0000'
                       }