
"""
This module contains a set of predefined infrastructure standards for the retail environment. These standards serve as a reference point for development teams, helping to ensure consistency and reliability across systems and applications.

The following infrastructure standards are currently defined in this module:

- CELLULAR_ROUTER_OS_VERSION: the version number of the cellular router operating system (OS).
- SW_9300_OS_VERSION: the version number of the operating system for the Cisco Catalyst 9300 switch.
- SW_3650_OS_VERSION: the version number of the operating system for the Cisco Catalyst 3650 switch.
- SW_NUM_OF_STACK_MEMBER: the number of members in the switch stack.
- SW_9300_LICENCE_PACKAGE: the license package for the Cisco Catalyst 9300 switch.
- SW_9300_SYSTEM_IMAGE: the system image for the Cisco Catalyst 9300 switch.
- SW_MODE: the software installation mode for the Cisco Catalyst switches.

By utilizing these predefined standards, development teams can reduce errors, improve efficiency, and ensure consistency across infrastructure components. These standards are subject to review and update as needed to keep pace with evolving infrastructure requirements.
"""

CELLULAR_ROUTER_OS_VERSION='17.3.5'
SW_9300_OS_VERSION='17.3.5'
SW_3650_OS_VERSION='17.3.5'
SW_NUM_OF_STACK_MEMBER=3
SW_9300_LICENCE_PACKAGE='dna-essentials'
SW_9300_SYSTEM_IMAGE='flash:packages.conf'
SW_MODE='INSTALL'
SW_9300_PLATFORM='C9300-48U'
SW_9300_PLATFORM_INFO='Catalyst L3 Switch'
SW_3660_PLATFORM='C9300-48U'




#SW INTERFACE DESCRIPTION STANDARDS
####################################
# Naming convention:
# SW <SW_NR_IN_THE_STACK>_INT_<PORT_NUMBER>
# e.g.: SW1_INT_1 -> (Gi1/0/1)

SW1_INT_1='VCE1_LAN3'
SW1_INT_10='DEMARC_WANA'
SW1_INT_11='WAP'
SW1_INT_12='WAP'
SW1_INT_13='WAP'
SW1_INT_14='WAP'
SW1_INT_15='WAP'
SW1_INT_16='WAP'
SW1_INT_17='WAP'
SW1_INT_18='WAP'
SW1_INT_19='WAP'
SW1_INT_2='//RESERVED_VCE//'
SW1_INT_20='WAP'
SW1_INT_21='CE_DE'
SW1_INT_22='CE_DE'
SW1_INT_23='PoE '
SW1_INT_24='NVR '
SW1_INT_25='VSAM'
SW1_INT_26='BoH '
SW1_INT_27='mPOS Wired '
SW1_INT_28='mPOS Wired '
SW1_INT_29='Cash Drawer'
SW1_INT_3='VCE1_GE1_WANA'
SW1_INT_30='Cash Drawer'
SW1_INT_31='Cash Drawer'
SW1_INT_32='BOH'
SW1_INT_33='BOH'
SW1_INT_34='BOH'
SW1_INT_35='BOH'
SW1_INT_36='BOH'
SW1_INT_37=''
SW1_INT_38=''
SW1_INT_39=''
SW1_INT_4='VCE2_GE1_WANA'
SW1_INT_40=''
SW1_INT_41='POS'
SW1_INT_42='POS'
SW1_INT_43='POS'
SW1_INT_44='EBPN'
SW1_INT_45='Server'
SW1_INT_46='Server'
SW1_INT_47='Server'
SW1_INT_48='Server'
SW1_INT_5='VCE1_SFP2_POLR'
SW1_INT_6='VCE1_SFP1'
SW1_INT_7='//RESERVED_VOICE//'
SW1_INT_8='//RESERVED_VCE//'
SW1_INT_9='DEMARC_POLR'
SW2_INT_1='VCE2_LAN3'
SW2_INT_10='DEMARC_WANB'
SW2_INT_11='WAP'
SW2_INT_12='WAP'
SW2_INT_13='WAP'
SW2_INT_14='WAP'
SW2_INT_15='WAP'
SW2_INT_16='WAP'
SW2_INT_17='WAP'
SW2_INT_18='WAP'
SW2_INT_19='WAP'
SW2_INT_2='//RESERVED_VCE//'
SW2_INT_20='WAP'
SW2_INT_21='CE_DE'
SW2_INT_22='CE_DE_FoH_Mac_Mini'
SW2_INT_23='PoE '
SW2_INT_24='VSAM'
SW2_INT_25='VSAM'
SW2_INT_26=''
SW2_INT_27='mPOS Wired '
SW2_INT_28='mPOS Wired '
SW2_INT_29='Cash Drawer'
SW2_INT_3='VCE1_GE2_WANB'
SW2_INT_30='Cash Drawer'
SW2_INT_31='Cash Drawer'
SW2_INT_32='BOH'
SW2_INT_33='BOH'
SW2_INT_34='BOH'
SW2_INT_35='BOH'
SW2_INT_36='BOH'
SW2_INT_37=''
SW2_INT_38=''
SW2_INT_39=''
SW2_INT_4='VCE2_GE2_WANB'
SW2_INT_40=''
SW2_INT_41='POS'
SW2_INT_42='POS'
SW2_INT_43='POS'
SW2_INT_44='EBPN'
SW2_INT_45='Server'
SW2_INT_46='Server'
SW2_INT_47='Server'
SW2_INT_48='Server'
SW2_INT_5='VCE2_SFP2_POLR'
SW2_INT_6='VCE2_SFP1'
SW2_INT_7='//RESERVED_VOICE//'
SW2_INT_8='//RESERVED_VCE//'
SW2_INT_9='DEMARC_WANC'
SW3_INT_1='Self-Checkout_iPAD_04'
SW3_INT_10='WAP'
SW3_INT_11='WAP'
SW3_INT_12='WAP'
SW3_INT_13='WAP'
SW3_INT_14='WAP'
SW3_INT_15='WAP'
SW3_INT_16='WAP'
SW3_INT_17='WAP'
SW3_INT_18='WAP'
SW3_INT_19='WAP'
SW3_INT_2='Self-Checkout_Printer_04'
SW3_INT_20='WAP'
SW3_INT_21='CE_DE'
SW3_INT_22='CE_DE'
SW3_INT_23='PoE '
SW3_INT_24='VSAM'
SW3_INT_25='VSAM'
SW3_INT_26='mPOS Wired '
SW3_INT_27='mPOS Wired '
SW3_INT_28='mPOS Wired '
SW3_INT_29='Cash Drawer'
SW3_INT_3='Self-Checkout_Payment-Terminal_04'
SW3_INT_30='Cash Drawer'
SW3_INT_31='Cash Drawer'
SW3_INT_32='BOH'
SW3_INT_33='BOH'
SW3_INT_34='BOH'
SW3_INT_35='BOH'
SW3_INT_36='BOH'
SW3_INT_37=''
SW3_INT_38=''
SW3_INT_39=''
SW3_INT_4='Self-Checkout_Reserved_04'
SW3_INT_40=''
SW3_INT_41='POS'
SW3_INT_42='POS'
SW3_INT_43='POS'
SW3_INT_44='EBPN'
SW3_INT_45='Server'
SW3_INT_46='Server'
SW3_INT_47='Server'
SW3_INT_48='Server'
SW3_INT_5='WAP'
SW3_INT_6='WAP'
SW3_INT_7='WAP'
SW3_INT_8='WAP'
SW3_INT_9='WAP'

int_description_dict = {'GigabitEthernet1/0/1':'VCE1_LAN3',
                        'GigabitEthernet1/0/10':'DEMARC_WANA',
                        'GigabitEthernet1/0/11':'WAP',
                        'GigabitEthernet1/0/12':'WAP',
                        'GigabitEthernet1/0/13':'WAP',
                        'GigabitEthernet1/0/14':'WAP',
                        'GigabitEthernet1/0/15':'WAP',
                        'GigabitEthernet1/0/16':'WAP',
                        'GigabitEthernet1/0/17':'WAP',
                        'GigabitEthernet1/0/18':'WAP',
                        'GigabitEthernet1/0/19':'WAP',
                        'GigabitEthernet1/0/2':'//RESERVED_VCE//',
                        'GigabitEthernet1/0/20':'WAP',
                        'GigabitEthernet1/0/21':'CE_DE',
                        'GigabitEthernet1/0/22':'CE_DE',
                        'GigabitEthernet1/0/23':'PoE ',
                        'GigabitEthernet1/0/24':'NVR ',
                        'GigabitEthernet1/0/25':'VSAM',
                        'GigabitEthernet1/0/26':'BoH ',
                        'GigabitEthernet1/0/27':'mPOS Wired ',
                        'GigabitEthernet1/0/28':'mPOS Wired ',
                        'GigabitEthernet1/0/29':'Cash Drawer',
                        'GigabitEthernet1/0/3':'VCE1_GE1_WANA',
                        'GigabitEthernet1/0/30':'Cash Drawer',
                        'GigabitEthernet1/0/31':'Cash Drawer',
                        'GigabitEthernet1/0/32':'BOH',
                        'GigabitEthernet1/0/33':'BOH',
                        'GigabitEthernet1/0/34':'BOH',
                        'GigabitEthernet1/0/35':'BOH',
                        'GigabitEthernet1/0/36':'BOH',
                        'GigabitEthernet1/0/37':'',
                        'GigabitEthernet1/0/38':'',
                        'GigabitEthernet1/0/39':'',
                        'GigabitEthernet1/0/4':'VCE2_GE1_WANA',
                        'GigabitEthernet1/0/40':'',
                        'GigabitEthernet1/0/41':'POS',
                        'GigabitEthernet1/0/42':'POS',
                        'GigabitEthernet1/0/43':'POS',
                        'GigabitEthernet1/0/44':'EBPN',
                        'GigabitEthernet1/0/45':'Server',
                        'GigabitEthernet1/0/46':'Server',
                        'GigabitEthernet1/0/47':'Server',
                        'GigabitEthernet1/0/48':'Server',
                        'GigabitEthernet1/0/5':'VCE1_SFP2_POLR',
                        'GigabitEthernet1/0/6':'VCE1_SFP1',
                        'GigabitEthernet1/0/7':'//RESERVED_VOICE//',
                        'GigabitEthernet1/0/8':'//RESERVED_VCE//',
                        'GigabitEthernet1/0/9':'DEMARC_POLR',
                        'GigabitEthernet2/0/1':'VCE2_LAN3',
                        'GigabitEthernet2/0/10':'DEMARC_WANB',
                        'GigabitEthernet2/0/11':'WAP',
                        'GigabitEthernet2/0/12':'WAP',
                        'GigabitEthernet2/0/13':'WAP',
                        'GigabitEthernet2/0/14':'WAP',
                        'GigabitEthernet2/0/15':'WAP',
                        'GigabitEthernet2/0/16':'WAP',
                        'GigabitEthernet2/0/17':'WAP',
                        'GigabitEthernet2/0/18':'WAP',
                        'GigabitEthernet2/0/19':'WAP',
                        'GigabitEthernet2/0/2':'//RESERVED_VCE//',
                        'GigabitEthernet2/0/20':'WAP',
                        'GigabitEthernet2/0/21':'CE_DE',
                        'GigabitEthernet2/0/22':'CE_DE_FoH_Mac_Mini',
                        'GigabitEthernet2/0/23':'PoE ',
                        'GigabitEthernet2/0/24':'VSAM',
                        'GigabitEthernet2/0/25':'VSAM',
                        'GigabitEthernet2/0/26':'',
                        'GigabitEthernet2/0/27':'mPOS Wired ',
                        'GigabitEthernet2/0/28':'mPOS Wired ',
                        'GigabitEthernet2/0/29':'Cash Drawer',
                        'GigabitEthernet2/0/3':'VCE1_GE2_WANB',
                        'GigabitEthernet2/0/30':'Cash Drawer',
                        'GigabitEthernet2/0/31':'Cash Drawer',
                        'GigabitEthernet2/0/32':'BOH',
                        'GigabitEthernet2/0/33':'BOH',
                        'GigabitEthernet2/0/34':'BOH',
                        'GigabitEthernet2/0/35':'BOH',
                        'GigabitEthernet2/0/36':'BOH',
                        'GigabitEthernet2/0/37':'',
                        'GigabitEthernet2/0/38':'',
                        'GigabitEthernet2/0/39':'',
                        'GigabitEthernet2/0/4':'VCE2_GE2_WANB',
                        'GigabitEthernet2/0/40':'',
                        'GigabitEthernet2/0/41':'POS',
                        'GigabitEthernet2/0/42':'POS',
                        'GigabitEthernet2/0/43':'POS',
                        'GigabitEthernet2/0/44':'EBPN',
                        'GigabitEthernet2/0/45':'Server',
                        'GigabitEthernet2/0/46':'Server',
                        'GigabitEthernet2/0/47':'Server',
                        'GigabitEthernet2/0/48':'Server',
                        'GigabitEthernet2/0/5':'VCE2_SFP2_POLR',
                        'GigabitEthernet2/0/6':'VCE2_SFP1',
                        'GigabitEthernet2/0/7':'//RESERVED_VOICE//',
                        'GigabitEthernet2/0/8':'//RESERVED_VCE//',
                        'GigabitEthernet2/0/9':'DEMARC_WANC',
                        'GigabitEthernet3/0/1':'Self-Checkout_iPAD_04',
                        'GigabitEthernet3/0/10':'WAP',
                        'GigabitEthernet3/0/11':'WAP',
                        'GigabitEthernet3/0/12':'WAP',
                        'GigabitEthernet3/0/13':'WAP',
                        'GigabitEthernet3/0/14':'WAP',
                        'GigabitEthernet3/0/15':'WAP',
                        'GigabitEthernet3/0/16':'WAP',
                        'GigabitEthernet3/0/17':'WAP',
                        'GigabitEthernet3/0/18':'WAP',
                        'GigabitEthernet3/0/19':'WAP',
                        'GigabitEthernet3/0/2':'Self-Checkout_Printer_04',
                        'GigabitEthernet3/0/20':'WAP',
                        'GigabitEthernet3/0/21':'CE_DE',
                        'GigabitEthernet3/0/22':'CE_DE',
                        'GigabitEthernet3/0/23':'PoE ',
                        'GigabitEthernet3/0/24':'VSAM',
                        'GigabitEthernet3/0/25':'VSAM',
                        'GigabitEthernet3/0/26':'mPOS Wired ',
                        'GigabitEthernet3/0/27':'mPOS Wired ',
                        'GigabitEthernet3/0/28':'mPOS Wired ',
                        'GigabitEthernet3/0/29':'Cash Drawer',
                        'GigabitEthernet3/0/3':'Self-Checkout_Payment-Terminal_04',
                        'GigabitEthernet3/0/30':'Cash Drawer',
                        'GigabitEthernet3/0/31':'Cash Drawer',
                        'GigabitEthernet3/0/32':'BOH',
                        'GigabitEthernet3/0/33':'BOH',
                        'GigabitEthernet3/0/34':'BOH',
                        'GigabitEthernet3/0/35':'BOH',
                        'GigabitEthernet3/0/36':'BOH',
                        'GigabitEthernet3/0/37':'',
                        'GigabitEthernet3/0/38':'',
                        'GigabitEthernet3/0/39':'',
                        'GigabitEthernet3/0/4':'Self-Checkout_Reserved_04',
                        'GigabitEthernet3/0/40':'',
                        'GigabitEthernet3/0/41':'POS',
                        'GigabitEthernet3/0/42':'POS',
                        'GigabitEthernet3/0/43':'POS',
                        'GigabitEthernet3/0/44':'EBPN',
                        'GigabitEthernet3/0/45':'Server',
                        'GigabitEthernet3/0/46':'Server',
                        'GigabitEthernet3/0/47':'Server',
                        'GigabitEthernet3/0/48':'Server',
                        'GigabitEthernet3/0/5':'WAP',
                        'GigabitEthernet3/0/6':'WAP',
                        'GigabitEthernet3/0/7':'WAP',
                        'GigabitEthernet3/0/8':'WAP',
                        'GigabitEthernet3/0/9':'WAP'
                        }
