import logging
class Base:
    def get_logger(self):
        logs = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        logs.setLevel(logging.INFO)
        logs.setLevel(logging.DEBUG)
        fileHandler.setFormatter(format)
        logs.addHandler(fileHandler)
        return logs

    def take_screenshot(self,driver):
        driver.save_screenshot("./booking.png")
