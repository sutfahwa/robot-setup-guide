from setuptools import setup

setup(
    name='robotframework-automation',
    version='1.0.0',
    description='A package for installing Robot Framework and its libraries for creating automation scripts for mobile and web',
    author='sutthasinee.wa',
    author_email='sutthasinee.wa@gmail.com',
    install_requires=[
        'robotframework',
        'robotframework-seleniumlibrary',
        'robotframework-appiumlibrary',
        'selenium',
        'Appium-Python-Client',
        'robotframework-requests',
        'robotframework-selenium2library',
        'webdriver-manager',
    ],
    python_requires='>=3.6',  # Need Python Version 3.6 and above
)
