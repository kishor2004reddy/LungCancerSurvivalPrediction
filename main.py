from LungCancerSurvivalPrediction import logger
from LungCancerSurvivalPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(f">>>>>> stage {STAGE_NAME} failed <<<<<< : {e}")
    raise e