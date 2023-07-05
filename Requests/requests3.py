# import requests
# path = "E://PYECourse//Requests//abc.jpg"
# r = requests.get("http://www.natgeo.com.cn/upload/images/2020/11/7927804254afdb3f.jpg")
# print(r.status_code)
# with open(path,'wb') as f:
#     f.write(r.content)
# f.close()
import requests
path = "E://PYECourse//Requests//changge.mp4"
r = requests.get("https://v.qq.com/x/page/u003668tbq5.html")
print(r.status_code)
print(r.text)
# with open(path,'wb') as f:
#     f.write(r.content)
# f.close()