import requests,time

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '异常'
        
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    start = time.time()
    for i in range(1,100):
        getHTMLText(url)
        
    end = time.time()
    print(end-start)
