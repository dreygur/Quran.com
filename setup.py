from os import path
import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'dreygur <ryeasin03@gmail.com>'
__version__ = '1.0.0'

packages = [
    'quran'
]

with io.open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements_inside = f.readlines()

setup(
    name='quran',
    version=__version__,
    author='dreygur',
    author_email='ryeasin03@gmail.com',
    license='MIT',
    url='https://github.com/dreygur/Quran.com/tree/master',
    install_requires=requirements_inside,
    keywords='quran api',
    description='A python wrapper quran.com api.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=packages,
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.8',
    ]
)
