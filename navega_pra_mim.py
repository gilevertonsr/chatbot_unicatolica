import time
from splinter import Browser


def navega_ai():
    #browser = Browser(driver_name="chrome")
    browser = Browser(driver_name="firefox")
    browser.visit("https://youtube.com")
    caixa_de_pesquisa = browser.find_by_name("search_query")
    botao_pesquisar = browser.find_by_id("search-icon-legacy")
    caixa_de_pesquisa.type("king size do rio de janeiro")
    botao_pesquisar.click()
    time.sleep(10)


if __name__ == '__main__':
    navega_ai()

