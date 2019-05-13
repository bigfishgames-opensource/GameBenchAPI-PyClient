import setuptools

with open("README.md", "r") as file_handle:
    long_description = file_handle.read()

setuptools.setup(
    name='GameBenchAPI-PyClient-BigFish',
    version='0.1.15',
    packages=setuptools.find_packages(),
    description='A GameBench API Client Library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bigfishgames/GameBenchAPI-PyClient',
    author='Big Fish Games, Inc.',
    author_email='',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas~=0.24.2',
        'urllib3>=1.24.2,<1.25',
        'requests~=2.21.0',
    ]
)


