"""
"""
__all__ = ['is_valid', 'iter_errors', 'validate', 'validator']

import json
import os

from jsonschema import Draft4Validator

# Load in the schema from file
with open(os.path.join(os.path.dirname(__file__), 'schema.json')) as schema:
    SCHEMA = json.load(schema)

# Build our validator
validator = Draft4Validator(SCHEMA)


def is_valid(instance):
    """
    Check if the provided instance is valid against resume-schema

    :param object instance: The object to validate against ``resume-schema``
    :rtype: bool
    :return: Whether or not ``instance`` is valid
    """
    return validator.is_valid(instance)


def iter_errors(instance):
    """
    Get a validation error iterator for this ``instance```

    :param object instance: The object to validate against ``resume-schema``
    :return: An iterator of py:class:`jsonschema.ValidationError`
    """
    return validator.iter_errors(instance)


def validate(instance):
    """
    Validate ``instance` against ``resume-schema``

    :param object instance: The object to valdiate against ``resume-schema``
    :raises: py:class:`jsonschema.ValidationError`
    :rtype: None
    :return: ``None`` on success, raises an error if any were found
    """
    return validator.validate(instance)
