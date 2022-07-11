from setuptools import setup

with open(file='README.md', mode='r') as readme_handler:
    long_description = readme_handler.read()

setup(
    name='ocam',
    author='',
    version='0.0.1',
    description='OCAM Analyzer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ehsanzabardast/OCAM',
    py_modules=['ocam'],
    package_dir={'': 'ocam'},
    python_requires='>=3.7',
    install_requires=[
        'requests',
        'argparse'
    ],
    extras_require = {
        'dev': [
            'pytest>=3.7',
        ],
    },
)
