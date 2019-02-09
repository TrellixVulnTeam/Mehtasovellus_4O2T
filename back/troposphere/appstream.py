# Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class ServiceAccountCredentials(AWSProperty):
    props = {
        'AccountName': (str, True),
        'AccountPassword': (str, True),
    }


class DirectoryConfig(AWSObject):
    resource_type = "AWS::AppStream::DirectoryConfig"

    props = {
        'DirectoryName': (str, True),
        'OrganizationalUnitDistinguishedNames': ([str], True),
        'ServiceAccountCredentials': (ServiceAccountCredentials, True),
    }


class ComputeCapacity(AWSProperty):
    props = {
        'DesiredInstances': (integer, True),
    }


class VpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([str], False),
        'SubnetIds': ([str], False),
    }


class DomainJoinInfo(AWSProperty):
    props = {
        'DirectoryName': (str, False),
        'OrganizationalUnitDistinguishedName': (str, False),
    }


class Fleet(AWSObject):
    resource_type = "AWS::AppStream::Fleet"

    props = {
        'ComputeCapacity': (ComputeCapacity, True),
        'Description': (str, False),
        'DisconnectTimeoutInSeconds': (integer, False),
        'DisplayName': (str, False),
        'DomainJoinInfo': (DomainJoinInfo, False),
        'EnableDefaultInternetAccess': (boolean, False),
        'FleetType': (str, False),
        'ImageArn': (str, False),
        'ImageName': (str, False),
        'InstanceType': (str, True),
        'MaxUserDurationInSeconds': (integer, False),
        'Name': (str, False),
        'VpcConfig': (VpcConfig, False),
    }


class ImageBuilder(AWSObject):
    resource_type = "AWS::AppStream::ImageBuilder"

    props = {
        'AppstreamAgentVersion': (str, False),
        'Description': (str, False),
        'DisplayName': (str, False),
        'DomainJoinInfo': (DomainJoinInfo, False),
        'EnableDefaultInternetAccess': (boolean, False),
        'ImageArn': (str, False),
        'ImageName': (str, False),
        'InstanceType': (str, True),
        'Name': (str, False),
        'VpcConfig': (VpcConfig, False),
    }


class StackFleetAssociation(AWSObject):
    resource_type = "AWS::AppStream::StackFleetAssociation"

    props = {
        'FleetName': (str, True),
        'StackName': (str, True),
    }


class StorageConnector(AWSProperty):
    props = {
        'ConnectorType': (str, True),
        'Domains': ([str], False),
        'ResourceIdentifier': (str, False),
    }


class UserSetting(AWSProperty):
    props = {
        'Action': (str, True),
        'Permission': (str, True),
    }


class ApplicationSettings(AWSProperty):
    props = {
        'Enabled': (boolean, True),
        'SettingsGroup': (str, False),
    }


class Stack(AWSObject):
    resource_type = "AWS::AppStream::Stack"

    props = {
        'ApplicationSettings': (ApplicationSettings, False),
        'AttributesToDelete': ([str], False),
        'DeleteStorageConnectors': (boolean, False),
        'Description': (str, False),
        'DisplayName': (str, False),
        'FeedbackURL': (str, False),
        'Name': (str, False),
        'RedirectURL': (str, False),
        'StorageConnectors': ([StorageConnector], False),
        'UserSettings': ([UserSetting], False),
    }


class StackUserAssociation(AWSObject):
    resource_type = "AWS::AppStream::StackUserAssociation"

    props = {
        'AuthenticationType': (str, True),
        'SendEmailNotification': (boolean, False),
        'StackName': (str, True),
        'UserName': (str, True),
    }


class User(AWSObject):
    resource_type = "AWS::AppStream::User"

    props = {
        'AuthenticationType': (str, True),
        'FirstName': (str, False),
        'LastName': (str, False),
        'MessageAction': (str, False),
        'UserName': (str, True),
    }
