import setuptools

setuptools.setup(
    name='gamebench_api_client_big_fish',
    version='0.0.1',
    description='A GameBench API Library Client.',
    url='https://github.com/bigfishgames/GameBenchAPI',
    author='Big Fish Games, Inc.',
    author_email='Placeholder for email.',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: 3-Clause BSD License",
        "Operating System :: OS Independent",
    ]
)

install_requires = [
    'python>=3.7',
    'requests-mock>=1.5.2',
    'pandas>=0.24.2',
    'coverage>=4.5.3',
]
