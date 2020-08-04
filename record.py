from mitmproxy import ctx

def responseheaders( flow):
    fp=open("resonseheader.log","a+")
    headers = flow.response.headers
    fp.write(repr(headers))
    fp.close()
    """
        HTTP response headers were successfully read. At this point, the body
        is empty.
    """

def record2db(flow):
    fp=open("url2db.log","a+",encoding='utf-8')
    fp.write(flow.request.url + "\n")
    fp.write(flow.request.method +"\n")
    fp.write(flow.request.path + "\n")
    fp.write("flow.request.get_text()" + "\n")
    fp.write(flow.request.text + "\n################################\n")
    headers = flow.request.headers
    fp.write("\n\nheader\n\n")
    fp.write(repr(headers))
    fp.write("\n\nresponse\n\n")
    fp.write(flow.response.status_code)
    fp.write(flow.response.headers)
    fp.write(flow.response.cookies)
    fp.write(flow.response.text)
    fp.write("\n\ncookie\n\n")
    fp.write(repr(flow.request.cookies))
    fp.close()

def response(flow):
    response =flow.response
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



    if 'live.kuaishou.com/rest/' in flow.request.url:
                 fp=open("live.kuaishou.log","ab+")
                 fp.write(flow.request.url.encode('utf-8'))
#                 fp.write(flow.request)
                 fp.write(response.content)
                 fp.write(b"\nendSession\n")
                 fp.close()

    if 'ksapisrv.com' in flow.request.url:
                 fp=open("ksapisrv.log","ab+")
                 fp.write(response.content)
                 fp.write(b"\nendSession\n")
                 fp.close()
