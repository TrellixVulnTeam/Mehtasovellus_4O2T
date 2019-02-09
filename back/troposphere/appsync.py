# Copyright (c) 2012-2017, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSObject, AWSProperty
from .validators import boolean, integer


def resolver_kind_validator(x):
    valid_types = ["UNIT", "PIPELINE"]
    if x not in valid_types:
        raise ValueError("Kind must be one of: %s" % ", ".join(valid_types))
    return x


class ApiKey(AWSObject):
    resource_type = "AWS::AppSync::ApiKey"

    props = {
        'ApiId': (str, True),
        'Description': (str, False),
        'Expires': (integer, False),
    }


class DynamoDBConfig(AWSProperty):
    props = {
        'AwsRegion': (str, True),
        'TableName': (str, True),
        'UseCallerCredentials': (boolean, False),
    }


class ElasticsearchConfig(AWSProperty):
    props = {
        'AwsRegion': (str, True),
        'Endpoint': (str, True),
    }


class AwsIamConfig(AWSProperty):
    props = {
        'SigningRegion': (str, False),
        'SigningServiceName': (str, False),
    }


class AuthorizationConfig(AWSProperty):
    props = {
        'AuthorizationType': (str, True),
        'AwsIamConfig': (AwsIamConfig, False),
    }


class HttpConfig(AWSProperty):
    props = {
        'AuthorizationConfig': (AuthorizationConfig, False),
        'Endpoint': (str, True),
    }


class LambdaConfig(AWSProperty):
    props = {
        'LambdaFunctionArn': (str, True),
    }


class RdsHttpEndpointConfig(AWSProperty):
    props = {
        'AwsRegion': (str, False),
        'DbClusterIdentifier': (str, False),
        'DatabaseName': (str, False),
        'Schema': (str, False),
        'AwsSecretStoreArn': (str, False),
    }


class RelationalDatabaseConfig(AWSProperty):
    props = {
        'RelationalDatasourceType': (str, False),
        'RdsHttpEndpointConfig': (RdsHttpEndpointConfig, False),
    }


class DataSource(AWSObject):
    resource_type = "AWS::AppSync::DataSource"

    props = {
        'ApiId': (str, True),
        'Description': (str, False),
        'DynamoDBConfig': (DynamoDBConfig, False),
        'ElasticsearchConfig': (ElasticsearchConfig, False),
        'HttpConfig': (HttpConfig, False),
        'LambdaConfig': (LambdaConfig, False),
        'Name': (str, True),
        'ServiceRoleArn': (str, False),
        'Type': (str, True),
        'RelationalDatabaseConfig': (RelationalDatabaseConfig, False),
    }


class LogConfig(AWSProperty):
    props = {
        'CloudWatchLogsRoleArn': (str, False),
        'FieldLogLevel': (str, False),
    }


class OpenIDConnectConfig(AWSProperty):
    props = {
        'AuthTTL': (float, False),
        'ClientId': (str, False),
        'IatTTL': (float, False),
        'Issuer': (str, True),
    }


class UserPoolConfig(AWSProperty):
    props = {
        'AppIdClientRegex': (str, False),
        'AwsRegion': (str, False),
        'DefaultAction': (str, False),
        'UserPoolId': (str, False),
    }


class GraphQLApi(AWSObject):
    resource_type = "AWS::AppSync::GraphQLApi"

    props = {
        'AuthenticationType': (str, True),
        'LogConfig': (LogConfig, False),
        'Name': (str, True),
        'OpenIDConnectConfig': (OpenIDConnectConfig, False),
        'UserPoolConfig': (UserPoolConfig, False),
    }


class GraphQLSchema(AWSObject):
    resource_type = "AWS::AppSync::GraphQLSchema"

    props = {
        'ApiId': (str, True),
        'Definition': (str, False),
        'DefinitionS3Location': (str, False),
    }


class PipelineConfig(AWSProperty):
    props = {
        'Functions': ([str], False),
    }


class Resolver(AWSObject):
    resource_type = "AWS::AppSync::Resolver"

    props = {
        'ApiId': (str, True),
        'DataSourceName': (str, False),
        'FieldName': (str, True),
        'Kind': (resolver_kind_validator, False),
        'PipelineConfig': (PipelineConfig, False),
        'RequestMappingTemplate': (str, False),
        'RequestMappingTemplateS3Location': (str, False),
        'ResponseMappingTemplate': (str, False),
        'ResponseMappingTemplateS3Location': (str, False),
        'TypeName': (str, True),
    }


class FunctionConfiguration(AWSObject):
    resource_type = "AWS::AppSync::FunctionConfiguration"

    props = {
        'ApiId': (str, True),
        'Name': (str, False),
        'Description': (str, False),
        'DataSourceName': (str, False),
        'FunctionVersion': (str, False),
        'RequestMappingTemplate': (str, False),
        'RequestMappingTemplateS3Location': (str, False),
        'ResponseMappingTemplate': (str, False),
        'ResponseMappingTemplateS3Location': (str, False),
    }
