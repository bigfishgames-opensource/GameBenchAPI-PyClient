import setuptools

setuptools.setup(
    name='GameBenchAPI-PyClient-BigFish',
    version='0.1.0',
    description='A GameBench API Library Client.',
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
        'requests-mock>=1.5.2',
        'pandas>=0.24.2',
        'coverage>=4.5.3',
        'urllib3>=1.24.2,<1.25',
    ]
)


