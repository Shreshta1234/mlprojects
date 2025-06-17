from setuptools import setup, find_packages
from typing import List

# Optional: If you want to filter out any unwanted lines in requirements
HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the requirements.txt file
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlprojects",                # Name of the package
    version="0.0.1",                  # Initial version
    author="Shreshta",                # Your name (GitHub name doesn't matter)
    author_email="nshreshta2006@gmail.com",  # Your email
    packages=find_packages(),         # Automatically discover packages in the project
    install_requires=get_requirements("requirements.txt")  # Install dependencies
)