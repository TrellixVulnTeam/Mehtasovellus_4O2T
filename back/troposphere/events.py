# Copyright (c) 2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty


class EcsParameters(AWSProperty):
    props = {
        "TaskCount": (int, False),
        "TaskDefinitionArn": (str, True),
    }


class InputTransformer(AWSProperty):
    props = {
        'InputPathsMap': (dict, False),
        'InputTemplate': (str, True),
    }


class KinesisParameters(AWSProperty):
    props = {
        'PartitionKeyPath': (str, True),
    }


class RunCommandTarget(AWSProperty):
    props = {
        'Key': (str, True),
        'Values': ([str], True),
    }


class RunCommandParameters(AWSProperty):
    props = {
        'RunCommandTargets': ([RunCommandTarget], True),
    }


class SqsParameters(AWSProperty):
    props = {
        'MessageGroupId': (str, True),
    }


class Target(AWSProperty):
    props = {
        'Arn': (str, True),
        "EcsParameters": (EcsParameters, False),
        'Id': (str, True),
        'Input': (str, False),
        'InputPath': (str, False),
        'InputTransformer': (InputTransformer, False),
        'KinesisParameters': (KinesisParameters, False),
        'RoleArn': (str, False),
        'RunCommandParameters': (RunCommandParameters, False),
        'SqsParameters': (SqsParameters, False),
    }


class Rule(AWSObject):
    resource_type = "AWS::Events::Rule"

    props = {

        'Description': (str, False),
        'EventPattern': (dict, False),
        'Name': (str, False),
        'ScheduleExpression': (str, False),
        'State': (str, False),
        'Targets': ([Target], False),
    }
