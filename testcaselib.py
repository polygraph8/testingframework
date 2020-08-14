import json
from copy import deepcopy

def extendcase_digital():

    max32= 1024*1024*1024*4-1
    max64 = (max32+1)*(max32+1)-1
    return (0,max32,max64,-max32,-max64)

def extendcase_str():
    snull = ''
    s1k = 'a'*1024
   # s1M = 'a'*1024*1024
    return (snull, s1k)


def gencase_json(jsondict):
    case_dict_array = []
    if not isinstance(jsondict,dict) :
        print("Not json dict:",jsondict,type(jsondict))
        return case_dict_array
    k=""
    for key in jsondict.keys():
        k=key
        break
    v= jsondict[k]
    if (isinstance(v,int)) or isinstance(v,float):
            print(k,'is a number')
            digits = extendcase_digital()
            for digit in digits:
                onecase={}
                onecase[k] =digit
                print(onecase)
                case_dict_array.append(onecase)

    if (isinstance(v, str)) or isinstance(v, str):
            print(k, 'is a str')
            strs = extendcase_str()
            for s in strs:
                onecase = {}
                onecase[k] = s
                print(onecase)
                case_dict_array.append(onecase)

    if len(jsondict.keys()) > 1 :
        jsondict.pop(k)
        caseb = gencase_json(jsondict)
        case_array_new = []
        for onecase_dicta in case_dict_array:
            for onecaseb in caseb:
                newcase_dict = deepcopy(onecase_dicta)
                newcase_dict.update(onecaseb)
                case_array_new.append(newcase_dict)
        return case_array_new
    else:
        return case_dict_array


def gencase_query(data):
        case_array = []
        if data.find('&') == -1 and data.find('=') == -1 :
            print("Not query data:  ---&---- "+data)
            return case_array

        query_array = data.split("&")
        query = query_array[0]

        k, v = query.split("=")
        if v.isdigit() or (v.count(".")==1 and v.replace(".",'').isdigit()) :
           print(v+" is digital or float ")
           digits = extendcase_digital()
           for digit in digits :
               onecase = k+"="+str(digit)
               print(onecase )
               case_array.append(onecase)
        else:
           print(v +" is str")
           strs = extendcase_str()
           for s in strs:
                 onecase=k+ "=" +s
                 print(onecase)
                 case_array.append(onecase)

        if len(query_array) > 1:
             caseb = gencase_query("&".join(query_array[1:]))
             case_array_new = []
             for onecasea in case_array:
                 for onecaseb in caseb:
                     case = "&".join([onecasea,onecaseb])
                     case_array_new.append(case)
             return case_array_new
        else:
             return case_array


def gencase_xml(data):  # 手头没有XML 的POST 示例，以后有需要用到框架的请自行解析
        case_array = []
        if data.find('xml') == -1:
            return case_array

        onecase = data
        case_array.append(onecase)
        return case_array


def gencase_formdata(data):
    case_array = []
    query_split_flag="\r\n------WebKitFormBoundary"

    if data.find('form-data') == -1:
           if data.find("WebKitForm") == -1 :
               print("Not form data:" + data)
               return case_array
           else:
               endtail= data.split(query_split_flag)[1]
               case_array.append(endtail)
               return case_array



    query_array = data.split(query_split_flag)

    query = query_array[0]
    next_qeruy_index = 1
    if query =="":
        query=query_array[1]
        next_qeruy_index = 2
    kv_split_flag="\r\n\r\n"
    k, v = query.split(kv_split_flag)
    vtail = "\r\n"
    v=v.replace(vtail,"")
    if v.isdigit() or (v.count(".") == 1 and v.replace(".", '').isdigit()):
 #       print(v + " is digital or float ")
        digits = extendcase_digital()
        for digit in digits:
            onecase = k + kv_split_flag + str(digit)+vtail
#            print(onecase)
            case_array.append(onecase)
    else:
#        print(v + " is str")
        strs = extendcase_str()
        for s in strs:
            onecase = k + kv_split_flag  + s +vtail
#            print(onecase)
            case_array.append(onecase)
#    print("##########case_array len : %d" % len(case_array))
    if len(query_array) > next_qeruy_index :
        caseb = gencase_formdata(query_split_flag + query_split_flag.join(query_array[next_qeruy_index:]) )
        case_array_new = []
        for onecasea in case_array:
            for onecaseb in caseb:
                case = query_split_flag.join([onecasea, onecaseb])
                case_array_new.append(case)

        return case_array_new
    else:
        return case_array
