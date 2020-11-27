from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="python-collection",
    url="https://github.com/Scientific-Guy/python-collection",
    version="1.0.0",
    description="A simple utility structure for python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=['collection'],
    keywords="collection",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
)
