from setuptools import setup, find_packages

setup(
    name='bmv',
    version='0.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
        'rich',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'bmv = bmv.__main__:entry',
        ],
    },
)