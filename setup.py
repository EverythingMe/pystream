from setuptools import setup, find_packages

setup(
    name='pystream',
    version='0.1',
    description='Stream uploads/downloads to/from S3 easily with smart_open',
    author='EverythingMe',
    author_email='omrib@everything.me',
    url='http://github.com/EverythingMe/pystream',
    packages=find_packages(),
    install_requires=['smart_open', 'click'],

    entry_points={
        'console_scripts': [
            'pystream = pystream.main:main'
        ]
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Clustering',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities'
    ]
)

