#  手动转自动化WEB接口测试框架    Automated Testing Web Interface Testing Framework From Manual testing 

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

**系统准备：**
    **python:** 
        python 3.7 
        pip install mitmproxy pymysql    
    **mysql:** 
        gencase.sql 在 test数据库 建proxyed,gencase 两张表         

**系统运行**

手动测试准备： 

           1. 修改 record.py 中的 live.kuaishou.com/rest/ 为你需要测试的应用中的服务器url 
               def response(flow):
                    response =flow.response
                    if 'live.kuaishou.com/rest/' in flow.request.url:
                    
           2- python3  runproxy.py ， 在8888 端口上启动http/https 代理 
           3- 设置web/app请求代理后，设置mitmproxy 代理方法请参考：  https://www.jianshu.com/p/0cc558a8d6a2

手动测试并且记录请求： 
           手动测试web和app应用。 系统会在后台记录请求。

生成测试用例：python3 gencase.py

运行测试用例：python3  runcase.py 


 

**程序结构：**

    record.py  **记录**对服务器的请求，包括header,url , method,cookie,data 
    gencase.py 根据记录的请求参数的类型，为每个参数生成不同的数据值，组合为测试用例。
               目前支持的请求数据有 form-data, json, plaintext， 
               函数分别在：gencase_formdata(data)， gencase_json(jsondict)，gencase_query(data)
    runcase.py **运行测试用例** 取出产生的测试用例，生成服务器请求，向服务器发送请求。
    mylib.py   测试用例保存在mysql 数据库中，提供接口函数进行测试用例的存取 
    testcaselib.py **测试用例生成策略**代码
    
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
 


**问题反馈**   914529035@qq.com
      
**License**
This library is distributed under the GPL license .




    
    
