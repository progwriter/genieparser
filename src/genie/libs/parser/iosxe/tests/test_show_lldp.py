#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_lldp import ShowLldp, ShowLldpEntry, \
                                   ShowLldpNeighborsDetail, \
                                   ShowLldpTraffic, \
                                   ShowLldpInterface


class test_show_lldp(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "hello_timer": 30,
        "enabled": True,
        "hold_timer": 120,
        "status": "active",
        "reinit_timer": 2
    }

    golden_output = {'execute.return_value': '''\
        Global LLDP Information:
          Status: ACTIVE
          LLDP advertisements are sent every 30 seconds
          LLDP hold time advertised is 120 seconds
          LLDP interface reinitialisation delay is 2 seconds
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldp(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldp(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_entry(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet2/0/15': {
                'if_name': 'GigabitEthernet2/0/15',
                'port_id': {
                    'GigabitEthernet1/0/4': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/4',
                                'port_description': 'GigabitEthernet1/0/4',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 112,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/16': {
                'if_name': 'GigabitEthernet1/0/16',
                'port_id': {
                    'GigabitEthernet1/0/2': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/2',
                                'port_description': 'GigabitEthernet1/0/2',
                                'system_name': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'time_remaining': 111,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/17': {
                'if_name': 'GigabitEthernet1/0/17',
                'port_id': {
                    'GigabitEthernet1/0/3': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/3',
                                'port_description': 'GigabitEthernet1/0/3',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 108,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/15': {
                'if_name': 'GigabitEthernet1/0/15',
                'port_id': {
                    'GigabitEthernet1/0/1': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/1',
                                'port_description': 'GigabitEthernet1/0/1',
                                'system_name': 'R5',
                                'time_remaining': 108,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            },
        'total_entries': 4,
        }

    golden_output = {'execute.return_value': '''\
        Capability codes:
            (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
            (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other
        ------------------------------------------------
        Local Intf: Gi2/0/15
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/4
        Port Description: GigabitEthernet1/0/4
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 112 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/16
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/2
        Port Description: GigabitEthernet1/0/2
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 111 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/17
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/3
        Port Description: GigabitEthernet1/0/3
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 108 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/15
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/1
        Port Description: GigabitEthernet1/0/1
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 108 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1


        Total entries displayed: 4
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpEntry(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(entry='GigabitEthernet1/0/19')

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpEntry(device=self.dev_c3850)
        parsed_output = obj.parse(entry='*')
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_neighbor_detail(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet2/0/15': {
                'if_name': 'GigabitEthernet2/0/15',
                'port_id': {
                    'GigabitEthernet1/0/4': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/4',
                                'port_description': 'GigabitEthernet1/0/4',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 101,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/16': {
                'if_name': 'GigabitEthernet1/0/16',
                'port_id': {
                    'GigabitEthernet1/0/2': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/2',
                                'port_description': 'GigabitEthernet1/0/2',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'system_name': 'R5',
                                'time_remaining': 99,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/17': {
                'if_name': 'GigabitEthernet1/0/17',
                'port_id': {
                    'GigabitEthernet1/0/3': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/3',
                                'port_description': 'GigabitEthernet1/0/3',
                                'system_name': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'time_remaining': 94,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            'GigabitEthernet1/0/15': {
                'if_name': 'GigabitEthernet1/0/15',
                'port_id': {
                    'GigabitEthernet1/0/1': {
                        'neighbors': {
                            'R5': {
                                'neighbor_id': 'R5',
                                'chassis_id': '843d.c638.b980',
                                'port_id': 'GigabitEthernet1/0/1',
                                'port_description': 'GigabitEthernet1/0/1',
                                'system_name': 'R5',
                                'system_description': 'Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Thu 21-Jul-11 01:23 by prod_rel_team',
                                'time_remaining': 98,
                                'capabilities': {
                                    'mac_bridge': {
                                        'name': 'mac_bridge',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    'router': {
                                        'name': 'router',
                                        'system': True,
                                        'enabled': True,
                                        },
                                    },
                                'management_address': '10.9.1.1',
                                'auto_negotiation': 'supported, enabled',
                                'physical_media_capabilities': ['1000baseT(FD)', '100base-TX(FD)', '100base-TX(HD)', '10base-T(FD)', '10base-T(HD)'],
                                'unit_type': 30,
                                'vlan_id': 1,
                                },
                            },
                        },
                    },
                },
            },
        'total_entries': 4,
        }

    golden_output = {'execute.return_value': '''\
        ------------------------------------------------
        Local Intf: Gi2/0/15
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/4
        Port Description: GigabitEthernet1/0/4
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 101 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/16
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/2
        Port Description: GigabitEthernet1/0/2
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 99 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/17
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/3
        Port Description: GigabitEthernet1/0/3
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 94 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1

        ------------------------------------------------
        Local Intf: Gi1/0/15
        Chassis id: 843d.c638.b980
        Port id: Gi1/0/1
        Port Description: GigabitEthernet1/0/1
        System Name: R5

        System Description: 
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(58)SE2, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2011 by Cisco Systems, Inc.
        Compiled Thu 21-Jul-11 01:23 by prod_rel_team

        Time remaining: 98 seconds
        System Capabilities: B,R
        Enabled Capabilities: B,R
        Management Addresses:
            IP: 10.9.1.1
        Auto Negotiation - supported, enabled
        Physical media capabilities:
            1000baseT(FD)
            100base-TX(FD)
            100base-TX(HD)
            10base-T(FD)
            10base-T(HD)
        Media Attachment Unit type: 30
        Vlan ID: 1


        Total entries displayed: 4
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpNeighborsDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpNeighborsDetail(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_traffic(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "frame_in": 13315,
        "frame_out": 20372,
        "frame_error_in": 0,
        "frame_discard": 14,
        "tlv_discard": 0,
        'tlv_unknown': 0,
        'entries_aged_out': 34
    }

    golden_output = {'execute.return_value': '''\
        LLDP traffic statistics:
          Total frames out: 20372
          Total entries aged: 34
          Total frames in: 13315
          Total frames received in error: 0
          Total frames discarded: 14
          Total TLVs discarded: 0
          Total TLVs unrecognized: 0
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_lldp_interface(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet1/0/15': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet1/0/16': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet1/0/17': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
            'GigabitEthernet2/0/15': {
                'tx': 'enabled',
                'rx': 'enabled',
                'tx_state': 'idle',
                'rx_state': 'wait for frame',
            },
        }        
    }

    golden_output = {'execute.return_value': '''\
        GigabitEthernet1/0/15:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME

        GigabitEthernet1/0/16:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME

        GigabitEthernet1/0/17:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME

        GigabitEthernet2/0/15:
            Tx: enabled
            Rx: enabled
            Tx state: IDLE
            Rx state: WAIT FOR FRAME
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpInterface(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)





if __name__ == '__main__':
    unittest.main()

