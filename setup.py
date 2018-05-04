from setuptools import setup

setup(
    name="backblaze",
    version='0.1.0',
    packages=['backblaze'],
    install_requires=[
        'masonite>=1.6.0,<=1.6.99',
        'requests>=2.18.0,<=2.18.99',
    ],
    include_package_data=True,
)
