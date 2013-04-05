from setuptools import setup

setup(name='validate_email',
      version = '2.0',
      download_url = 'git@github.com:openpolis/validate_email.git',
      py_modules = ('validate_email',),
      author = 'OpenPolis',
      author_email = 'info@openpolis.it',
      description = 'Validate_email verify if an email address is valid and really exists.',
      long_description=open('README.rst').read(),
      keywords = 'email validation verification mx verify',
      url = 'http://github.com/openpolis/validate_email',
      license = 'LGPL',
    )