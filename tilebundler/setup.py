from setuptools import setup
import os

install_requires = [
        'django-tilebundler==0.1-alpha1',
        'django-tastypie==0.12.1'
]

setup(
    name='tilebundler_prj',
    version='0.1',
    author='',
    author_email='',
    description='',
    classifiers=[
    ],
    license='MIT',
    keywords='',
    url='https://github.com/ROGUE-JCTD/',
    install_requires=install_requires,
    extras_require={
    },
    zip_safe=False,
)
