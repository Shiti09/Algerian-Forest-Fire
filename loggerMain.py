import logging

class FirePredictLogger:

    def ineuron_scrap_logger( file_name='log_file.log', log_level=logging.DEBUG):
        logger = logging.getLogger("FirePredictLogger")
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("log_file.log")
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger