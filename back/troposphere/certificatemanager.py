from . import AWSObject, AWSProperty, Tags


class DomainValidationOption(AWSProperty):
    props = {
        'DomainName': (str, True),
        'ValidationDomain': (str, True),
    }


class Certificate(AWSObject):
    resource_type = "AWS::CertificateManager::Certificate"

    props = {
        'DomainName': (str, True),
        'DomainValidationOptions': ([DomainValidationOption], False),
        'SubjectAlternativeNames': ([str], False),
        'Tags': ((Tags, list), False),
        'ValidationMethod': (str, False),
    }
