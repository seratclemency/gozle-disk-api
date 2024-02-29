from setuptools import setup, find_packages

setup(
    name='gozle_disk_api',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium',
        'seleniumbase',
        'fake-useragent'
    ],
    author='seratclemency',
    description='Gozle disk api is an unofficial api for the gozle disk service which provides the ability to log into your account, see the amount of space on your account and get account data. There is a function to update outdated cookies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seratclemency/gozle-disk-api/',
    license='MIT',
    keywords='gozle disk api',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
)
