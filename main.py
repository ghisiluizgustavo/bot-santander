from selenium import webdriver
import constants
import time


class BotSantanderCard:

    def __init__(self, browser):
        self.__browser = browser
        self.run()

    def run(self):
        self.home()
        self.cardDatas()
        self.downloadPdf()

    def home(self):
        print("Tela inicial...")
        self.__browser.get("https://www.santander.com.br/")
        cpf = self.__browser.find_element_by_xpath(
            '//*[@id="appHeader"]/header/login-field/div/form/div/div/div[1]/div/input')
        cpf.clear()
        cpf.send_keys(constants.CPF)
        self.__browser.find_element_by_xpath(
            '//*[@id="appHeader"]/header/login-field/div/form/div/div/div[1]/div/icon-circle-arrow/div') \
            .click()
        time.sleep(5)

    def cardDatas(self):
        print("Dados do cartão ....")
        numCard = self.__browser.find_element_by_xpath('//*[@id="nroCartao"]')
        numCard.send_keys(constants.QUATRO_DIGITOS)
        passWord = self.__browser.find_element_by_xpath('//*[@id="senha"]')
        passWord.send_keys(constants.SENHA)
        self.__browser.find_element_by_xpath('//*[@id="Entrar"]').click()
        time.sleep(5)

    def downloadPdf(self):
        print("Começando a baixar...")
        self.__browser.find_element_by_xpath('//*[@id="cartoesMinNC_WAR_Cartoes_WIDGET"]/header/a').click()
        time.sleep(5)
        self.__browser.find_element_by_xpath(
            '//*[@id="_cartoesMinNC_WAR_Cartoes_WIDGET__VIEW"]/form/footer/div/button').click()
        time.sleep(5)
        self.__browser.find_element_by_xpath('//*[@id="_W0000014_WAR_Cartoes_WIDGET_closeTab"]').click()
        time.sleep(5)
        self.__browser.find_element_by_xpath(
            '//*[@id="_W0000014_WAR_Cartoes_WIDGET__VIEW"]/div/form/fieldset/div[2]/div/div/div[3]/div[1]/ul/li[1]/a/span') \
            .click()
        time.sleep(5)
        self.__browser.close()
        print("Download finalizado!")


if __name__ == "__main__":
    browser = webdriver.Chrome()
    BotSantanderCard(browser)
