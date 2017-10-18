import requests
keyword = "python"
kv = {'wd':keyword}
head = {'user-agent':'Mozilla/5.0'}

try:
    r = requests.get('http://www.baidu.com/s',params=kv,headers=head)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('抓取失败')
