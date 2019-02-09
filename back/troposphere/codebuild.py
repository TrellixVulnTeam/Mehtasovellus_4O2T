# Copyright (c) 2016, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from . import AWSHelperFn, AWSObject, AWSProperty, Tags
from .validators import boolean, integer, positive_integer


VALID_IMAGE_PULL_CREDENTIALS = ('CODEBUILD', 'SERVICE_ROLE')
VALID_CREDENTIAL_PROVIDERS = ('SECRETS_MANAGER')


def validate_image_pull_credentials(image_pull_credentials):
    """Validate ImagePullCredentialsType for Project"""

    if image_pull_credentials not in VALID_IMAGE_PULL_CREDENTIALS:
        raise ValueError("Project ImagePullCredentialsType must be one of: %s" %  # NOQA
                         ", ".join(VALID_IMAGE_PULL_CREDENTIALS))
    return image_pull_credentials


def validate_credentials_provider(credential_provider):
    """Validate CredentialProvider for Project's RegistryCredential"""

    if credential_provider not in VALID_CREDENTIAL_PROVIDERS:
        raise ValueError("RegistryCredential CredentialProvider must be one of: %s" %  # NOQA
                         ", ".join(VALID_CREDENTIAL_PROVIDERS))
    return credential_provider


class SourceAuth(AWSProperty):
    props = {
        'Resource': (str, False),
        'Type': (str, True),
    }

    def validate(self):
        valid_types = [
            'OAUTH'
        ]
        auth_types = self.properties.get('Type')
        if auth_types not in valid_types:
            raise ValueError('SourceAuth Type: must be one of %s' %
                             ','.join(valid_types))


class Artifacts(AWSProperty):
    props = {
        'ArtifactIdentifier': (str, False),
        'EncryptionDisabled': (boolean, False),
        'Location': (str, False),
        'Name': (str, False),
        'NamespaceType': (str, False),
        'OverrideArtifactName': (boolean, False),
        'Packaging': (str, False),
        'Path': (str, False),
        'Type': (str, True),
    }

    def validate(self):
        valid_types = [
            'CODEPIPELINE',
            'NO_ARTIFACTS',
            'S3',
        ]
        artifact_type = self.properties.get('Type')
        if artifact_type not in valid_types:
            raise ValueError('Artifacts Type: must be one of %s' %
                             ','.join(valid_types))

        if artifact_type == 'S3':
            for required_property in ['Name', 'Location']:
                if not self.properties.get(required_property):
                    raise ValueError(
                        'Artifacts Type S3: requires %s to be set' %
                        required_property
                    )


class EnvironmentVariable(AWSProperty):
    props = {
        'Name': (str, True),
        'Type': (str, False),
        'Value': (str, True),
    }

    def validate(self):
        if 'Type' in self.properties:
            valid_types = [
                'PARAMETER_STORE',
                'PLAINTEXT',
            ]
            env_type = self.properties.get('Type')
            if env_type not in valid_types:
                raise ValueError(
                    'EnvironmentVariable Type: must be one of %s' %
                    ','.join(valid_types))


class RegistryCredential(AWSProperty):
    props = {
        'Credential': (str, True),
        'CredentialProvider': (validate_credentials_provider, True),
    }


class Environment(AWSProperty):
    props = {
        'Certificate': (str, False),
        'ComputeType': (str, True),
        'EnvironmentVariables': ((list, [EnvironmentVariable]), False),
        'Image': (str, True),
        'ImagePullCredentialsType': (validate_image_pull_credentials, False),
        'PrivilegedMode': (boolean, False),
        'RegistryCredential': (RegistryCredential, False),
        'Type': (str, True),
    }

    def validate(self):
        valid_types = [
            'LINUX_CONTAINER',
            'WINDOWS_CONTAINER',
        ]
        env_type = self.properties.get('Type')
        if env_type not in valid_types:
            raise ValueError('Environment Type: must be one of %s' %
                             ','.join(valid_types))


class ProjectCache(AWSProperty):
    props = {
        'Location': (str, False),
        'Type': (str, True),
    }

    def validate(self):
        valid_types = [
            'NO_CACHE',
            'S3',
        ]
        cache_type = self.properties.get('Type')
        if cache_type not in valid_types:
            raise ValueError('ProjectCache Type: must be one of %s' %
                             ','.join(valid_types))


class Source(AWSProperty):
    props = {
        'Auth': (SourceAuth, False),
        'BuildSpec': (str, False),
        'GitCloneDepth': (positive_integer, False),
        'InsecureSsl': (boolean, False),
        'Location': (str, False),
        'ReportBuildStatus': (boolean, False),
        'SourceIdentifier': (str, False),
        'Type': (str, True),
    }

    def validate(self):
        valid_types = [
            'BITBUCKET',
            'CODECOMMIT',
            'CODEPIPELINE',
            'GITHUB',
            'GITHUB_ENTERPRISE',
            'NO_SOURCE',
            'S3',
        ]

        location_agnostic_types = [
            'CODEPIPELINE',
            'NO_SOURCE',
        ]

        source_type = self.properties.get('Type')

        # Don't do additional checks if source_type can't
        # be determined (for example, being a Ref).
        if isinstance(source_type, AWSHelperFn):
            return

        if source_type not in valid_types:
            raise ValueError('Source Type: must be one of %s' %
                             ','.join(valid_types))

        location = self.properties.get('Location')

        if source_type not in location_agnostic_types and not location:
            raise ValueError(
                'Source Location: must be defined when type is %s' %
                source_type
                )

        auth = self.properties.get('Auth')
        if auth is not None and source_type != 'GITHUB':
            raise ValueError("SourceAuth: must only be defined when using "
                             "'GITHUB' Source Type.")


class VpcConfig(AWSProperty):
    props = {
        'SecurityGroupIds': ([str], True),
        'Subnets': ([str], True),
        'VpcId': (str, True),
    }


class ProjectTriggers(AWSProperty):
    props = {
        'Webhook': (boolean, False),
    }


def validate_status(status):
    """ Validate status
    :param status: The Status of CloudWatchLogs or S3Logs
    :return: The provided value if valid
    """
    valid_statuses = [
        'ENABLED',
        'DISABLED'
    ]

    if status not in valid_statuses:
        raise ValueError('Status: must be one of %s' %
                         ','.join(valid_statuses))
    return status


class CloudWatchLogs(AWSProperty):
    props = {
        "Status": (validate_status, True),
        "GroupName": (str, False),
        "StreamName": (str, False)
    }


class S3Logs(AWSProperty):
    props = {
        "Status": (validate_status, True),
        "Location": (str, False)
    }


class LogsConfig(AWSProperty):
    props = {
        'CloudWatchLogs': (CloudWatchLogs, False),
        'S3Logs': (S3Logs, False)
    }


class Project(AWSObject):
    resource_type = "AWS::CodeBuild::Project"

    props = {
        'Artifacts': (Artifacts, True),
        'BadgeEnabled': (boolean, False),
        'Cache': (ProjectCache, False),
        'Description': (str, False),
        'EncryptionKey': (str, False),
        'Environment': (Environment, True),
        "LogsConfig": (LogsConfig, False),
        'Name': (str, True),
        'SecondaryArtifacts': ([Artifacts], False),
        'SecondarySources': ([Source], False),
        'ServiceRole': (str, True),
        'Source': (Source, True),
        'Tags': (Tags, False),
        'TimeoutInMinutes': (integer, False),
        'Triggers': (ProjectTriggers, False),
        'VpcConfig': (VpcConfig, False),
    }
