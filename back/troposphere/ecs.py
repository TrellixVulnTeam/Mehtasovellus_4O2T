from . import AWSObject, AWSProperty
from .validators import boolean, integer, network_port, positive_integer


LAUNCH_TYPE_EC2 = 'EC2'
LAUNCH_TYPE_FARGATE = 'FARGATE'

SCHEDULING_STRATEGY_REPLICA = 'REPLICA'
SCHEDULING_STRATEGY_DAEMON = 'DAEMON'


class Cluster(AWSObject):
    resource_type = "AWS::ECS::Cluster"

    props = {
        'ClusterName': (str, False),
    }


class LoadBalancer(AWSProperty):
    props = {
        'ContainerName': (str, False),
        'ContainerPort': (network_port, True),
        'LoadBalancerName': (str, False),
        'TargetGroupArn': (str, False),
    }


class DeploymentConfiguration(AWSProperty):
    props = {
        'MaximumPercent': (positive_integer, False),
        'MinimumHealthyPercent': (positive_integer, False),
    }


def placement_strategy_validator(x):
    valid_values = ['random', 'spread', 'binpack']
    if x not in valid_values:
        raise ValueError("Placement Strategy type must be one of: %s" %
                         ', '.join(valid_values))
    return x


def placement_constraint_validator(x):
    valid_values = ['distinctInstance', 'memberOf']
    if x not in valid_values:
        raise ValueError("Placement Constraint type must be one of: %s" %
                         ', '.join(valid_values))
    return x


def scope_validator(x):
    valid_values = ['shared', 'task']
    if x not in valid_values:
        raise ValueError("Scope type must be one of: %s" %
                         ', '.join(valid_values))
    return x


class PlacementConstraint(AWSProperty):
    props = {
        'Type': (placement_constraint_validator, True),
        'Expression': (str, False),
    }


class PlacementStrategy(AWSProperty):
    props = {
        'Type': (placement_strategy_validator, True),
        'Field': (str, False),
    }


class AwsvpcConfiguration(AWSProperty):
    props = {
        'AssignPublicIp': (str, False),
        'SecurityGroups': (list, False),
        'Subnets': (list, True),
    }


class NetworkConfiguration(AWSProperty):
    props = {
        'AwsvpcConfiguration': (AwsvpcConfiguration, False),
    }


def launch_type_validator(x):
    valid_values = [LAUNCH_TYPE_EC2, LAUNCH_TYPE_FARGATE]
    if x not in valid_values:
        raise ValueError("Launch Type must be one of: %s" %
                         ', '.join(valid_values))
    return x


class ServiceRegistry(AWSProperty):
    props = {
        'ContainerName': (str, False),
        'ContainerPort': (integer, False),
        'Port': (integer, False),
        'RegistryArn': (str, False),
    }


class Service(AWSObject):
    resource_type = "AWS::ECS::Service"

    props = {
        'Cluster': (str, False),
        'DeploymentConfiguration': (DeploymentConfiguration, False),
        'DesiredCount': (positive_integer, False),
        'HealthCheckGracePeriodSeconds': (positive_integer, False),
        'LaunchType': (launch_type_validator, False),
        'LoadBalancers': ([LoadBalancer], False),
        'NetworkConfiguration': (NetworkConfiguration, False),
        'Role': (str, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'PlacementStrategies': ([PlacementStrategy], False),
        'PlatformVersion': (str, False),
        'SchedulingStrategy': (str, False),
        'ServiceName': (str, False),
        'ServiceRegistries': ([ServiceRegistry], False),
        'TaskDefinition': (str, True),
    }


class Environment(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, True),
    }


class MountPoint(AWSProperty):
    props = {
        'ContainerPath': (str, True),
        'SourceVolume': (str, True),
        'ReadOnly': (boolean, False),
    }


class PortMapping(AWSProperty):
    props = {
        'ContainerPort': (network_port, True),
        'HostPort': (network_port, False),
        'Protocol': (str, False),
    }


class VolumesFrom(AWSProperty):
    props = {
        'SourceContainer': (str, True),
        'ReadOnly': (boolean, False),
    }


class HostEntry(AWSProperty):
    props = {
        'Hostname': (str, True),
        'IpAddress': (str, True),
    }


class Device(AWSProperty):
    props = {
        'ContainerPath': (str, False),
        'HostPath': (str, False),
        'Permissions': ([str], False),
    }


class HealthCheck(AWSProperty):
    props = {
        'Command': ([str], True),
        'Interval': (integer, False),
        'Retries': (integer, False),
        'StartPeriod': (integer, False),
        'Timeout': (integer, False),
    }


class KernelCapabilities(AWSProperty):
    props = {
        'Add': ([str], False),
        'Drop': ([str], False),
    }


class LinuxParameters(AWSProperty):
    props = {
        'Capabilities': (KernelCapabilities, False),
        'Devices': ([Device], False),
        'InitProcessEnabled': (boolean, False),
    }


class LogConfiguration(AWSProperty):
    props = {
        'LogDriver': (str, True),
        'Options': (dict, False),
    }


class RepositoryCredentials(AWSProperty):
    props = {
        'CredentialsParameter': (str, False)
    }


class Ulimit(AWSProperty):
    props = {
        'HardLimit': (integer, True),
        'Name': (str, False),
        'SoftLimit': (integer, True),
    }


class ContainerDefinition(AWSProperty):
    props = {
        'Command': ([str], False),
        'Cpu': (positive_integer, False),
        'DisableNetworking': (boolean, False),
        'DnsSearchDomains': ([str], False),
        'DnsServers': ([str], False),
        'DockerLabels': (dict, False),
        'DockerSecurityOptions': ([str], False),
        'EntryPoint': ([str], False),
        'Environment': ([Environment], False),
        'Essential': (boolean, False),
        'ExtraHosts': ([HostEntry], False),
        'HealthCheck': (HealthCheck, False),
        'Hostname': (str, False),
        'Image': (str, True),
        'Links': ([str], False),
        'LinuxParameters': (LinuxParameters, False),
        'LogConfiguration': (LogConfiguration, False),
        'Memory': (positive_integer, False),
        'MemoryReservation': (positive_integer, False),
        'MountPoints': ([MountPoint], False),
        'Name': (str, True),
        'PortMappings': ([PortMapping], False),
        'Privileged': (boolean, False),
        'ReadonlyRootFilesystem': (boolean, False),
        'RepositoryCredentials': (RepositoryCredentials, False),
        'Ulimits': ([Ulimit], False),
        'User': (str, False),
        'VolumesFrom': ([VolumesFrom], False),
        'WorkingDirectory': (str, False),
    }


class Host(AWSProperty):
    props = {
        'SourcePath': (str, False),
    }


class DockerVolumeConfiguration(AWSProperty):
    props = {
        'Autoprovision': (boolean, False),
        'Driver': (str, False),
        'DriverOpts': (dict, False),
        'Labels': (dict, False),
        'Scope': (scope_validator, False)
    }


class Volume(AWSProperty):
    props = {
        'DockerVolumeConfiguration': (DockerVolumeConfiguration, False),
        'Name': (str, True),
        'Host': (Host, False),
    }


class TaskDefinition(AWSObject):
    resource_type = "AWS::ECS::TaskDefinition"

    props = {
        'ContainerDefinitions': ([ContainerDefinition], True),
        'Cpu': (str, False),
        'ExecutionRoleArn': (str, False),
        'Family': (str, False),
        'Memory': (str, False),
        'NetworkMode': (str, False),
        'PlacementConstraints': ([PlacementConstraint], False),
        'RequiresCompatibilities': ([str], False),
        'TaskRoleArn': (str, False),
        'Volumes': ([Volume], False),
    }
