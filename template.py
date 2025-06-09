import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/models/__init.py",
    "src/models/recommender.py",
    "src/train/trainer.py",
    "src/evaluate/evaluate.py",
    "src/predict/infer.py",
    "src/utils/logger.py",
    "artifacts/models",
    "artifacts/logs",
    "artifacts/mlflow",
    "tests/test_data.py",
    "tests/test_model.py",
    "tests/test_train.py",
    ".env",
    "dvc.yaml",
    "setup.py",
    "research/trials.ipynb",
    "research/research.txt"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory; {filedir} for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating")

    else:
        logging.info(f"{filename} already exists")
