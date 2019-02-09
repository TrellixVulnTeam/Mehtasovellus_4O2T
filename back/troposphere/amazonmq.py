# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty, Tags
from .validators import boolean, integer


class ConfigurationId(AWSProperty):
    props = {
        'Id': (str, True),
        'Revision': (integer, True),
    }


class MaintenanceWindow(AWSProperty):
    props = {
        'DayOfWeek': (str, True),
        'TimeOfDay': (str, True),
        'TimeZone': (str, True),
    }


class User(AWSProperty):
    props = {
        'ConsoleAccess': (boolean, False),
        'Groups': ([str], False),
        'Password': (str, True),
        'Username': (str, True),
    }


class LogsConfiguration(AWSProperty):
    props = {
        'Audit': (boolean, False),
        'General': (boolean, False),
    }


class Broker(AWSObject):
    resource_type = "AWS::AmazonMQ::Broker"

    props = {
        'AutoMinorVersionUpgrade': (boolean, True),
        'BrokerName': (str, True),
        'Users': ([User], True),
        'Configuration': (ConfigurationId, False),
        'DeploymentMode': (str, True),
        'EngineType': (str, True),
        'EngineVersion': (str, True),
        'HostInstanceType': (str, True),
        'Logs': (LogsConfiguration, False),
        'MaintenanceWindowStartTime': (MaintenanceWindow, False),
        'PubliclyAccessible': (boolean, True),
        'SecurityGroups': ([str], False),
        'SubnetIds': ([str], False),
        'Tags': ((Tags, list), False),
    }


class Configuration(AWSObject):
    resource_type = "AWS::AmazonMQ::Configuration"

    props = {
        'Data': (str, True),
        'Description': (str, False),
        'EngineType': (str, True),
        'EngineVersion': (str, True),
        'Name': (str, True),
    }


class ConfigurationAssociation(AWSObject):
    resource_type = "AWS::AmazonMQ::ConfigurationAssociation"

    props = {
        'Broker': (str, True),
        'Configuration': (ConfigurationId, True),
    }
