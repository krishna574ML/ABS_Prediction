from setuptools import setup , find_packages


def get_requirements(file_path:str) ->list[str]:
    
    requriments=[]
    hypen_e_dot = '-e .'
    with open(file_path) as file_obj:
        requriments = file_obj.readlines()
        requriments = [i.replace('\n' , "" )for i in requriments] # type: ignore

        if hypen_e_dot in requriments:
            requriments.remove(hypen_e_dot)
    return requriments

setup(
    name='ABS_ml_project',
    version='1.0.0',
    author='Krishna',
    author_email='saik36048@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    ) 
