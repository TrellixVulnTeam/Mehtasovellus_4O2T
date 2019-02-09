# Copyright (c) 2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer, network_port, positive_integer


CDC = "cdc"
FULL_LOAD = "full-load"
FULL_LOAD_AND_CDC = "full-load-and-cdc"


class Certificate(AWSObject):
    resource_type = "AWS::DMS::Certificate"

    props = {
        'CertificateIdentifier': (str, False),
        'CertificatePem': (str, False),
        'CertificateWallet': (str, False),
    }


class DynamoDBSettings(AWSProperty):
    props = {
        'ServiceAccessRoleArn': (str, True),
    }


class MongoDbSettings(AWSProperty):
    props = {
        'AuthMechanism': (str, False),
        'AuthSource': (str, False),
        'DatabaseName': (str, False),
        'DocsToInvestigate': (str, False),
        'ExtractDocId': (str, False),
        'KmsKeyId': (str, False),
        'NestingLevel': (str, False),
        'Password': (str, False),
        'Port': (network_port, False),
        'ServerName': (str, False),
        'Username': (str, False),
    }


class S3Settings(AWSProperty):
    props = {
        'BucketFolder': (str, False),
        'BucketName': (str, False),
        'CompressionType': (str, False),
        'CsvDelimiter': (str, False),
        'CsvRowDelimiter': (str, False),
        'ExternalTableDefinition': (str, False),
        'ServiceAccessRoleArn': (str, False),
    }


class Endpoint(AWSObject):
    resource_type = "AWS::DMS::Endpoint"

    props = {
        'CertificateArn': (str, False),
        'DatabaseName': (str, False),
        'DynamoDbSettings': (DynamoDBSettings, False),
        'EndpointIdentifier': (str, False),
        'EndpointType': (str, True),
        'EngineName': (str, True),
        'ExtraConnectionAttributes': (str, False),
        'KmsKeyId': (str, False),
        'MongoDbSettings': (MongoDbSettings, False),
        'Password': (str, False),
        'Port': (network_port, False),
        'S3Settings': (S3Settings, False),
        'ServerName': (str, False),
        'SslMode': (str, False),
        'Tags': (Tags, False),
        'Username': (str, True),
    }


class EventSubscription(AWSObject):
    resource_type = "AWS::DMS::EventSubscription"

    props = {
        'Enabled': (boolean, False),
        'EventCategories': ([str], False),
        'SnsTopicArn': (str, True),
        'SourceIds': ([str], False),
        'SourceType': (str, False),
        'SubscriptionName': ([str], False),
        'Tags': (Tags, False),
    }


class ReplicationInstance(AWSObject):
    resource_type = "AWS::DMS::ReplicationInstance"

    props = {
        'AllocatedStorage': (integer, False),
        'AutoMinorVersionUpgrade': (boolean, False),
        'AvailabilityZone': (str, False),
        'EngineVersion': (str, False),
        'KmsKeyId': (str, False),
        'MultiAZ': (boolean, False),
        'PreferredMaintenanceWindow': (str, False),
        'PubliclyAccessible': (boolean, False),
        'ReplicationInstanceClass': (str, True),
        'ReplicationInstanceIdentifier': (str, False),
        'ReplicationSubnetGroupIdentifier': (str, False),
        'Tags': (Tags, False),
        'VpcSecurityGroupIds': ([str], False),
    }


class ReplicationSubnetGroup(AWSObject):
    resource_type = "AWS::DMS::ReplicationSubnetGroup"

    props = {
        'ReplicationSubnetGroupIdentifier': (str, False),
        'ReplicationSubnetGroupDescription': (str, True),
        'SubnetIds': ([str], True),
        'Tags': (Tags, False),
    }


class ReplicationTask(AWSObject):
    resource_type = "AWS::DMS::ReplicationTask"

    props = {
        'CdcStartTime': (positive_integer, False),
        'MigrationType': (str, True),
        'ReplicationInstanceArn': (str, True),
        'ReplicationTaskIdentifier': (str, False),
        'ReplicationTaskSettings': (str, False),
        'SourceEndpointArn': (str, True),
        'TableMappings': (str, True),
        'Tags': (Tags, False),
        'TargetEndpointArn': (str, True),
    }
