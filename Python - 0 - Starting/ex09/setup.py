from setuptools import setup, find_packages

"""
This script configures the installation details of the
ft_package using setuptools.

Explanation of setup() arguments:

- name: The name of the package. This is how it will be
    referred to when installed or listed via pip.
- version: The current version of the package.
    Used for version tracking and updates.
- description: A short summary of what the package does.
- author: The name of the person or organization who
    created the package.
- author_email: Contact email address of the author.
- url: A link to the homepage or source code repository
    of the package.
- license: The license under which the package
    is distributed (e.g., MIT, GPL).
- packages: A list of all Python import packages that
    should be included. `find_packages()` automatically discovers them.
- classifiers: A list of standard metadata that helps tools and
    users understand the package better (e.g., supported
    Python versions, license type).
"""


setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="Eagle",
    author_email="eagle@42.fr",
    url="https://github.com/eagle/ft_package",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
