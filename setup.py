from setuptools import setup,find_packages

__version__="0.0.0.0"


setup(
    name="Resume_type",
    version=__version__,
    author_email="amandeepsingh.kaillay@gmail.com",
    author="Amandeep",
    packages=find_packages(where="src"),
    package_dir={"":"src"}
)