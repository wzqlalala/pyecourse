import requests
kv ={'wd':'Python'}
r = requests.get("http://www.baidu.com/s",params=kv)
print(r.status_code)
print(len(r.text))