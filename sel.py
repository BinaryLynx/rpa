from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from excel import get_info_from_file


class SeleniumController:

    def __init__(self, website="https://rpachallenge.com/") -> None:
        # сетап селениума
        # options = Options()
        # options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # options=options
        self.driver.get(website)

    def get_inputs(self):
        # нахождение полей ввода
        phone = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelPhone]")
        companyName = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelCompanyName]")
        lastName = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelLastName]")
        address = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelAddress]")
        email = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelEmail]")
        role = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelRole]")
        firstName = self.driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name=labelFirstName]")
        # нахождение кнопки отправки формы
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "input[type=submit]")

        # добавление полей ввода в массив в порядке соответствующем файлу.
        inputs = [firstName, lastName, companyName, role, address, email, phone]
        return (inputs, submit_btn)

    def input_data(self, data_file_path):
        success_count = 0
        try:
            for data_row in get_info_from_file(data_file_path):
                inputs, submit_btn = self.get_inputs()
                for i in range(len(data_row)):
                    self.driver.implicitly_wait(2)
                    inputs[i].clear()
                    inputs[i].send_keys(data_row[i])
                submit_btn.click()
                success_count += 1
        except:
            return f"Ошибка при вводе значений в поле ввода; успешно обработано {success_count} записей"

        return f"Успешно обработано {success_count} записей"
