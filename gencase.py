from mylib import *

max_gencase_num = 100


def gen_testcase(db,req):
    host, url, method, cookie, headers, data = req
#    print(url)
    gendata_array = []

    if "<?xml" in data : # xml
        gendata_array=gencase_xml(data)
    elif "form-data" in data : # form-data split byte ----webkit
        gendata_array=gencase_formdata(data)
    elif "{" in data:
        print("data  is json:"+ data)
        jsondict = json.loads(data)
        gendict_array = gencase_json(jsondict)
        for d in gendict_array:
            gendata_array.append(json.dumps(d))
    elif "=" in data:
        print("data is query:"+ data)
        gendata_array = gencase_query(data)
    i=0
    for gendata in gendata_array:
        db.myinsert_gencase(host, url, method, cookie, headers, gendata)
        i=i+1
        if i>max_gencase_num :
            break
    print("gencase  num: ",i)

if __name__ == '__main__':

    db=  myMySQL("test")

    results = db.myselect_case("rest",5)
    for  record in results:
         gen_testcase(db,record)
