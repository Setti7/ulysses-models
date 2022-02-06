from setuptools import find_packages, setup

setup(
    name="ulysses-models",
    packages=find_packages(include=["ulysses_models"]),
    version="0.1.0",
    description="Library to manage the Ulysses models repository.",
    author="André Niero Setti <andre.niero.setti@usp.br>",
    license="MIT",
    install_requires=[
        "google-cloud-storage==2.1.0",
        "google-api-core==2.5.0",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.0.0"],
    test_suite="tests",
)
