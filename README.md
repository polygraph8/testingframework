# testingframework， 测试自动化框架   
A light Testng framework base on python , for web testing ,android/IOS app testing and testing for service interface.  
It can do :
1. record the web http request via mitmproxy
2. generate testcase based on the recorded request.  
3. replay the case . 

**设计目标:**   

    希望在手动测试和自动化测试中建立一个桥梁，利用手动测试产生的结果，来自动生成测试用例。
 
**设计思路：**

        通过监控手动测试的结果，我们可以对手动测试的结果进行分析，得到请求的条件以及返回的结果。
        通过泛化请求条件，例如：边界值，等价值,安全测试等，我们可以自动生成更多的测试用例。
        通过自动生成的测试用例，我们可以得到返回结果，以及预期的结果，以及判断对错。

**程序结构：**

    record.py  记录对服务器的请求，包括header,url , method,cookie,data 
    gencase.py 根据记录的请求参数的类型，为每个参数生成不同的数据值，组合为测试用例。
               目前支持的请求数据有 form-data, json, plaintext， 
               函数分别在：gencase_formdata(data)， gencase_json(jsondict)，gencase_query(data)
    runcase.py 取出产生的测试用例，生成服务器请求，向服务器发送请求。
    mylib.py   测试用例保存在mysql 数据库中，提供接口函数进行测试用例的存取 
    
    results = db.myselect_case("rest",5,'gencase',fields)
    for  record in results:
        response = run_case(record)            

**测试用例的扩展：** 

    这个版本仅对数字类型取值和字符串类型取值进行了数据的简单扩展。
    见 testcaselib.py  ，对测试用例测扩展 主要修改这个文件即可。
    
    数字扩展为：
              
         def extendcase_digital():
            max32= 1024*1024*1024*4-1
            max64 = (max32+1)*(max32+1)-1
            return (0,max32,max64,-max32,-max64)

    字符串扩展为：
    
    def extendcase_str():
        snull = ''
        s1k = 'a'*1024
       # s1M = 'a'*1024*1024
        return (snull, s1k)
 
![Image text](image/gencase.png)
 
 
 后续工作：
      可以集成压力测试工具
      安全测试工具： 
      




    
    
