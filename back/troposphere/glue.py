# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, double, integer_range, positive_integer


class GrokClassifier(AWSProperty):
    props = {
        'Classification': (str, True),
        'CustomPatterns': (str, False),
        'GrokPattern': (str, True),
        'Name': (str, False),
    }


class JsonClassifier(AWSProperty):
    props = {
        'JsonPath': (str, True),
        'Name': (str, False),
    }


class XMLClassifier(AWSProperty):
    props = {
        'Classification': (str, True),
        'Name': (str, False),
        'RowTag': (str, True),
    }


class Classifier(AWSObject):
    resource_type = "AWS::Glue::Classifier"

    props = {
        'GrokClassifier': (GrokClassifier, False),
        'JsonClassifier': (JsonClassifier, False),
        'XMLClassifier': (XMLClassifier, False),
    }


class PhysicalConnectionRequirements(AWSProperty):
    props = {
        'AvailabilityZone': (str, True),
        'SecurityGroupIdList': ([str], True),
        'SubnetId': (str, True),
    }


def connection_type_validator(type):
    valid_types = [
        'JDBC',
        'SFTP',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for ConnectionType' % type)
    return type


class ConnectionInput(AWSProperty):
    props = {
        'ConnectionProperties': (dict, True),
        'ConnectionType': (connection_type_validator, True),
        'Description': (str, False),
        'MatchCriteria': ([str], True),
        'Name': (str, False),
        'PhysicalConnectionRequirements':
            (PhysicalConnectionRequirements, True),
    }


class Connection(AWSObject):
    resource_type = "AWS::Glue::Connection"

    props = {
        'CatalogId': (str, True),
        'ConnectionInput': (ConnectionInput, True),
    }


class Schedule(AWSProperty):
    props = {
        'ScheduleExpression': (str, False),
    }


def delete_behavior_validator(value):
    valid_values = [
        'LOG',
        'DELETE_FROM_DATABASE',
        'DEPRECATE_IN_DATABASE',
    ]
    if value not in valid_values:
        raise ValueError('% is not a valid value for DeleteBehavior' % value)
    return value


def update_behavior_validator(value):
    valid_values = [
        'LOG',
        'UPDATE_IN_DATABASE',
    ]
    if value not in valid_values:
        raise ValueError('% is not a valid value for UpdateBehavior' % value)
    return value


class SchemaChangePolicy(AWSProperty):
    props = {
        'DeleteBehavior': (delete_behavior_validator, False),
        'UpdateBehavior': (update_behavior_validator, False),
    }


class JdbcTarget(AWSProperty):
    props = {
        'ConnectionName': (str, False),
        'Exclusions': ([str], False),
        'Path': (str, False),
    }


class S3Target(AWSProperty):
    props = {
        'Exclusions': ([str], False),
        'Path': (str, False),
    }


class Targets(AWSProperty):
    props = {
        'JdbcTargets': ([JdbcTarget], False),
        'S3Targets': ([S3Target], False),
    }


class Crawler(AWSObject):
    resource_type = "AWS::Glue::Crawler"

    props = {
        'Classifiers': ([str], False),
        'Configuration': (str, False),
        'DatabaseName': (str, True),
        'Description': (str, False),
        'Name': (str, False),
        'Role': (str, True),
        'Schedule': (Schedule, False),
        'SchemaChangePolicy': (SchemaChangePolicy, False),
        'TablePrefix': (str, False),
        'Targets': (Targets, True),
    }


class DatabaseInput(AWSProperty):
    props = {
        'Description': (str, False),
        'LocationUri': (str, False),
        'Name': (str, False),
        'Parameters': (dict, False),
    }


class Database(AWSObject):
    resource_type = "AWS::Glue::Database"

    props = {
        'CatalogId': (str, True),
        'DatabaseInput': (DatabaseInput, True),
    }


class DevEndpoint(AWSObject):
    resource_type = "AWS::Glue::DevEndpoint"

    props = {
        'EndpointName': (str, False),
        'ExtraJarsS3Path': (str, False),
        'ExtraPythonLibsS3Path': (str, False),
        'NumberOfNodes': (positive_integer, False),
        'PublicKey': (str, True),
        'RoleArn': (str, True),
        'SecurityGroupIds': ([str], False),
        'SubnetId': (str, False),
    }


class ConnectionsList(AWSProperty):
    props = {
        'Connections': ([str], False),
    }


class ExecutionProperty(AWSProperty):
    props = {
        'MaxConcurrentRuns': (positive_integer, False),
    }


class JobCommand(AWSProperty):
    props = {
        'Name': (str, False),
        'ScriptLocation': (str, False),
    }


class Job(AWSObject):
    resource_type = "AWS::Glue::Job"

    props = {
        'AllocatedCapacity': (double, False),
        'Command': (JobCommand, True),
        'Connections': (ConnectionsList, False),
        'DefaultArguments': (dict, False),
        'Description': (str, False),
        'ExecutionProperty': (ExecutionProperty, False),
        'LogUri': (str, False),
        'MaxRetries': (double, False),
        'Name': (str, False),
        'Role': (str, True),
    }


class Column(AWSProperty):
    props = {
        'Comment': (str, False),
        'Name': (str, True),
        'Type': (str, False),
    }


class Order(AWSProperty):
    props = {
        'Column': (str, True),
        'SortOrder': (integer_range(0, 1), False),
    }


class SerdeInfo(AWSProperty):
    props = {
        'Name': (str, False),
        'Parameters': (dict, False),
        'SerializationLibrary': (str, False),
    }


class SkewedInfo(AWSProperty):
    props = {
        'SkewedColumnNames': ([str], False),
        'SkewedColumnValues': ([str], False),
        'SkewedColumnValueLocationMaps': (dict, False),
    }


class StorageDescriptor(AWSProperty):
    props = {
        'BucketColumns': ([str], False),
        'Columns': ([Column], False),
        'Compressed': (boolean, False),
        'InputFormat': (str, False),
        'Location': (str, False),
        'NumberofBuckets': (positive_integer, False),
        'OutputFormat': (str, False),
        'Parameters': (dict, False),
        'SerdeInfo': (SerdeInfo, False),
        'SkewedInfo': (SkewedInfo, False),
        'SortColumns': ([Order], False),
        'StoredAsSubDirectories': (boolean, False),
    }


class PartitionInput(AWSProperty):
    props = {
        'Parameters': (dict, False),
        'StorageDescriptor': (StorageDescriptor, False),
        'Values': ([str], True),
    }


class Partition(AWSObject):
    resource_type = "AWS::Glue::Partition"

    props = {
        'CatalogId': (str, True),
        'DatabaseName': (str, True),
        'PartitionInput': (PartitionInput, True),
        'TableName': (str, True),
    }


def table_type_validator(type):
    valid_types = [
        'EXTERNAL_TABLE',
        'VIRTUAL_VIEW',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for TableType' % type)
    return type


class TableInput(AWSProperty):
    props = {
        'Description': (str, False),
        'Name': (str, True),
        'Owner': (str, False),
        'Parameters': (dict, False),
        'PartitionKeys': ([Column], False),
        'Retention': (positive_integer, False),
        'StorageDescriptor': (StorageDescriptor, False),
        'TableType': (table_type_validator, False),
        'ViewExpandedText': (str, False),
        'ViewOriginalText': (str, False),
    }


class Table(AWSObject):
    resource_type = "AWS::Glue::Table"

    props = {
        'CatalogId': (str, True),
        'DatabaseName': (str, True),
        'TableInput': (TableInput, True),
    }


class Action(AWSProperty):
    props = {
        'Arguments': (dict, False),
        'JobName': (str, False),
    }


class Condition(AWSProperty):
    props = {
        'JobName': (str, False),
        'LogicalOperator': (str, False),
        'State': (str, False),
    }


class Predicate(AWSProperty):
    props = {
        'Conditions': ([Condition], False),
        'Logical': (str, False),
    }


def trigger_type_validator(type):
    valid_types = [
        'SCHEDULED',
        'CONDITIONAL',
        'ON_DEMAND',
    ]
    if type not in valid_types:
        raise ValueError('% is not a valid value for Type' % type)
    return type


class Trigger(AWSObject):
    resource_type = "AWS::Glue::Trigger"

    props = {
        'Actions': ([Action], True),
        'Description': (str, False),
        'Name': (str, False),
        'Predicate': (Predicate, False),
        'Schedule': (str, False),
        'Type': (trigger_type_validator, True),
    }
