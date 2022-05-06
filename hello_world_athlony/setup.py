from setuptools import setup

setup(
    name='hello_world_athlony',
    version='1.0.0',
    description='Hello world for testing',
    author='Anton Yemets',
    author_email='athlony@gmail.com',
    license='MIT',
    #packages=find_namespace_packages(),
    #install_requires=['markdown'],
    entry_points={'console_scripts': ['greeting=hello_world_athlony.main:greeting']}
)
