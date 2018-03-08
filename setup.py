from setuptools import setup

setup(
    name='nameko-twilio',
    version='0.1',
    url='https://github.com/invictuscapital/nameko-twilio/',
    license='Apache License, Version 2.0',
    author='raybotha',
    author_email='rabotha42@gmail.com',
    py_modules=['nameko_twilio'],
    install_requires=[
        "nameko>=2.0.0",
        "twilio",
    ],
    description='Twilio dependency for nameko services',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
