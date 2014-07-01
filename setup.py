# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from django_hashcash import __version__

REQUIREMENTS = [
    # 'django-cms>=3.0.3'
    # 'aldryn-country-segment>=0.1.0'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='django-hashcash',
    version=__version__,
    description='Adds HashCash.IO "proof-of-work" control to django login form.',
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    url='https://github.com/mkoistinen/django-hashcash',
    packages=find_packages(),
    package_data={
        "django_hashcash": [
            "templates/django_hashcash/*",
        ],
    },
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
