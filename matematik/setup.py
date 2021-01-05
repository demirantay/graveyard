import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="matematik",
    version="1.2.1",
    author="Demir Antay",
    author_email="demir99antay@gmail.com",
    description="An package for solving math equations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/demirantay/matematik",
    packages=setuptools.find_packages()
)
