import requests
url = "https://m.ip138.com/ip.asp?ip="
# r = requests.get("https://www.ip138.com/iplookup.asp?ip=222.244.139.68&action=2")
r = requests.get(url+'202.204.80.112')
print(r.status_code)