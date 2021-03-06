#################### Maintained by Hatch ####################
# This file is auto-generated by hatch. If you'd like to customize this file
# please add your changes near the bottom marked for 'USER OVERRIDES'.
# EVERYTHING ELSE WILL BE OVERWRITTEN by hatch.
#############################################################
from io import open

from setuptools import find_packages, setup

with open('mailprep/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

kwargs = {
    'name': 'mailprep',
    'version': version,
    'description': 'mailprep converts vCard data into physical labels from SVG templates',
    'long_description': readme,
    'long_description_content_type': 'text/markdown',
    'author': 'NE Automation',
    'author_email': 'code@neautomation.com',
    'maintainer': 'NE Automation',
    'maintainer_email': 'code@neautomation.com',
    'url': 'https://git.sr.ht/~lucidone/mailprep',
    'license': 'MIT/Apache-2.0',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    'install_requires': REQUIRES,
    'tests_require': ['coverage', 'pytest', 'delegator.py'],
    'packages': find_packages(),
    'entry_points': {
        'console_scripts': [
            'mailprep = mailprep.cli:mailprep',
        ],
    },

}

#################### BEGIN USER OVERRIDES ####################
# Add your customizations in this section.
kwargs['include_package_data']=True
kwargs['eager_resources']=['mailprep/template.svg']
kwargs['setup_requires']=['pytest-runner']

###################### END USER OVERRIDES ####################

setup(**kwargs)
