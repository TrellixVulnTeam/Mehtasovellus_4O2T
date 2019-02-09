# Copyright (c) 2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, positive_integer


class CognitoIdentityProvider(AWSProperty):
    props = {
        'ClientId': (str, False),
        'ProviderName': (str, False),
        'ServerSideTokenCheck': (bool, False),
    }


class CognitoStreams(AWSProperty):
    props = {
        'RoleArn': (str, False),
        'StreamingStatus': (str, False),
        'StreamName': (str, False),
    }


class PushSync(AWSProperty):
    props = {
        'ApplicationArns': ([str], False),
        'RoleArn': (str, False),
    }


class IdentityPool(AWSObject):
    resource_type = "AWS::Cognito::IdentityPool"

    props = {
        'AllowUnauthenticatedIdentities': (bool, True),
        'CognitoEvents': (dict, False),
        'CognitoIdentityProviders': ([CognitoIdentityProvider], False),
        'CognitoStreams': (CognitoStreams, False),
        'DeveloperProviderName': (str, False),
        'IdentityPoolName': (str, False),
        'OpenIdConnectProviderARNs': ([str], False),
        'PushSync': (PushSync, False),
        'SamlProviderARNs': ([str], False),
        'SupportedLoginProviders': (dict, False),
    }


class MappingRule(AWSProperty):
    props = {
        'Claim': (str, True),
        'MatchType': (str, True),
        'RoleARN': (str, True),
        'Value': (str, True),
    }


class RulesConfiguration(AWSProperty):
    props = {
        'Rules': ([MappingRule], True),
    }


class RoleMapping(AWSProperty):
    props = {
        'AmbiguousRoleResolution': (str, False),
        'RulesConfiguration': (RulesConfiguration, False),
        'Type': (str, True),
    }


class IdentityPoolRoleAttachment(AWSObject):
    resource_type = "AWS::Cognito::IdentityPoolRoleAttachment"

    props = {
        'IdentityPoolId': (str, True),
        'RoleMappings': (dict, False),
        'Roles': (dict, False),
    }


class InviteMessageTemplate(AWSProperty):
    props = {
        'EmailMessage': (str, False),
        'EmailSubject': (str, False),
        'SMSMessage': (str, False),
    }


class AdminCreateUserConfig(AWSProperty):
    props = {
        'AllowAdminCreateUserOnly': (boolean, False),
        'InviteMessageTemplate': (InviteMessageTemplate, False),
        'UnusedAccountValidityDays': (positive_integer, False),
    }


class DeviceConfiguration(AWSProperty):
    props = {
        'ChallengeRequiredOnNewDevice': (boolean, False),
        'DeviceOnlyRememberedOnUserPrompt': (boolean, False),
    }


class EmailConfiguration(AWSProperty):
    props = {
        'ReplyToEmailAddress': (str, False),
        'SourceArn': (str, False),
    }


class LambdaConfig(AWSProperty):
    props = {
        'CreateAuthChallenge': (str, False),
        'CustomMessage': (str, False),
        'DefineAuthChallenge': (str, False),
        'PostAuthentication': (str, False),
        'PostConfirmation': (str, False),
        'PreAuthentication': (str, False),
        'PreSignUp': (str, False),
        'VerifyAuthChallengeResponse': (str, False),
    }


class PasswordPolicy(AWSProperty):
    props = {
        'MinimumLength': (positive_integer, False),
        'RequireLowercase': (boolean, False),
        'RequireNumbers': (boolean, False),
        'RequireSymbols': (boolean, False),
        'RequireUppercase': (boolean, False),
    }


class Policies(AWSProperty):
    props = {
        'PasswordPolicy': (PasswordPolicy, False),
    }


class NumberAttributeConstraints(AWSProperty):
    props = {
        'MaxValue': (str, False),
        'MinValue': (str, False),
    }


class StringAttributeConstraints(AWSProperty):
    props = {
        'MaxLength': (str, False),
        'MinLength': (str, False),
    }


class SchemaAttribute(AWSProperty):
    props = {
        'AttributeDataType': (str, False),
        'DeveloperOnlyAttribute': (boolean, False),
        'Mutable': (boolean, False),
        'Name': (str, False),
        'NumberAttributeConstraints': (NumberAttributeConstraints, False),
        'StringAttributeConstraints': (StringAttributeConstraints, False),
        'Required': (boolean, False),
    }


class SmsConfiguration(AWSProperty):
    props = {
        'ExternalId': (str, False),
        'SnsCallerArn': (str, True),
    }


class UserPool(AWSObject):
    resource_type = "AWS::Cognito::UserPool"

    props = {
        'AdminCreateUserConfig': (AdminCreateUserConfig, False),
        'AliasAttributes': ([str], False),
        'AutoVerifiedAttributes': ([str], False),
        'DeviceConfiguration': (DeviceConfiguration, False),
        'EmailConfiguration': (EmailConfiguration, False),
        'EmailVerificationMessage': (str, False),
        'EmailVerificationSubject': (str, False),
        'LambdaConfig': (LambdaConfig, False),
        'MfaConfiguration': (str, False),
        'Policies': (Policies, False),
        'UserPoolName': (str, True),
        'Schema': ([SchemaAttribute], False),
        'SmsAuthenticationMessage': (str, False),
        'SmsConfiguration': (SmsConfiguration, False),
        'SmsVerificationMessage': (str, False),
        'UsernameAttributes': ([str], False),
        'UserPoolTags': (dict, False),
    }


class UserPoolClient(AWSObject):
    resource_type = "AWS::Cognito::UserPoolClient"

    props = {
        'ClientName': (str, False),
        'ExplicitAuthFlows': ([str], False),
        'GenerateSecret': (boolean, False),
        'ReadAttributes': ([str], False),
        'RefreshTokenValidity': (positive_integer, False),
        'UserPoolId': (str, True),
        'WriteAttributes': ([str], False),
    }


class UserPoolGroup(AWSObject):
    resource_type = "AWS::Cognito::UserPoolGroup"

    props = {
        'Description': (str, False),
        'GroupName': (str, True),
        'Precedence': (positive_integer, False),
        'RoleArn': (str, False),
        'UserPoolId': (str, True),
    }


class AttributeType(AWSProperty):
    props = {
        'Name': (str, True),
        'Value': (str, False),
    }


class UserPoolUser(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUser"

    props = {
        'DesiredDeliveryMediums': ([str], False),
        'ForceAliasCreation': (boolean, False),
        'UserAttributes': ([AttributeType], False),
        'MessageAction': (str, False),
        'Username': (str, False),
        'UserPoolId': (str, True),
        'ValidationData': ([AttributeType], False),
    }


class UserPoolUserToGroupAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUserToGroupAttachment"

    props = {
        'GroupName': (str, True),
        'Username': (str, True),
        'UserPoolId': (str, True),
    }
