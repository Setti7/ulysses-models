from pathlib import Path

from setuptools import find_packages, setup

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name="ulysses-models",
    packages=find_packages(exclude=["tests"]),
    version="0.1.0",
    description="Library to manage the Ulysses models repository.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Setti7/ulysses-models",
    author="André Niero Setti",
    author_email="andre.niero.setti@usp.br",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["google-cloud-storage==2.1.0"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.0.0"],
    test_suite="tests",
)
