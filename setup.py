from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
#NEWS = open(os.path.join(here, 'NEWS.txt')).read()
NEWS = ""


version = '0.0.1'

install_requires = [
    'requests'
]


setup(name='gpueater',
    version=version,
    description="GPUEater API console for python.",
    long_description=README + '\n\n' + NEWS,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='gpu gpueater deeplearning eater cloud',
    author='Pegara, Inc.',
    author_email='info@pegara.com',
    url='https://www.gpueater.com',
    license='MIT',
    packages=find_packages('gpueater'),
    package_dir = {'': 'gpueater'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['gpueater=gpueater:main']
    }
)
