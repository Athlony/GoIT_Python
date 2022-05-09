from setuptools import setup,find_namespace_packages

setup(
    name='clean_folder',
    version='0.1.1',
    description='Homework7. Clean folder',
    author='Anton Yemets',
    author_email='athlony@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)
