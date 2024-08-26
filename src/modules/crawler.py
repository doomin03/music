from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd 


class base(ABC):
    def __init__(self) -> None:
        self.options = Options()
        self.options.add_argument('--window-size=1920x1080')
        # self.options.add_argument('--headless')
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-images")
        self.options.add_argument('--incognito')
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')


        self.service = Service()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, 20)
        
    def max_page(self):
        pass
    @abstractmethod
    def pageSetting(self) -> None:
        pass

    


