import logging
import datetime
import traceback

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init_logger()
        return cls._instance
    
    def init_logger(self):
        current_date = datetime.datetime.now().strftime('%Y%m%d')
        self.logger = logging.getLogger('ny_app')
        self.logger.setLevel(logging.DEBUG)
        
        self.log_filename = rf"./log/{current_date}.log"  # Added log_filename attribute
        file_handler = logging.FileHandler(self.log_filename, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')  # Fix formatter
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    @staticmethod
    def logger_info(msg):
        return Logger()._instance.logger.info(msg)
    
    @staticmethod
    def logger_debug(msg):
        return Logger()._instance.logger.debug(msg)
    
    @staticmethod
    def logger_warning(msg):
        return Logger()._instance.logger.warning(msg)    
    
    @staticmethod
    def logger_error(msg):
        return Logger()._instance.logger.error(msg)    
    
    @staticmethod
    def logger_trackback():
        return traceback.format_exc()

if __name__ == "__main__":
    logger = Logger()
    print(logger.log_filename)
