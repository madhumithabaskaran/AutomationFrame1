import logging
import os
class LogGen:
    @staticmethod
    def loggen():

        logger=logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\auto.log',mode='w')
        formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fhandler.setFormatter(formatter)
        chandler=logging.StreamHandler()
        chandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.addHandler(chandler)
        logger.setLevel(logging.INFO)
        return logger
