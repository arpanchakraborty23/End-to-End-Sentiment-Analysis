import os
from pathlib import Path
import logging

list_of_files=[
    '.github/workflow',
    'expariment/expariment.ipynb',
    'setup.py',
    'templates/index.html',
    'src/components/__init__.py',
    'src/pipline/__init__.py',
    'src/constant/traning_pipline/__init__.py',
    'src/entity/__init__.py',
    'src/entity/artifacts_entity.py',
    'src/entity/config_entity.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/logging/__init__.py',
    'src/__init__.py',
    'Dockerfile',
    'app.py',
    'requirements.txt',
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating :{filedir} and file:{filename}')
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass