from setuptools import setup, find_packages

setup(
    name='noisy_diabetes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'csv',
        'sklearn',
        # These libraries are currently all you need.
    ],
    author='Hiroyuki Akama',
    author_email='akamalab01@gmail.com',
    description='A modified verison of Scikit-learn diabete data with noise added to intentionally lower the accuracy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hilolani/noisy_diabetes',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
