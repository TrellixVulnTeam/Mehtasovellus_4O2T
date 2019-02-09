# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, json_checker, double
try:
    from awacs.aws import Policy
    policytypes = (dict, Policy)
except ImportError:
    policytypes = dict,


class RetentionPeriod(AWSProperty):
    props = {
        'NumberOfDays': (integer, False),
        'Unlimited': (boolean, False),
    }


class Channel(AWSObject):
    resource_type = "AWS::IoTAnalytics::Channel"

    props = {
        'ChannelName': (str, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }


class AddAttributes(AWSProperty):
    props = {
        'Attributes': (json_checker, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class ActivityChannel(AWSProperty):
    props = {
        'ChannelName': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Datastore(AWSProperty):
    props = {
        'DatastoreName': (str, False),
        'Name': (str, False),
    }


class DeviceRegistryEnrich(AWSProperty):
    props = {
        'Attribute': (str, False),
        'Name': (str, False),
        'Next': (str, False),
        'RoleArn': (str, False),
        'ThingName': (str, False),
    }


class DeviceShadowEnrich(AWSProperty):
    props = {
        'Attribute': (str, False),
        'Name': (str, False),
        'Next': (str, False),
        'RoleArn': (str, False),
        'ThingName': (str, False),
    }


class Filter(AWSProperty):
    props = {
        'Filter': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Lambda(AWSProperty):
    props = {
        'BatchSize': (integer, False),
        'LambdaName': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Math(AWSProperty):
    props = {
        'Attribute': (str, False),
        'Math': (str, False),
        'Name': (str, False),
        'Next': (str, False),
    }


class RemoveAttributes(AWSProperty):
    props = {
        'Attributes': ([str], False),
        'Name': (str, False),
        'Next': (str, False),
    }


class SelectAttributes(AWSProperty):
    props = {
        'Attributes': ([str], False),
        'Name': (str, False),
        'Next': (str, False),
    }


class Activity(AWSProperty):
    props = {
        'AddAttributes': (AddAttributes, False),
        'Channel': (ActivityChannel, False),
        'Datastore': (Datastore, False),
        'DeviceRegistryEnrich': (DeviceRegistryEnrich, False),
        'DeviceShadowEnrich': (DeviceShadowEnrich, False),
        'Filter': (Filter, False),
        'Lambda': (Lambda, False),
        'Math': (Math, False),
        'RemoveAttributes': (RemoveAttributes, False),
        'SelectAttributes': (SelectAttributes, False),
    }


class Pipeline(AWSObject):
    resource_type = "AWS::IoTAnalytics::Pipeline"

    props = {
        'PipelineActivities': ([Activity], True),
        'PipelineName': (str, False),
        'Tags': ((Tags, list), False),
    }


class RetentionPeriod(AWSProperty):
    props = {
        'NumberOfDays': (integer, False),
        'Unlimited': (boolean, False),
    }


class Datastore(AWSObject):
    resource_type = "AWS::IoTAnalytics::Datastore"

    props = {
        'DatastoreName': (str, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
    }


class ResourceConfiguration(AWSProperty):
    props = {
        'ComputeType': (str, True),
        'VolumeSizeInGB': (integer, True),
    }


class DatasetContentVersionValue(AWSProperty):
    props = {
        'DatasetName': (str, False),
    }


class OutputFileUriValue(AWSProperty):
    props = {
        'FileName': (str, False),
    }


class Variable(AWSProperty):
    props = {
        'DatasetContentVersionValue': (DatasetContentVersionValue, False),
        'DoubleValue': (double, False),
        'OutputFileUriValue': (OutputFileUriValue, False),
        'StringValue': (str, False),
        'VariableName': (str, False)
    }


class ContainerAction(AWSProperty):
    props = {
        'ExecutionRoleArn': (str, True),
        'Image': (str, True),
        'ResourceConfiguration': (ResourceConfiguration, False),
        'Variables': ([Variable], False),
    }


class DeltaTime(AWSProperty):
    props = {
        'TimeExpression': (str, True),
        'OffsetSeconds': (integer, True),
    }


class QueryActionFilter(AWSProperty):
    props = {
        'DeltaTime': (DeltaTime, False),
    }


class QueryAction(AWSProperty):
    props = {
        'Filters': ([QueryActionFilter], False),
        'SqlQuery': (str, False),
    }


class Action(AWSProperty):
    props = {
        'ActionName': (str, True),
        'ContainerAction': (ContainerAction, False),
        'QueryAction': (QueryAction, False)
    }


class Schedule(AWSProperty):
    props = {
        'ScheduleExpression': (str, True),
    }


class TriggeringDataset(AWSProperty):
    props = {
        'DatasetName': (str, True),
    }


class Trigger(AWSProperty):
    props = {
        'Schedule': (Schedule, False),
        'TriggeringDataset': (TriggeringDataset, False),
    }


class Dataset(AWSObject):
    resource_type = "AWS::IoTAnalytics::Dataset"

    props = {
        'Actions': ([Action], True),
        'DatasetName': (str, False),
        'RetentionPeriod': (RetentionPeriod, False),
        'Tags': ((Tags, list), False),
        'Triggers': ([Trigger], False),
    }
