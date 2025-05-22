import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\demo1.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S",force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger