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
        print("Not dict:",jsondict,type(jsondict))
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
            print("Not form data:"+data)
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