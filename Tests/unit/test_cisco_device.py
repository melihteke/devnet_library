import unittest
from cisco_device import CiscoDevice
import json
import sys

class TestCiscoDevice(unittest.TestCase):
    
    def setUp(self):
        self.device = CiscoDevice('NER0502X01')
    
    def test_get_show_version(self):
        #output = self.device.get_show_version()
        with open('tests/mock_data/cisco_device_get_show_version.json', 'r') as f:
            output = json.load(f)
        self.assertIsInstance(output, dict)
        #self.assertListEqual(list(output.keys()), output)
        
    def test_get_chassis_info(self):
        #output = self.device.get_chassis_info()
        with open('tests/mock_data/cisco_get_chassis_info.txt', 'r') as f:
            output = f.readline()
        self.assertIsInstance(output, str)

    def test_get_image_id_info(self):
        #output = self.device.get_image_id_info()
        with open('tests/mock_data/cisco_get_image_id_info.txt', 'r') as f:
            output = f.readline()
        self.assertIsInstance(output, str)
        
    def test_get_platform_info(self):
        #output = self.device.get_platform_info()
        with open('tests/mock_data/cisco_get_platform_info.txt', 'r') as f:
            output = f.readline()
        self.assertIsInstance(output, str)
        
    def test_get_number_of_sw_stack_info(self):
        output = self.device.get_number_of_sw_stack_info()
        self.assertIsInstance(output, int)
        self.assertGreater(output, 0)
        
    def test_get_modes_of_sw_stack_info(self):
        output = self.device.get_modes_of_sw_stack_info('genie')
        self.assertIsInstance(output, dict)
        self.assertGreater(len(output), 0)
        
    def test_get_os_version_info(self):
        output = self.device.get_os_version_info()
        self.assertIsInstance(output, str)
        
    def test_get_interface_description(self):
        output = self.device.get_interface_description('genie')
        self.assertIsInstance(output, dict)
        
    def test_get_ip_interface_brief(self):
        output = self.device.get_ip_interface_brief('genie')
        self.assertIsInstance(output, dict)
        
    def test_get_interface_status(self):
        output = self.device.get_interface_status('genie')
        self.assertIsInstance(output, dict)

        
if __name__ == '__main__':
    unittest.main()
