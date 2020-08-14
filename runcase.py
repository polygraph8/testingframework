import requests
from mylib import *
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

def http_req(url,req_data={},method='GET',headers_dict=headers_in,fn=""):
    r= ""
    try:
        if method == "GET":  # GET http://httpbin.org/get?name=liujun&addr=beijing HTTP/1.1
            r = requests.get(url,params=req_data,proxies=proxies,timeout=0.01,headers=headers_dict)

            if fn!="":
                with open(fn, 'wb') as f:
                    f.write(r.content)
        if method == "POST":
            if fn!="":
                files = {'file': open(fn, 'rb')}   #  'favicon.ico'
                r = requests.post(url, files=files,headers=headers_dict , proxies=proxies,)

            else:
                r = requests.post(url, data=req_data,headers= headers_dict, proxies=proxies)
        return r
    except requests.exceptions.ReadTimeout as e:
        print('读数据超时')
    except requests.exceptions.ConnectTimeout as e:
        print('连接超时')

def test():
    #proxies={}
    geturl='http://httpbin.org/get'
    posturl='http://httpbin.org/post'
    geturl="http://127.0.0.1/get.php"
    posturl="http://127.0.0.1/post.php"
    req_data={"name":'polygraph','addr':'beijing'}

    http_req(geturl,req_data)
    http_req(posturl,req_data,method='POST')
    http_req(posturl,req_data,method="POST",heads=headers_in,fn="car.jpg")

def headers2dict(headerstr):
    headerstr = headerstr.replace("b'","'").replace("Headers[('","").replace("')]","")
    arr=  headerstr.split("'), ('")
    header_dict = {}
    for header in arr:
        k,v = header.split("', '")
    if k != "Content-Length" and k != "Data":
            header_dict[k] = v
#            print("_%s:%s_" %(k,v))
    return header_dict

def run_case(record):
    host, url, method, headers, data = record
    print(headers)
    header_dict = headers2dict(headers)
    r= http_req(url,data, method, header_dict )
    print(url)
    print(r.status_code)
    print(r.text)
    return  r

if __name__ == '__main__':
    db=  myMySQL("test")
    fields = "host, url, method, headers, data"
    results = db.myselect_case("rest",5,'gencase',fields)
    for  record in results:
        response = run_case(record)




