import proxmoxer
import urllib3
import environment

urllib3.disable_warnings()

class ProxmoxManager:

    def __init__(self, host=environment.PROXMOX_HOST, user=environment.PROXMOX_USER, password=environment.PROXMOX_PASSWORD):
        self.host = host
        self.user = user
        self.password = password
        self.client = proxmoxer.ProxmoxAPI(host, user=user, password=password, verify_ssl=False)
    
    def create_vm(self, vm_name, ova_file, node_name, memory=1024, cores=1):
        node = self.client.nodes(node_name)
        vm = node.qemu.create(
            name=vm_name,
            memory=memory,
            cores=cores,
            ide2=ova_file,
            boot='cdrom'
        )
        return vm
    
    def create_container(self, container_name, template_name, node_name, memory=512, cores=1):
        node = self.client.nodes(node_name)
        ct = node.lxc.create(
            vmid=120,
            ostemplate=template_name,
            hostname=container_name,
            memory=memory,
            cores=cores,
        )
        return ct
    
    def get_vm_ip_address(self, vm_id, node_name):
        node = self.client.nodes(node_name)
        vm = node.qemu.get(vmid=vm_id)
        if vm['status'] == 'running':
            for net, netinfo in vm['net'].items():
                if 'ip-address' in netinfo and netinfo['ip-address'] != '0.0.0.0':
                    return netinfo['ip-address']
        return None
    
    def create_bridge(self, bridge_name, node_name):
        node = self.client.nodes(node_name)
        bridge = node.network.create(bridge_name)
        return bridge
    
    def create_veth_pair(self, veth_name, peer_name, bridge_name, node_name):
        node = self.client.nodes(node_name)
        bridge = node.network.get(bridge_name)
        veth = node.network.create(
            'veth',
            iface=veth_name,
            peer=peer_name,
            bridge=bridge_name
        )
        return veth
    
    def get_interface_mac_address(self, iface_name, node_name):
        node = self.client.nodes(node_name)
        iface = node.network.interfaces.get(iface_name)
        return iface['mac']
    
    def get_all_mac_addresses(self, node_name):
        node = self.client.nodes(node_name)
        interfaces = node.network.interfaces.get()
        return {iface['name']: iface['mac'] for iface in interfaces}
    
    def create_vlans(self, vlan_id, bridge_name, node_name):
        node = self.client.nodes(node_name)
        bridge = node.network.get(bridge_name)
        vlan_iface = node.network.create(
            'vlan',
            vlan_id=vlan_id,
            iface=f'{bridge_name}.{vlan_id}',
            bridge=bridge_name
        )
        return vlan_iface
    
    def create_vxlan(self, vxlan_id, bridge_name, node_name, local_ip, remote_ip):
        node = self.client.nodes(node_name)
        bridge = node.network.get(bridge_name)
        vxlan = node.network.create(
            'vxlan',
            iface=f'vxlan{vxlan_id}',
            id=vxlan_id,
            local_ip=local_ip,
            remote_ip=remote_ip,
            bridge=bridge_name
        )
        return vxlan
    
    def create_ovs_bridge(self, bridge_name, node_name):
        node = self.client.nodes(node_name)
        bridge = node.network.create(
            'ovsbridge',
            bridge_name
        )
        return bridge
    
    def get_all_nodes(self):
        nodes = self.client.nodes.get()
        return nodes
