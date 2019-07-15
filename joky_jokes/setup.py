import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jokyjokes",
    version="0.0.4",
    author="Demir Antay",
    author_email="demir99antay@gmail.com",
    description="A package that provides you hundreds of terrbile jokes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/demirantay/jokes",
    packages=setuptools.find_packages(),
)
