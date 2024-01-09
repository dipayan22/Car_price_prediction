import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO)

project_name="Second_Hand_Car_Price_Prediction"

list_of_files=[
    # ".github/workflows/gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",
    f"src/components/model_monitering.py",
    f"src/pipelines/__init__.py",
    f"src/pipelines/training_pipeline.py",
    f"src/pipelines/prediction_pipeline.py",
    f"src/exception.py",
    f"src/logger.py",
    f"src/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]


for file_path in list_of_files:
    filepath=Path(file_path)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exist")

