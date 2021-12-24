import setuptools
import pkg_resources

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("pyproject.toml", "r") as fh:
    pyproject = fh.read()

version = (
    [l.split(" = ")[1] for l in pyproject.split("\n") if "version = " in l][0]
    .replace('"', "")
    .replace("'", "")
)

setuptools.setup(
    name="blossom-wrapper",
    version=pkg_resources.get_distribution("blossom-wrapper").version,
    author="Grafeas Group",
    author_email="info@grafeas.org",
    description="Wrapper for the Blossom API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GrafeasGroup/blossom-wrapper",
    packages=setuptools.find_packages(),
    package_data={
        "blossom_wrapper": ["py.typed"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
