import json
from cisco_device import CiscoDevice
from box2 import BoxClient
from device_integration_tests import Access_Sw_Tests
from utility import XLSWriter, PingDevice
import os
import datetime
import argparse



now = datetime.datetime.now()
date_time_string = now.strftime("%Y-%m-%d_%H-%M-%S")


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", help="Store Type and 4 digits of the store number", required=True)
args = parser.parse_args()

cisco_switch = args.data + 'X01'
cisco_cellular_router = args.data + 'C01'
wti = args.data + 'S01'
vce = args.data + 'D01'
store_number = args.data


device = CiscoDevice(cisco_switch)

if device.find_prompt():
    print( device.find_prompt())
    base_device_list = [cisco_switch] #print(#cisco_cellular_router, wti, vce)

device_list=[]

for device in base_device_list:
    if PingDevice(device).ping():
        device_list.append(device)

#device_list = [f'{args}X01']

#device_list=['10.60.31.132', '10.61.111.132']
box_folder_id = '195121193192'

xls_writer = XLSWriter(f'{store_number}_{date_time_string}_store_test_results.xlsx')
xls_writer.add_sheet(sheetname="Sheet")
xls_writer.write_single_row_data(sheetname='Sheet', data=["DEVICE", "TEST", "DEVICE RESPONSE", "RESULT"],bold=True, italic=False, font_color='FF000000')

for dev in device_list:
    device = CiscoDevice(dev)
    test = Access_Sw_Tests(device)

    #ADD HERE MORE TESTS
    test_list = [test.check_os_version(), 
                 test.check_cdp_neighbor_number(),
                 test.check_cdp_cellular_router_interface(),
                 test.check_platform(),
                 test.check_number_of_sw_per_stack(),
                 test.check_modes_of_sw_stack(),
                 test.check_device_interface_status(interface='GigabitEthernet1/0/1'),
                 test.check_device_interface_status(interface='GigabitEthernet1/0/3'),
                 test.check_device_interface_status(interface='GigabitEthernet1/0/4'),
                 test.check_device_interface_status(interface='GigabitEthernet1/0/5'),
                 test.check_device_interface_status(interface='GigabitEthernet1/0/9'),
                 test.check_device_interface_status(interface='GigabitEthernet1/0/10'),
                 test.check_device_interface_status(interface='GigabitEthernet2/0/1'),
                 test.check_device_interface_status(interface='GigabitEthernet2/0/3'),
                 test.check_device_interface_status(interface='GigabitEthernet2/0/4'),
                 test.check_device_interface_status(interface='GigabitEthernet2/0/5'),
                 test.check_device_interface_status(interface='GigabitEthernet2/0/10'),
                 test.check_interface_description(interface='GigabitEthernet1/0/1'),
                 test.check_interface_description(interface='GigabitEthernet1/0/2'),
                 test.check_interface_description(interface='GigabitEthernet1/0/3'),
                 test.check_interface_description(interface='GigabitEthernet1/0/4'),
                 test.check_interface_description(interface='GigabitEthernet1/0/5'),
                 test.check_interface_description(interface='GigabitEthernet1/0/6'),
                 test.check_interface_description(interface='GigabitEthernet1/0/7'),
                 test.check_interface_description(interface='GigabitEthernet1/0/8'),
                 test.check_interface_description(interface='GigabitEthernet1/0/9'),
                 test.check_interface_description(interface='GigabitEthernet1/0/10'),
                 test.check_interface_description(interface='GigabitEthernet2/0/1'),
                 test.check_interface_description(interface='GigabitEthernet2/0/2'),
                 test.check_interface_description(interface='GigabitEthernet2/0/3'),
                 test.check_interface_description(interface='GigabitEthernet2/0/4'),
                 test.check_interface_description(interface='GigabitEthernet2/0/5'),
                 test.check_interface_description(interface='GigabitEthernet2/0/6'),
                 test.check_interface_description(interface='GigabitEthernet2/0/7'),
                 test.check_interface_description(interface='GigabitEthernet2/0/8'),
                 test.check_interface_description(interface='GigabitEthernet2/0/9'),
                 test.check_interface_description(interface='GigabitEthernet2/0/10'),
                 test.check_aaa_configuration(),
                 test.check_psu_status(),
                 test.check_number_of_psu()
                 ]

    for test in test_list:
        test_result = test
        xls_writer.write_single_row_data(sheetname='Sheet', data=[device.hostname, test_result['test_name'], test_result['response'],test_result['test_status']],bold=test_result['bold'], italic=test_result['italic'], font_color=test_result['font_color'])
        xls_writer.save()


box_client = BoxClient()

client = BoxClient().get_client()

box_client.upload_file(client, folder_id=box_folder_id, file_name=f'{store_number}_{date_time_string}_store_test_results.xlsx')


#print(box_client.get_folder_contents(client, folder_id=box_folder_id))
#box_client.get_url_link(client, file_id=None)

box_folder_content=box_client.get_folder_contents(client, folder_id=box_folder_id)

for file in box_folder_content:
    if file['name'] == f'{store_number}_{date_time_string}_store_test_results.xlsx':
        link_description = box_client.get_url_link(client, file_id=file['id'])
        link = link_description['url']
        box_directory = f'https://nike.ent.box.com/folder/{box_folder_id}'
        print('\033[1;31m---------------------------------------------------------------------------\033[0m')
        print(f'\033[1;34mBOX DIRECTORY: ~~~> \033[0m \033[1;35m{box_directory}\033[0m')
        print(f'\033[1;34mREPORT NAME:   ~~~> \033[0m \033[1;35m{store_number}_{date_time_string}_store_test_results.xlsx\033[0m')
        print('\n')
        print(f'\033[1;34mDOWNLOAD LINK  ~~~> \033[0m \033[1;36m{link}\033[0m')
             
file_path = f'{store_number}_{date_time_string}_store_test_results.xlsx'

# Remove the file
os.remove(file_path)
