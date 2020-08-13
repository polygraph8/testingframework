from mitmproxy import ctx
from mylib import myMySQL


def record2db(flow):
    host = flow.request.host
    url = flow.request.url
    method= flow.request.method
    cookie = flow.response.cookies
    headers = flow.response.headers
    data = flow.request.text
    response_header = flow.response.headers
    response_text = flow.response.text
    response_status_code = flow.response.status_code
    response_cookie = flow.response.cookies
    print("===================================================================")
    print(type(headers))
    print("===================================================================")
    #if data.find("WebKitFormBoundary") > -1:
    #    data=""

    db=  myMySQL("test")
    sql= db.myinsert_proxyed(host,url,method,cookie,headers,data,response_header,response_cookie,response_text,response_status_code)
    logstr2file(sql)

def logstr2file(s):
    fp=open("sql.log","a+",encoding='utf-8')
    fp.write(s)
    fp.write("\n\n\nend of sql \n")
    fp.close()
def log2file(flow):
    fp=open("url.log","a+",encoding='utf-8')
    fp.write(flow.request.url +"\n")
    fp.write(flow.request.pretty_url + "\n")
    fp.write(flow.request.method +"\n")
    fp.write(flow.request.path + "\n")
    fp.write("flow.request.get_text()" + "\n")
    fp.write(flow.request.text + "\n################################\n")
    headers = flow.request.headers
    fp.write("\n\nheader\n\n")
    fp.write(repr(headers))
    fp.write("\n\nresponse\n\n")
    #fp.write(repr(flow.request))
    fp.write(flow.response.text)
    fp.write("\n\ncookie\n\n")
    fp.write(repr(flow.request.cookies))
    fp.write("\n\n\n===========================================\n")
    fp.close()


def response(flow):
    response =flow.response

    if 'live.kuaishou.com/rest/' in flow.request.url:
                 fp=open("live.kuaishou.log","ab+")
                 fp.write(flow.request.url.encode('utf-8'))
#                 fp.write(flow.request)
                 fp.write(response.content)
                 fp.write(b"\nendSession\n")
                 fp.close()

                 record2db(flow)


