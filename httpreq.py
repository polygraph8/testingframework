import requests

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',
}
proxies = {}
headers_in = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie': "",
    'Host': 'www.baidu.com',
}

def http_req(url,req_data={},method='GET',heads=headers_in,fn=""):
    try:
        if method == "GET":  # GET http://httpbin.org/get?name=liujun&addr=beijing HTTP/1.1
            r = requests.get(url,params=req_data,proxies=proxies,timeout=0.01,headers=heads)
            print(r.text)
            print(r.status_code)
            if fn!="":
                with open(fn, 'wb') as f:
                    f.write(r.content)
        if method == "POST":
            if fn!="":
                files = {'file': open(fn, 'rb')}   #  'favicon.ico'
                r = requests.post(url, files=files,proxies=proxies,)
                print(r.text)
            else:
                r = requests.post(url, data=req_data,proxies=proxies)
                print(r.text)
    except requests.exceptions.ReadTimeout as e:
        print('读数据超时')
    except requests.exceptions.ConnectTimeout as e:
        print('连接超时')


#proxies={}
geturl='http://httpbin.org/get'
posturl='http://httpbin.org/post'
geturl="http://127.0.0.1/get.php"
posturl="http://127.0.0.1/post.php"
req_data={"name":'liujun','addr':'beijing'}

http_req(geturl,req_data)
http_req(posturl,req_data,method='POST')
http_req(posturl,req_data,method="POST",heads=headers_in,fn="car.jpg")

#import requests
#s = requests.Session()
#s.get('http://httpbin.org/cookies/set/number/123456789')
#r = s.get('http://httpbin.org/cookies')
#print(r.text)
