import os
import sys
import logging

logging_dir = "logs"
log_file_path = os.path.join(logging_dir, "running_logs.log")
os.makedirs(logging_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(levelname)s:  %(message)s',

    handlers= [
        logging.FileHandler(log_file_path, mode='w'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)