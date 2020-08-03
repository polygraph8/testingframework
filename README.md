# testingframework， 测试自动化框架
A light Testng framework  base on python , for web testing ,android/IOS app testing and testing for service interface.  


设计目标:   
    希望在手动测试和自动化测试中建立一个桥梁，利用手动测试产生的结果，来自动生成测试用例。
 
设计思路：
    模拟appscan ,      
        通过监控手动测试的结果，我们可以对手动测试的结果进行分析，得到请求的条件以及返回的结果。
        
        通过泛化请求条件，例如：边界值，等价值,安全测试等，我们可以自动生成更多的测试用例。
        
        通过测试用例的改变，我们可以得到返回结果，以及预期的结果，以及判断对错。
        
        可以通过这个结果，我们可以进行无差别压力测试

    可以集成： 
         基于python的性能测试工具–locust





    
    
