import json
import os
import unittest

import jsonschema

import resumeschema


class TestResumeSchema(unittest.TestCase):
    def setUp(self):
        """Preload in our fixture resumes needed for tests"""
        with open(os.path.join(os.path.dirname(__file__), 'valid_resume.json')) as schema:
            self.valid_resume = json.load(schema)

        with open(os.path.join(os.path.dirname(__file__), 'invalid_resume.json')) as schema:
            self.invalid_resume = json.load(schema)

    def test_validate_valid_resume(self):
        """
        When validating a valid resume
            No exception is raised
        """
        # DEV: `validate` will raise an exception if it could not validate
        self.assertIsNone(resumeschema.validate(self.valid_resume))

    def test_validate_invalid_resume(self):
        """
        When validating an invalid resume
            A `jsonschema.ValidationError` is raised
        """
        # DEV: `validate` will raise an exception if it could not validate
        with self.assertRaises(jsonschema.ValidationError):
            resumeschema.validate(self.invalid_resume)

    def test_is_valid_valid_resume(self):
        """
        When checking if a valid resume is valid
            is_valid responds with True
        """
        self.assertTrue(resumeschema.is_valid(self.valid_resume))

    def test_is_valid_invalid_resume(self):
        """
        When checking if an invalid resume is valid
            is_valid responds with False
        """
        self.assertFalse(resumeschema.is_valid(self.invalid_resume))

    def test_iter_errors_valid_resume(self):
        """
        When checking a valid resume for errors
            iter_errors responds with no errors
        """
        errors = list(resumeschema.iter_errors(self.valid_resume))
        self.assertEqual(len(errors), 0)

    def test_iter_errors_invalid_resume(self):
        """
        When checking an invalid resume for errors
            iter_errors responds with all errors from the resume
        """
        errors = list(resumeschema.iter_errors(self.invalid_resume))
        self.assertEqual(len(errors), 3)

        self.assertEqual(list(errors[0].path), ['basics'])
        self.assertEqual(
            errors[0].message, 'Additional properties are not allowed (u\'first_name\', u\'last_name\' were unexpected)'
        )

        self.assertEqual(list(errors[1].path), ['basics', 'profiles'])
        self.assertEqual(
            errors[1].message,
            '{u\'username\': u\'neutralthoughts\', u\'network\': u\'Facebook\'} is not of type u\'array\''
        )

        self.assertEqual(list(errors[2].path), ['work'])
        self.assertEqual(
            errors[2].message,
            ('{u\'website\': u\'http://piedpiper.com\', u\'startDate\': u\'2013-12-01\', u\'highlights\': '
             '[u\'Build an algorithm\'], u\'company\': u\'Pied Piper\', u\'summary\': '
             'u\'Pied Piper is a multi-platform technology.\', u\'position\': u\'CEO/President\'} '
             'is not of type u\'array\'')
        )
