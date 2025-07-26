from setuptools import find_packages, setup

from typing import List
HYPEN_E_DOT='-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will give the list of requirements from the reauirement.txt
    Beacause when someone is installing our project then while installing it should install all the
    packages which is needed to run the project like numpy, pandas, matplotlib.pyplot ect

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

setup(

    name='mlproject',
    version='0.0.1',
    author='Harsh',
    author_email='harshnnarayankar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)