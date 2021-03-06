import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blossom-wrapper",
    version="0.0.1",
    author="Grafeas Group",
    author_email="info@grafeas.org",
    description="Wrapper for the Blossom API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GrafeasGroup/blossom-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)