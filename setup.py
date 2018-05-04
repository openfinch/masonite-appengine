from setuptools import setup

setup(
    name="masonite_backblaze",
    version='0.1.0',
    packages=['masonite_backblaze'],
    install_requires=[
        'masonite',
        'requests>=2.18.0,<=2.18.99',
    ],
    include_package_data=True,
)
