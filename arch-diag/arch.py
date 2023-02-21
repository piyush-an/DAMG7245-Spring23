from diagrams import Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Class Labs", show=False, direction="TB"):
    # Define Nodes
    node1 = ELB("lb") 
    node2 = [EC2("worker1"), EC2("worker2")]
    node3 = RDS("events")

    ## Define edges
    node1 >> Edge(color="green", style="bold") >> node2
    node2 >> Edge(color="black", style="bold") >> node3

