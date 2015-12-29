#!/usr/bin/env python

import os
import setuptools

import patterndict


CLASSIFIERS = [
    # TBC
    # 'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries',
]


setuptools.setup(
    author='Piotr Kilczuk',
    author_email='piotr@tymaszweb.pl',
    name='patterndict',
    version='.'.join(str(v) for v in patterndict.VERSION),
    description='A well tested dict-like objects where keys are regexps or globs.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/centralniak/python-patterndict',
    license='MIT License',
    classifiers=CLASSIFIERS,
    tests_require=open('test_requirements.txt').read(),
    packages=['patterndict'],
    include_package_data=False,
    zip_safe=False,
    test_suite='nose.collector',
)
