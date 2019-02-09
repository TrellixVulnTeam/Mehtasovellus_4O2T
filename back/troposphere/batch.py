from . import AWSObject, AWSProperty
from .validators import exactly_one, integer, positive_integer


class LaunchTemplateSpecification(AWSProperty):
    props = {
        "LaunchTemplateId": (str, False),
        "LaunchTemplateName": (str, False),
        "Version": (str, False),
    }

    def validate(self):
        template_ids = [
            'LaunchTemplateId',
            'LaunchTemplateName'
        ]
        exactly_one(self.__class__.__name__, self.properties, template_ids)


class ComputeResources(AWSProperty):

    props = {
        "SpotIamFleetRole": (str, False),
        "MaxvCpus": (positive_integer, True),
        "SecurityGroupIds": ([str], True),
        "BidPercentage": (positive_integer, False),
        "Type": (str, True),
        "Subnets": ([str], True),
        "MinvCpus": (positive_integer, True),
        "LaunchTemplate": (LaunchTemplateSpecification, False),
        "ImageId": (str, False),
        "InstanceRole": (str, True),
        "InstanceTypes": ([str], True),
        "Ec2KeyPair": (str, False),
        "PlacementGroup": (str, False),
        "Tags": (dict, False),
        "DesiredvCpus": (positive_integer, False)
    }


class MountPoints(AWSProperty):

    props = {
        "ReadOnly": (bool, False),
        "SourceVolume": (str, False),
        "ContainerPath": (str, False)
    }


class VolumesHost(AWSProperty):

    props = {
        "SourcePath": (str, False)
    }


class Volumes(AWSProperty):

    props = {
        "Host": (VolumesHost, False),
        "Name": (str, False)
    }


class Environment(AWSProperty):

    props = {
        "Value": (str, False),
        "Name": (str, False)
    }


class Ulimit(AWSProperty):

    props = {
        "SoftLimit": (positive_integer, True),
        "HardLimit": (positive_integer, True),
        "Name": (str, True)
    }


class ContainerProperties(AWSProperty):

    props = {
        "MountPoints": ([MountPoints], False),
        "User": (str, False),
        "Volumes": ([Volumes], False),
        "Command": ([str], False),
        "Memory": (positive_integer, True),
        "Privileged": (bool, False),
        "Environment": ([Environment], False),
        "JobRoleArn": (str, False),
        "ReadonlyRootFilesystem": (bool, False),
        "Ulimits": ([Ulimit], False),
        "Vcpus": (positive_integer, True),
        "Image": (str, True)
    }


class RetryStrategy(AWSProperty):

    props = {
        "Attempts": (positive_integer, False)
    }


class Timeout(AWSProperty):
    props = {
        'AttemptDurationSeconds': (integer, False),
    }


class JobDefinition(AWSObject):
    resource_type = "AWS::Batch::JobDefinition"

    props = {
        'ContainerProperties': (ContainerProperties, True),
        'JobDefinitionName': (str, False),
        'Parameters': (dict, True),
        'RetryStrategy': (RetryStrategy, False),
        'Timeout': (Timeout, False),
        'Type': (str, True),
    }


def validate_environment_state(environment_state):
    """ Validate response type
    :param environment_state: State of the environment
    :return: The provided value if valid
    """
    valid_states = [
        "ENABLED",
        "DISABLED"
    ]
    if environment_state not in valid_states:
        raise ValueError(
            "{} is not a valid environment state".format(environment_state)
        )
    return environment_state


class ComputeEnvironment(AWSObject):
    resource_type = "AWS::Batch::ComputeEnvironment"

    props = {
        "Type": (str, True),
        "ServiceRole": (str, True),
        "ComputeEnvironmentName": (str, False),
        "ComputeResources": (ComputeResources, True),
        "State": (validate_environment_state, False)
    }


class ComputeEnvironmentOrder(AWSProperty):

    props = {
        "ComputeEnvironment": (str, True),
        "Order": (positive_integer, True)
    }


def validate_queue_state(queue_state):
    """ Validate response type
    :param queue_state: State of the queue
    :return: The provided value if valid
    """
    valid_states = [
        "ENABLED",
        "DISABLED"
    ]
    if queue_state not in valid_states:
        raise ValueError(
            "{} is not a valid queue state".format(queue_state)
        )
    return queue_state


class JobQueue(AWSObject):
    resource_type = "AWS::Batch::JobQueue"

    props = {
        "ComputeEnvironmentOrder": ([ComputeEnvironmentOrder], True),
        "Priority": (positive_integer, True),
        "State": (validate_queue_state, False),
        "JobQueueName": (str, False)
    }
