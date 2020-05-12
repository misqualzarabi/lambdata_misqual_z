# Setup.py file


from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_lambdata_zarabi",  # the name that you will install via pip
    version="1.0",
    author="Misqual Zarabi",
    author_email="misqualzarabi234@yahoo.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    license="MIT",
    url="https://github.com/misqualzarabi/lambdata_misqual_z",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)
