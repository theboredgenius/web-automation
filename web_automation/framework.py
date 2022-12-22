# System libraries
from abc import ABC, abstractmethod
from enum import Enum, auto
import time

# External libraries
from selenium.webdriver import Chrome, ChromeOptions, Edge, EdgeOptions, Firefox, FirefoxOptions, Ie, IeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Local libraries
from .exceptions import BrowserException


class Browser(Enum):
    CHROME = auto()
    EDGE = auto()
    FIREFOX = auto()
    SAFARI = auto()


class SelectBy(Enum):
    INDEX = auto()
    TEXT = auto()
    VALUE = auto()


mime_types = ["application/x-7z-compressed",
              "application/pdf",
              "application/octet-stream",
              "image/bmp",
              "text/csv",
              "image/gif",
              "application/json",
              "image/jpeg",
              "image/x-citrix-jpeg",
              "image/pjpeg",
              "application/vnd.ms-excel",
              "application/vnd.ms-excel.addin.macroenabled.12",
              "application/vnd.ms-excel.sheet.binary.macroenabled.12",
              "application/vnd.ms-excel.template.macroenabled.12",
              "application/vnd.ms-excel.sheet.macroenabled.12",
              "application/vnd.openxmlformats-officedocument.presentationml.presentation",
              "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
              "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
              "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
              "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
              "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
              "application/vnd.ms-powerpoint",
              "application/vnd.ms-powerpoint.presentation.macroenabled.12",
              "application/msword",
              "image/png",
              "image/x-citrix-png",
              "image/x-png",
              "image/x-portable-pixmap",
              "application/x-rar-compressed",
              "image/svg+xml",
              "application/zip"]


def _create_driver(browser: Browser,
                   headless: bool = False,
                   download_path: str = ''):
    """
    Create driver object based on browser and browser options

    :param browser: Browser type
    :type browser: Browser
    :param options:
    :type options: Union[ChromeOptions | EdgeOptions | FirefoxOptions | IeOptions]
    :return: WebDriver
    """
    match browser:
        case Browser.CHROME:
            options = ChromeOptions()
            options.headless = headless
            if download_path != '':
                prefs = {
                    'download.default_directory': download_path
                }
                options.add_experimental_option('prefs', prefs)
            return Chrome(options=options)

        case Browser.EDGE:
            options = EdgeOptions()
            options.headless = headless
            if download_path != '':
                prefs = {
                    'download.default_directory': download_path
                }
                options.add_experimental_option('prefs', prefs)
            return Edge(options=options)

        case Browser.FIREFOX:
            options = FirefoxOptions()
            options.headless = headless
            if download_path != '':
                options.set_preference('browser.download.folderList', 2)
                options.set_preference(
                    'browser.download.manager.showWhenStarting', False)
                options.set_preference('browser.download.dir', download_path)
                options.set_preference(
                    'browser.helperApps.neverAsk.saveToDisk', ';'.join(mime_types))
            return Firefox(options=options)

        case Browser.SAFARI:
            options = IeOptions()
            options.headless = headless
            return Ie(options=options)

        case _:
            raise BrowserException('No supporting browser provided!')


class Framework(ABC):
    """
    Class to be inherited by the target class for automating
    """

    driver = None

    def __init__(self,
                 browser: Browser,
                 wait: int = 30,
                 headless: bool = False,
                 download_path: str = ''):
        """
        Create a webdriver instance based on the browser mentioned

        :param browser: browser enum value
        :type browser: Browser
        :param wait: Implicit wait for elements in browser
        :type wait: int
        :param options: Browser configurations
        :type options: ChromeOptions | EdgeOptions | FirefoxOptions | IeOptions]
        """
        self.driver = _create_driver(browser, headless, download_path)
        self.driver.implicitly_wait(wait)
        self.run()

    def type(self, elem_type: By, elem_id: str, value: str, clear: bool = True):
        """
        Type the value to the element mentioned

        :param elem_type: Search type
        :type elem_type: By
        :param elem_id: Element search id
        :type elem_id: str
        :param value: Value to be typed in the element
        :type value: str
        :param clear: Whether clear the element before typing
        :type clear: bool
        :return: None
        :rtype: None
        """
        elem = self.driver.find_element(elem_type, elem_id)
        if clear:
            elem.clear()
        elem.send_keys(value)

    def click(self, elem_type: By, elem_id: str):
        """
        Click the element mentioned

        :param elem_type: Search type
        :type elem_type: By
        :param elem_id: Element search id
        :type elem_id: str
        :return: None
        :rtype: None
        """
        elem = self.driver.find_element(elem_type, elem_id)
        elem.click()

    def select(self, elem_type: By, elem_id: str, select_by: SelectBy, value: str):
        """
        Select the dropdown value

        :param elem_type: Search type
        :type elem_type: By
        :param elem_id: Element search id
        :type elem_id: str
        :param select_by: Select by option
        :type select_by: SelectBy
        :param value: Value to be selected
        :type value: str
        :return: None
        :rtype: None
        """
        elem = Select(self.driver.find_element(elem_type, elem_id))
        match select_by:
            case SelectBy.INDEX:
                elem.select_by_index(value)
            case SelectBy.TEXT:
                elem.select_by_visible_text(value)
            case SelectBy.VALUE:
                elem.select_by_value(value)

    def deselect(self, elem_type: By, elem_id: str):
        """
        Clear the dropdown values

        :param elem_type: Search type
        :type elem_type: By
        :param elem_id: Element search id
        :type elem_id: str
        :return: None
        :rtype: None
        """
        elem = Select(self.driver.find_element(elem_type, elem_id))
        elem.deselect_all()

    def check_if_exists(self, elem_type: By, elem_id: str):
        """
        Check whether the element is present in the page or not

        :param elem_type: Search type
        :type elem_type: By
        :param elem_id: Element search id
        :type elem_id: str
        :return: None
        :rtype: None
        """
        self.driver.find_element(elem_type, elem_id)

    def get_children(self):
        pass

    def navigate_to(self, url: str):
        """
        Navigate to the mentioned URL

        :param url: URL to be navigated to
        :type url: str
        :return: None
        :rtype: None
        """
        self.driver.get(url)

    def wait(self, wait_time: int = 0):
        """
        Wait for the mentioned amount of time

        :param wait_time: waiting time (in seconds)
        :type wait_time: int
        :return: None
        :rtype: None
        """
        time.sleep(wait_time)

    def __del__(self):
        if self.driver:
            self.driver.quit()

    @abstractmethod
    def run(self):
        pass
