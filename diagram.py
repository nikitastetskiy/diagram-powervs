from diagrams import Diagram, Cluster, Edge
from diagrams.ibm.network import VpnGateway, TransitGateway
from diagrams.ibm.compute import PowerInstance
from diagrams.ibm.network import Router
from diagrams.generic.place import Datacenter

# Create the diagram with adjusted global node attributes for size and spacing
with Diagram("PowerVS with a VPC and VPN Connection", show=False,
             node_attr={"fontsize": "10", "width": "1.2", "height": "1.2"},
             graph_attr={"nodesep": "1.0", "ranksep": "1.2"}):
    
    # Define the clusters and elements
    with Cluster("On-Premises Network"):
        with Cluster("On-Premises Datacenter"):
            on_prem_info = Datacenter("192.168.1.10\nIKE Policy:\nVersion: IKEv2 ...")
        router = Router("Edge Router")
        
    with Cluster("IBM Cloud - MAD02"):
        with Cluster("VPC"):
            vpn_gateway = VpnGateway("VPN Gateway")

        transit_gateway = TransitGateway("Transit Gateway")
        
        with Cluster("PowerVS Workspace"):
            powervs_instance = PowerInstance("PowerVS Instance\nIP: 10.0.1.5")

    # Define the connections
    on_prem_info >> Edge(label="IPSec Tunnel", fontsize="10") >> router >> vpn_gateway
    vpn_gateway >> Edge(label="VPC Routing", fontsize="10") >> transit_gateway >> powervs_instance

