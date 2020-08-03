from mitmproxy import ctx

def response(flow): 

    response =flow.response
    fp=open("url.log","a+")
    fp.write(flow.request.url +"\n")
    fp.close()



    if 'mtop.taobao.iliad.comment.query.anchorlatest' in flow.request.url:
            if response.content.find(b'content":')> -1:
                 fp=open("taobao-vistor.log","ab+")
                 fp.write(response.content)
                 fp.write(b"\nendSession\n")
                 fp.close()
