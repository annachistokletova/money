# import requests
# from bs4 import BeautifulSoup
# import time
#
# DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&ei=NPF3YriLHovbrgTgnLH4Dg&ved=0ahUKEwi49fzhqtD3AhWLrYsKHWBODO8Q4dUDCA4&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6DggAEI8BEOoCEIwDEOUCOg4ILhCPARDqAhCMAxDlAjoECAAQQzoHCAAQsQMQQzoOCC4QgAQQsQMQxwEQowI6CAgAELEDEIMBOggIABCABBCxAzoICC4QsQMQgwE6BggAEAoQQzoKCAAQsQMQgwEQQzoHCC4Q1AIQQzoFCC4QgAQ6CwguEIAEELEDENQCOgsIABCABBCxAxDJAzoLCAAQgAQQsQMQgwE6EggAELEDEIMBELEDEAoQRhCCAjoECAAQCjoPCAAQsQMQgwEQChBGEIICSgQIQRgASgQIRhgAUIgLWMhJYMFPaARwAXgAgAFdiAGBC5IBAjE3mAEAoAEBsAEKwAEB&sclient=gws-wiz'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
#
# def check_currency():
#     full_page = requests.get(DOLLAR_RUB, headers=headers)
#
#     soup = BeautifulSoup(full_page.content, 'html.parser')
#
#     convert = soup.findAll("span", {"class":"DFlfde", "class":"SwHCTb", "data-precision":2})
#     print("Сейчас курс: 1 доллар = " + convert[0].text)
#     time.sleep(3)
#     check_currency()
#
# check_currency()

# import requests
# from bs4 import BeautifulSoup
# import time
#
# class Currency:
#     DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&ei=NPF3YriLHovbrgTgnLH4Dg&ved=0ahUKEwi49fzhqtD3AhWLrYsKHWBODO8Q4dUDCA4&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6DggAEI8BEOoCEIwDEOUCOg4ILhCPARDqAhCMAxDlAjoECAAQQzoHCAAQsQMQQzoOCC4QgAQQsQMQxwEQowI6CAgAELEDEIMBOggIABCABBCxAzoICC4QsQMQgwE6BggAEAoQQzoKCAAQsQMQgwEQQzoHCC4Q1AIQQzoFCC4QgAQ6CwguEIAEELEDENQCOgsIABCABBCxAxDJAzoLCAAQgAQQsQMQgwE6EggAELEDEIMBELEDEAoQRhCCAjoECAAQCjoPCAAQsQMQgwEQChBGEIICSgQIQRgASgQIRhgAUIgLWMhJYMFPaARwAXgAgAFdiAGBC5IBAjE3mAEAoAEBsAEKwAEB&sclient=gws-wiz'
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
#
#     current_converted_price = 0
#     difference = 5
#
#     def __init__(self):
#         self.current_converted_price = float (self.get_currency_price().replace("," , "."))
#
#     def get_currency_price(self):
#         full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
#
#         soup = BeautifulSoup(full_page.content, 'html.parser')
#
#         convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
#         return convert[0].text
#
#     def check_currency(self):
#         currency = float(self.get_currency_price().replace("," , "."))
#         if currency >= self.current_converted_price + self.difference:
#             print("Курс сильно вырос, может пора что-то делать?")
#         elif currency <= self.current_converted_price - self.difference:
#             print("Курс сильно упал, может пора что-то делать?")
#         print("Сейчас курс: 1 доллар = " + str(currency))
#         time.sleep(3)
#         self.check_currency()
#
# currency = Currency()
# currency.check_currency()

import requests
from bs4 import BeautifulSoup
import time

class Currency:
    EURO_RUB = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&ei=oGl6YpnWEOrhrgSa-IXQDg&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQ0oECEEYAEoECEYYAFAAWABgzBNoAnABeACAAQCIAQCSAQCYAQDIAQrAAQE&sclient=gws-wiz'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float (self.get_currency_price().replace("," , "."))

    def get_currency_price(self):
        full_page = requests.get(self.EURO_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace("," , "."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно вырос, может пора что-то делать?")
        elif currency <= self.current_converted_price - self.difference:
            print("Курс сильно упал, может пора что-то делать?")
        print("Сейчас курс: 1 евро = " + str(currency))
        time.sleep(3)
        self.check_currency()

currency = Currency()
currency.check_currency()