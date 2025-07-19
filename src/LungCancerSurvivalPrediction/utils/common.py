import os
import yaml
import json
from ensure import ensure_annotations
from typing import Any
from LungCancerSurvivalPrediction import logger
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
import joblib


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path (Path): The path to the YAML file.

    Returns:
        ConfigBox: The content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error in YAML file {path}: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading YAML file {path}: {e}")
        raise e

@ensure_annotations
def create_directories(paths: list, verbose = True):
    """
    Creates directories if they do not exist.

    Args:
        paths (List[Path]): List of directory paths to create.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data)
    
    logger.info(f"json file saved at {path}")

@ensure_annotations
def save_bin(path: Path, data: Any) -> None:
    """save binary data

    Args:
        path (Path): path to binary file
        data (dict): data to be saved in binary file
    
    Returns:
        None: Ruturns nothing, just saves the data to the file
    """
    joblib.dump(value = data, filename = path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(filename = path)
    logger.info(f"binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
