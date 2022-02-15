from importlib.metadata import entry_points
from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Fernando Muñoz',
    author_email='fernandrewm@gmail.com',
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_type='text/markdown',
    url='https://github.com/Fernandrewm/cli-pgbackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requieres=['boto3'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ],
    }
)
