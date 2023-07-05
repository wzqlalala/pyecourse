import requests
url = "https://www.amazon.cn/dp/B08CDLHMFF/ref=s9_acsd_hps_bw_c2_x_0_i?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-4&pf_rd_r=7AF1C8CV1G5PK1ZTAGAD&pf_rd_t=101&pf_rd_p=583d0f00-a1c8-428a-a276-77204a982ab2&pf_rd_i=2334070071"
try:
    r =requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
    print(r.request.headers)
    kv = {'User-Agent': 'Mozilla/5.0'}
    r.encoding=r.apparent_encoding
    r =requests.get(url,headers = kv)
    print(r.status_code)
    print(r.request.headers)
    print(r.text)