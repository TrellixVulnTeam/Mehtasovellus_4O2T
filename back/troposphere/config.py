# Copyright (c) 2015, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean


ONE_HOUR = "One_Hour"
THREE_HOURS = "Three_Hours"
SIX_HOURS = "Six_Hours"
TWELVE_HOURS = "Twelve_Hours"
TWENTYFOUR_HOURS = "TwentyFour_Hours"


class Scope(AWSProperty):
    props = {
        'ComplianceResourceId': (str, False),
        'ComplianceResourceTypes': ([str], False),
        'TagKey': (str, False),
        'TagValue': (str, False),
    }


class SourceDetails(AWSProperty):
    props = {
        'EventSource': (str, True),
        'MaximumExecutionFrequency': (str, False),
        'MessageType': (str, True),
    }

    def validate(self):
        valid_freqs = [
            ONE_HOUR,
            THREE_HOURS,
            SIX_HOURS,
            TWELVE_HOURS,
            TWENTYFOUR_HOURS,
        ]
        freq = self.properties.get('MaximumExecutionFrequency')
        if freq and freq not in valid_freqs:
            raise ValueError(
                "MaximumExecutionFrequency (given: %s) must be one of: %s" % (
                    freq, ', '.join(valid_freqs)))


class Source(AWSProperty):
    props = {
        'Owner': (str, True),
        'SourceDetails': ([SourceDetails], False),
        'SourceIdentifier': (str, True),
    }


class ConfigRule(AWSObject):
    resource_type = "AWS::Config::ConfigRule"

    props = {
        'ConfigRuleName': (str, False),
        'Description': (str, False),
        'InputParameters': (dict, False),
        'MaximumExecutionFrequency': (str, False),
        'Scope': (Scope, False),
        'Source': (Source, True),
    }


class AggregationAuthorization(AWSObject):
    resource_type = "AWS::Config::AggregationAuthorization"

    props = {
        'AuthorizedAccountId': (str, True),
        'AuthorizedAwsRegion': (str, True),
    }


class OrganizationAggregationSource(AWSProperty):
    props = {
        'AllAwsRegions': (boolean, False),
        'AwsRegions': ([str], False),
        'RoleArn': (str, True),
    }


class AccountAggregationSources(AWSProperty):
    props = {
        'AccountIds': ([str], True),
        'AllAwsRegions': (boolean, False),
        'AwsRegions': ([str], False),
    }


class ConfigurationAggregator(AWSObject):
    resource_type = "AWS::Config::ConfigurationAggregator"

    props = {
        'AccountAggregationSources': ([AccountAggregationSources], False),
        'ConfigurationAggregatorName': (str, True),
        'OrganizationAggregationSource':
            (OrganizationAggregationSource, False),
    }


class RecordingGroup(AWSProperty):
    props = {
        'AllSupported': (boolean, False),
        'IncludeGlobalResourceTypes': (boolean, False),
        'ResourceTypes': ([str], False),
    }


class ConfigurationRecorder(AWSObject):
    resource_type = "AWS::Config::ConfigurationRecorder"

    props = {
        'Name': (str, False),
        'RecordingGroup': (RecordingGroup, False),
        'RoleARN': (str, True),
    }


class ConfigSnapshotDeliveryProperties(AWSProperty):
    props = {
        'DeliveryFrequency': (str, False),
    }


class DeliveryChannel(AWSObject):
    resource_type = "AWS::Config::DeliveryChannel"

    props = {
        'ConfigSnapshotDeliveryProperties':
            (ConfigSnapshotDeliveryProperties, False),
        'Name': (str, False),
        'S3BucketName': (str, True),
        'S3KeyPrefix': (str, False),
        'SnsTopicARN': (str, False),
    }
