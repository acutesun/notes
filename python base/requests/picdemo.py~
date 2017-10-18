import requests,os
path='/home/sun/abc.jpg'
try:
    url = 'http://img0.dili360.com/rw9/ga/M00/43/98/wKgBy1eF-wOAJFYdADKuJTtEXYM688.tub.jpg'
    r = requests.get(url)
    r.raise_for_status()
    with open(path,'wb') as f:
        f.write(r.content)
    print('文件保存成功')
except:
    print('failed')
