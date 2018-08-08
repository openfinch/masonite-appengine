from setuptools import setup

setup(
    name="appengine",
    version='0.0.1',
    packages=['appengine'],
    install_requires=[
        'masonite',
    ],
    include_package_data=True,
)
