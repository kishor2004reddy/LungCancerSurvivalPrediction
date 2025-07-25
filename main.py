from PodcastListeningTimePrediction import logger
from PodcastListeningTimePrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from PodcastListeningTimePrediction.pipeline.data_validation_pipeline import DataValidationPipeline
from PodcastListeningTimePrediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from PodcastListeningTimePrediction.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from PodcastListeningTimePrediction.utils.common import read_yaml
from pathlib import Path

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<< : {e}")
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<< : {e}")
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    validation_report = read_yaml(Path("artifacts/data_validation/report.yaml"))
    if validation_report.data_validation_status == "false":
        raise Exception("Data validation failed. Cannot proceed with data transformation.")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataTransformationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<< : {e}")
    raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_train_pipeline = ModelTrainerPipeline()
    model_train_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<< : {e}")
    raise e