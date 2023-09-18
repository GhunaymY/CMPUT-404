#Lab 1: Virtualenv & Curl Lab


#Python Script:
import requests
print(requests.__version__)
print(requests.get("http://www.google.com"))
print(requests.get("https://raw.githubusercontent.com/GhunaymY/CMPUT-404/main/L1.py").text)
