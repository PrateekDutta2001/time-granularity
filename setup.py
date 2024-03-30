from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='time-granularity',
    version='1.2',
    packages=find_packages(),
    install_requires=[],  # Add dependencies if any
    author='Prateek Dutta',
    author_email='parteekdutta2001@email.com',
    description='A Python package for managing time granularity with options to re-execute at different intervals.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PrateekDutta2001/time-granularity',
)
