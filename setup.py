from setuptools import setup, find_packages

setup(
    name="easy-flagger",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Doneeel",
    author_email="doneeel08@gmail.com",
    description="A simple package for a flag parsing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Doneeel/easy-flagger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)