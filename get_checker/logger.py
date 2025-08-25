import logging

# Function to say in log file: hour, minute, etc...
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("get_checker.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("GetChecker")