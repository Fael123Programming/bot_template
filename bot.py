from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager, ChromeType

from datetime import datetime

import constants
import time

class Bot(Chrome):
    
    __slots__ = ['_start_datetime']
    
    def __init__(self):
        options = ChromeOptions()
        prefs = {
            'profile.managed_default_content_settings.images': 2,  # Disable images for being loaded.
            'intl.accept_languages': 'en-GB'                       # Set browser default language to English.
        }
        options.add_experimental_option(
            'prefs',
            prefs
        )
        super().__init__(
            service=ChromeService(
                ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM
                ).install()
            ),
            options=options
        )
        self._start_datetime = datetime.now()
        print(f'Bot started on {self._start_datetime}')

        """This is the main method where the main logic should be put like
        accessing the main websites and fetching the desired data from there.
        As such, it could be needed to add another separate methods and call them
        from here.
        """
    def execute(self):
        pass
    
    def __enter__(self):
        self.get(constants.MAIN_URL)
        time.sleep(5)
        
    def __exit__(self, exc_type, exc, traceback):
        self.quit()
        now = datetime.now()
        print(f'Bot execution finished on {now}')
        print(f'Time took: {now - self._start_datetime}')
    
