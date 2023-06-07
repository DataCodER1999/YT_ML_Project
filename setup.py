from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(filepath:str) ->List[str]:
    """
    This function will return list of all the requirements
    """
    requirements = []
    
    with open(filepath,'r') as f:
        
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    
    name="ML_Project",
    version="0.0.1",
    author="Krishna",
    author_email="malhotranitin771@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)