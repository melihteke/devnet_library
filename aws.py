import boto3
import environment

class VPCManager:

    """
    A class for managing VPC instances in Amazon Web Services (AWS).

    Attributes:
        region_name (str): The name of the AWS region where the VPC instance will be created.
        aws_access_key_id (str): The AWS access key ID used to authenticate the API requests.
        aws_secret_access_key (str): The AWS secret access key used to authenticate the API requests.
        vpc (boto3.client): The VPC client used to interact with the AWS API for VPC operations.
    """

    region_name = environment.AWS_REGION_NAME
    aws_access_key_id = environment.AWS_ACCESS_KEY_ID
    aws_secret_access_key = environment.AWS_SECRET_ACCESS_KEY


    def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):

        """
        Initializes a new instance of the VPCManager class.

        Args:
            region_name (str): The name of the AWS region where the VPC instance will be created.
            aws_access_key_id (str): The AWS access key ID used to authenticate the API requests.
            aws_secret_access_key (str): The AWS secret access key used to authenticate the API requests.
        """

        self.region_name = region_name
        self.vpc = boto3.client('vpc', region_name=region_name,
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key)

    def create_vpc(self, cidr_block):
        response = self.vpc.create_vpc(CidrBlock=cidr_block)
        vpc_id = response['Vpc']['VpcId']
        return vpc_id

    def create_subnet(self, vpc_id, cidr_block):
        response = self.vpc.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block)
        subnet_id = response['Subnet']['SubnetId']
        return subnet_id

    def create_internet_gateway(self):
        response = self.vpc.create_internet_gateway()
        internet_gateway_id = response['InternetGateway']['InternetGatewayId']
        return internet_gateway_id

    def attach_internet_gateway(self, vpc_id, internet_gateway_id):
        self.vpc.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=internet_gateway_id)

    def create_route_table(self, vpc_id):
        response = self.vpc.create_route_table(VpcId=vpc_id)
        route_table_id = response['RouteTable']['RouteTableId']
        return route_table_id

    def create_route(self, route_table_id, destination_cidr_block, gateway_id):
        self.vpc.create_route(RouteTableId=route_table_id, DestinationCidrBlock=destination_cidr_block,
                              GatewayId=gateway_id)

    def associate_subnet_with_route_table(self, subnet_id, route_table_id):
        self.vpc.associate_route_table(SubnetId=subnet_id, RouteTableId=route_table_id)

    def create_security_group(self, vpc_id, group_name, description):
        response = self.vpc.create_security_group(GroupName=group_name, Description=description, VpcId=vpc_id)
        group_id = response['GroupId']
        return group_id

    def authorize_security_group_ingress(self, group_id, ip_protocol, from_port, to_port, cidr_ip):
        self.vpc.authorize_security_group_ingress(GroupId=group_id, IpProtocol=ip_protocol, FromPort=from_port,
                                                  ToPort=to_port, CidrIp=cidr_ip)


'''
# import the VPCManager class
from aws import VPCManager

# create an instance of the VPCManager class
region_name = 'us-west-2'  # replace with your desired region
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
vpc_manager = VPCManager(region_name, aws_access_key_id, aws_secret_access_key)

# create a new VPC instance
cidr_block = '10.0.0.0/16'  # replace with your desired CIDR block
vpc_id = vpc_manager.create_vpc(cidr_block)

# create a new subnet
subnet_cidr_block = '10.0.1.0/24'  # replace with your desired subnet CIDR block
subnet_id = vpc_manager.create_subnet(vpc_id, subnet_cidr_block)

# create a new internet gateway
internet_gateway_id = vpc_manager.create_internet_gateway()

# attach the internet gateway to the VPC
vpc_manager.attach_internet_gateway(vpc_id, internet_gateway_id)

# create a new route table
route_table_id = vpc_manager.create_route_table(vpc_id)

# create a new route in the route table
destination_cidr_block = '0.0.0.0/0'
vpc_manager.create_route(route_table_id, destination_cidr_block, internet_gateway_id)

# associate the subnet with the route table
vpc_manager.associate_subnet_with_route_table(subnet_id, route_table_id)

# create a new security group
security_group_name = 'my-security-group'  # replace with your desired security group name
security_group_description = 'My security group description'  # replace with your desired security group description
security_group_id = vpc_manager.create_security_group(vpc_id, security_group_name, security_group_description)

# authorize inbound traffic to the security group
ip_protocol = 'tcp'
from_port = 22  # SSH port
to_port = 22  # SSH port
cidr_ip = '0.0.0.0/0'  # allow access from any IP address
vpc_manager.authorize_security_group_ingress(security_group_id, ip_protocol, from_port, to_port, cidr_ip)

'''