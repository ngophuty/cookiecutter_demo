import os
import shutil
from pathlib import Path

path = Path(os.getcwd())
parent_path = path.parent.absolute()

def remove_folder(folder):
    folder_path = os.path.join(parent_path, 
                            '{{cookiecutter.project_name}}', 
                            '{{cookiecutter.app_name}}', 
                            folder
                            )
    return shutil.rmtree(folder_path)

folders_databse = ['database', 'models']
folders_celery = ['celery']
folders_redis = ['redis']

cookiecutter_var = ['{{cookiecutter.database}}', '{{cookiecutter.celery}}', '{{cookiecutter.redis}}']


if cookiecutter_var[0] == 'no':
    for folder in folders_databse:
        remove_folder(folder)

if cookiecutter_var[1] == 'no':
    for folder in folders_celery:
        remove_folder(folder)

if cookiecutter_var[2] == 'no':
    for folder in folders_redis :
       remove_folder(folder)
