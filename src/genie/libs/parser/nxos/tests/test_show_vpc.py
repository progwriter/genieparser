# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
											 SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_vpc import ShowVpc


#=========================================================
# Unit test for show vpc
#=========================================================
class test_show_vpc(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'vpc_domain_id': 1,
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_per_vlan_consistency_status': 'success',
        'vpc_type_2_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 1,
        'peer_gateway': 'Enabled',
        'dual_active_excluded_vlans': '-',
        'vpc_graceful_consistency_check_status': 'Enabled',
        'vpc_auto_recovery_status': 'Enabled, timer is off.(timeout = 240s)',
        'vpc_delay_restore_status': 'Timer is off.(timeout = 30s)',
        'vpc_delay_restore_svi_status': 'Timer is off.(timeout = 10s)',
        'operational_l3_peer_router': 'Disabled',
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel101',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1,100-102,200-202,300-350'
            }
        },
        'vpc': {
            1: {
            	'vpc_id': 1,
                'vpc_ifindex': 'Port-channel1',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1,100-102,200-202'
            }
        }
	}

	golden_output = {'execute.return_value': '''
		R2# show vpc
		Legend:
		                (*) - local vPC is down, forwarding via vPC peer-link

		vPC domain id                     : 1   
		Peer status                       : peer adjacency formed ok      
		vPC keep-alive status             : peer is alive                 
		Configuration consistency status  : success 
		Per-vlan consistency status       : success                       
		Type-2 consistency status         : success 
		vPC role                          : primary                       
		Number of vPCs configured         : 1   
		Peer Gateway                      : Enabled
		Dual-active excluded VLANs        : -
		Graceful Consistency Check        : Enabled
		Auto-recovery status              : Enabled, timer is off.(timeout = 240s)
		Delay-restore status              : Timer is off.(timeout = 30s)
		Delay-restore SVI status          : Timer is off.(timeout = 10s)
		Operational Layer3 Peer-router    : Disabled

		vPC peer-link status
		---------------------------------------------------------------------
		id    Port   Status Active vlans    
		--    ----   ------ -------------------------------------------------
		1     Po101  up     1,100-102,200-
							202,300-350
		         

		vPC status
		----------------------------------------------------------------------------
		Id    Port          Status Consistency Reason                Active vlans
		--    ------------  ------ ----------- ------                ---------------
		1     Po1           up     success     success               1,100-102,200-     
                                                             		202               		         


		Please check "show vpc consistency-parameters vpc <vpc-num>" for the 
		consistency reason of down vpc and for type-2 consistency reasons for 
		any vpc.
	'''
	}

	golden_parsed_output_2 = {
		'vpc_domain_id': 10,
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 1,
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel10',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1-100'
            }
        },
        'vpc': {
            20: {
            	'vpc_id': 20,
                'vpc_ifindex': 'Port-channel20',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1-100'
            }
        }
	}

	golden_output_2 = {'execute.return_value': '''
		R2# show vpc
		Legend:
		(*) - local vpc is down, forwarding via vPC peer-link
		 
		vPC domain id : 10
		Peer status : peer adjacency formed ok
		vPC keep-alive status : peer is alive
		Configuration consistency status: success
		vPC role : primary
		Number of vPC configured : 1
		 
		vPC peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po10 up 1-100
		 
		vPC status
		----------------------------------------------------------------------
		id Port Status Consistency Reason Active vlans
		-- ---- ------ ----------- -------------------------- ------------
		20 Po20 up success success 1-100
	'''
	}

	golden_parsed_output_3 = {
		'vpc_domain_id': 10,
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'failed',
        'vpc_configuration_consistency_reason': 'vPC type-1 configuration incompatible - STP interface port type inconsistent',
        'vpc_role': 'secondary',
        'num_of_vpcs': 1,
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel10',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1-100'
            }
        },
        'vpc': {
            20: {
            	'vpc_id': 20,
                'vpc_ifindex': 'Port-channel20',
                'vpc_port_state': 'up',
                'vpc_consistency': 'failed',
                'vpc_consistency_status': 'vPC type-1 configuration',
                'up_vlan_bitset': '-'
            }
        }
	}

	golden_output_3 = {'execute.return_value': '''
		Legend:
		(*) - local vpc is down, forwarding via vPC peer-link

		vPC domain id : 10
		Peer status : peer adjacency formed ok
		vPC keep-alive status : peer is alive
		Configuration consistency status: failed
		Configuration consistency reason: vPC type-1 configuration incompatible - STP interface port type inconsistent
		vPC role : secondary
		Number of vPC configured : 1

		vPC peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po10 up 1-100

		vPC status
		----------------------------------------------------------------------
		id Port Status Consistency Reason Active vlans
		-- ---- ------ ----------- -------------------------- ------------
		20 Po20 up failed vPC type-1 configuration -
		incompatible - STP
		interface port type
		inconsistent
	'''
	}

	golden_parsed_output_4 = {
		'vpc_domain_id': 1,
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_role': 'secondary',
        'num_of_vpcs': 3,
        'track_object': 12,
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel10',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1-100'
            }
        }
	}

	golden_output_4 = {'execute.return_value': '''
		Legend:
		(*) - local vpc is down, forwarding via vPC peer-link
		 
		vPC domain id : 1
		Peer status : peer adjacency formed ok
		vPC keep-alive status : peer is alive
		Configuration consistency status: success
		vPC role : secondary
		Number of vPC configured : 3
		Track object : 12
		 
		 
		vPC peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po10 up 1-100
	'''
	}

	golden_parsed_output_5 = {
		'vpc_domain_id': 100,
        'vpc_peer_status': 'peer link is down',
        'vpc_peer_keepalive_status': 'peer is alive, but domain IDs do not match',
        'vpc_configuration_consistency_status': 'success',
        'vpc_per_vlan_consistency_status': 'success',
        'vpc_type_2_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 1,
        'peer_gateway': 'Disabled',
        'dual_active_excluded_vlans': '-',
        'vpc_graceful_consistency_check_status': 'Enabled',
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel100',
                'peer_link_port_state': 'down',
                'peer_up_vlan_bitset': '-'
            }
        },
        'vpc': {
            1: {
            	'vpc_id': 1,
                'vpc_ifindex': 'Port-channel1',
                'vpc_port_state': 'down',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '-'
            }
        }
	}

	golden_output_5 = {'execute.return_value': '''
		Legend:
		(*) - local vPC is down, forwarding via vPC peer-link
		 
		vPC domain id : 100
		Peer status : peer link is down
		vPC keep-alive status : peer is alive, but domain IDs do not match
		Configuration consistency status: success
		Per-vlan consistency status : success
		Type-2 consistency status : success
		vPC role : primary
		Number of vPCs configured : 1
		Peer Gateway : Disabled
		Dual-active excluded VLANs : -
		Graceful Consistency Check : Enabled
		 
		vPC peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po100 down -
		 
		vPC status
		----------------------------------------------------------------------------
		id Port Status Consistency Reason Active vlans
		------ ----------- ------ ----------- -------------------------- -----------
		1 Po1 down success success -
	'''
	}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowVpc(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_2(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_2)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_2)

	def test_golden_3(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_3)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_3)

	def test_golden_4(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_4)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_4)

	def test_golden_5(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_5)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_5)

if __name__ == '__main__':
	unittest.main()