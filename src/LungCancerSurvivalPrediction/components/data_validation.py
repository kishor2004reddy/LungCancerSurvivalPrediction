import pandas as pd
from LungCancerSurvivalPrediction.utils.common import write_yaml, read_yaml
from LungCancerSurvivalPrediction import logger
from LungCancerSurvivalPrediction.entity.config_entity import DataValidationConfig
from LungCancerSurvivalPrediction.constants import *

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        """
        Validates the data by checking for missing columns and incorrect data types.
        Returns True if validation passes, otherwise False.
        """
        
        try:
            schema = read_yaml(self.config.schema_file_path)
            schema_cols = schema.Columns

            df = pd.read_csv(self.config.unzip_data_path)
            columns = df.columns.tolist()
            missing_columns = [col for col in schema_cols if col not in columns]
            report = {"data_validation_status": None}

            if missing_columns:
                report["data_validation_status"] = False
                report["missing_columns"] = missing_columns
                write_yaml(self.config.report_file_path, report)
                logger.error(f"{missing_columns} columns are missing in the data")
                return False

            # Data type validation
            wrong_types = []
            for column in schema_cols:
                expected_dtype = schema_cols[column]
                actual_dtype = str(df[column].dtype)
                if expected_dtype not in actual_dtype:
                    wrong_types.append({column: {"expected": expected_dtype, "actual": actual_dtype}})
            if wrong_types:
                report["data_validation_status"] = False
                report["wrong_types"] = wrong_types
                write_yaml(self.config.report_file_path, report)
                logger.error(f"Wrong data types: {wrong_types}")
                return False

            report["data_validation_status"] = True
            write_yaml(self.config.report_file_path, report)
            logger.info("Data validation passed.")
            return True

        except Exception as e:
            logger.error(f"{e}")
            write_yaml(self.config.report_file_path, {"data_validation_status": False, "error": str(e)})
            raise e
