from selenium.webdriver import Chrome


def chromedriver():
    drive = Chrome(executable_path='/Webdrivers/chromedriver.exe')


from selenium.webdriver import Edge


def edgedriver():
    drive = Edge(executable_path='/Webdrivers/MicrosoftWebDriver.exe')


from selenium.webdriver import Firefox


def firefoxdriver():
    drive = Firefox(executable_path='/Webdrivers/geckodriver.exe')
