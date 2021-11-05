def currency_rates(currency):
    import requests
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    for element_code in req.split('<CharCode>'):
        code = element_code[0:element_code.find('<')]
        if code == currency.upper():
            for element_nominal in element_code.split('<Nominal>'):
                nominal = element_nominal[0:element_nominal.find('<')]
            for element_value in element_code.split('<Value>'):
                value = element_value[0:element_value.find('<')]
            return print(f'Курс RUB за {nominal} {code} = {value}')


if __name__ == '__main__':
   currency_rates('usd')