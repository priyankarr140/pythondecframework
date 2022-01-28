from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    cancelButton = (By.ID, "wzrk-cancel")
    searchBoxButton = (By.ID, "4")
    searchInputButton = (By.CLASS_NAME, "eTcNgn")
    movieOptionButton=(By.CLASS_NAME,'sc-chAAoq')
    bookTicketButton=(By.XPATH,"//*[text()='Book tickets']")
    threedimensionOptionButton=(By.XPATH,"//span[text()='3D']")

    def cancel(self):
        return self.driver.find_element(*HomePage.cancelButton)

    def searchBox(self):
        return self.driver.find_element(*HomePage.searchBoxButton)

    def searchInput(self):
        return self.driver.find_element(*HomePage.searchInputButton)

    def movieOption(self):
        return self.driver.find_element(*HomePage.movieOptionButton)

    def bookTicket(self):
        return self.driver.find_element(*HomePage.bookTicketButton)

    def threedimensionOption(self):
        return self.driver.find_element(*HomePage.threedimensionOptionButton)