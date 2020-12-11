from pylenium.driver import Pylenium
from selenium.common.exceptions import NoAlertPresentException


class AlertActions:
    def __init__(self, py: Pylenium):
        self.py = py
        self.alert = None

    def wait_for_alert(self):
        return self.py\
            .wait(ignored_exceptions=[NoAlertPresentException])\
            .until(lambda _: self.py.webdriver.switch_to.alert)

    def accept(self):
        self.wait_for_alert().accept()
