============
resumeschema
============

``resumeschema`` is a `json-schema <http://json-schema.org/>`_ validator for the `resume-schema <https://github.com/jsonresume/resume-schema>`_ spec.

``resumeschema`` is mostly just a wrapper around `jsonschema <https://github.com/Julian/jsonschema>`_.

Installation
------------

.. code-block:: bash

   $ [sudo] pip install resumeschema


API
---
validate(instance)
~~~~~~~~~~~~~~~~~~
Check if the provided ``instance`` is valid under the ``resume-schema`` spec.

Returns nothing.

Raises a ``jsonschema.ValidationError`` on error.

.. code:: python

   import resumeschema
   instance = {
       'basics': {
           'name': 'Resume Schema',
       },
   }
   resumeschema.validate(instance)


is_valid(instance)
~~~~~~~~~~~~~~~~~~
Check if the provided ``instance`` is valid under the ``resume-schema`` spec.

Returns ``True`` if valid ``False`` if not.

.. code:: python

   import resumeschema
   instance = {
       'basics': {
           'name': 'Resume Schema',
       },
   }
   if resumeschema.is_valid(instance):
       print 'It is valid!'


iter_errors(instance)
~~~~~~~~~~~~~~~~~~~~~
Get an iterator to iterate any ``jsonschema.ValidationErrors`` from the provided ``instance``.

Returns an iterator of ``jsonschema.ValidationErrors``.

.. code:: python

   import resumeschema
   invalid_instance = {
       'basics': {
           # `first_name` is not a supported field
           'first_name': 'Resume Schema',
       },
   }
   for error in resumeschema.iter_errors(invalid_instance):
       print error.message


validator
~~~~~~~~~
An instance of ``jsonschema.Draft4Validator`` to use as you so choose.


.. code:: python

   import resumeschema
   instance = {
       'basics': {
           'name': 'Resume Schema',
       },
   }
   resumeschema.validator.validate(instance)
