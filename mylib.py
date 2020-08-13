# -*- coding=utf-8 -*-
import pymysql.cursors
import re

from warnings import filterwarnings
import hashlib
from testcaselib import *
filterwarnings("error",category=pymysql.Warning)  #  指定过滤告警的类别为 pymysql.Warning类，


class myMySQL():
    def __init__(self,dbname="test"): #初始化
        # 连接数据库
        try:
            self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db= dbname ,  # 数据库名
            user='root',  # 数据库用户名
            passwd='',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
            self.cursor  = self.connect.cursor();
            self.myquery("set names utf8;")
            #  create database TEST DEFAULT CHARACTER SET utf8;    建表时采用这个方法，则可以避免UTF-8 字符存不进去。

        except Exception as e:
            print(e)
            raise e
        # 通过cursor执行增删查改

    def setdictcursor(self): #初始化
            self.cursor  = self.connect.cursor(cursor=pymysql.cursors.DictCursor)


    def __del__(self): # 析构
        self.connect.close()



    def myquery(self, query):
        label = False
        insert_id= -1
        try:
 #           print("insert sql is : %s" % (query,))
            self.cursor.execute(query)
            insert_id= self.connect.insert_id()
            self.connect.commit()
            label = True
        except Exception as e:
 #           self.connect.rollback()
            print(e)
 #           raise e
        except pymysql.Warning as e:
            print(e)

        finally:
 #           self.cursor.close()
            return insert_id

    def myselectone(self, query):
            results = None
            print("the query is: %s" % (query,))
            try:
                self.cursor.execute(query)
                results = self.cursor.fetchone()
            except Exception as e:
                print(e)
                raise e
            #       self.cursor.close()
            print("the query results is: %s" % (results,))
            return results

    def myselect(self, query):
        results = None
#        print("the query is: %s" % (query,))
        fields = []
        try:
            self.cursor.execute(query)
            columns = self.cursor.description
            for i in range(len(columns)):
                fields.append(columns[i][0])

#            print(columns[0])
#            print(columns[0][0])

 #           c = cursor.execute("SHOW FULL COLUMNS FROM users FROM blog")
            results = self.cursor.fetchall()
 #           results = self.cursor.fetchmany()

        except Exception as e:
            print(e)
            raise e
        except pymysql.Warning as e:
            print(e)
        #       self.cursor.close()
        print("the query results is: %s" % (results,))
        return results, fields

    def myinsert_proxyed(self,host="",url="",method="",cookie="1",headers="2",data="3",response_header="4",response_cookie="5",response_text="6",response_status_code="7"):
        m= hashlib.md5()
        m.update(data.encode("utf-8"))
        datamd5 = m.hexdigest()

        sql= "insert into proxyed(host,url,method,cookie,headers,data,datamd5,response_header,response_cookie,response_text,response_status_code) values('%s','%s','%s','%s',\"%s\",'%s','%s',\"%s\",'%s','%s','%s')" %  \
                                (host, url, method, cookie, headers, data, datamd5, response_header, response_cookie, response_text, response_status_code)
        self.myquery(sql)
        return sql

    def myinsert_gencase(self,host="",url="",method="",cookie="1",headers="2",data="3",response_header="4",response_cookie="5",response_text="6",response_status_code="7"):
        m= hashlib.md5()
        m.update(data.encode("utf-8"))
        datamd5 = m.hexdigest()

        sql= "insert into gencase(host,url,method,cookie,headers,data,datamd5,response_header,response_cookie,response_text,response_status_code) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %  \
                                (host, url, method, cookie, headers, data, datamd5, response_header, response_cookie, response_text, response_status_code)

        self.myquery(sql)
    def myselect_proxyed(self, url_pattern="", limit_num=0 ):
        fields= "host, url, method, cookie, headers, data"
        sql=""
        if url_pattern == "":
            sql = "select %s from proxyed "  % (fields)
        else:
            sql = "select "+fields+" from proxyed where url like '%"+url_pattern+"%'"

        if limit_num > 0 :
            sql = sql +"limit " + str(limit_num)
        result,fields = self.myselect(sql)
        return result







def gen_testcase(db,req):
    host, url, method, cookie, headers, data = req
#    print(url)
    gendata_array = []
    if "{" in data:
        print("data  is json:"+ data)
        jsondict = json.loads(data)
        gendict_array = gencase_json(jsondict)
        for d in gendict_array:
            gendata_array.append(json.dumps(d))

    if "=" in data:
        print("data is query:"+ data)
        gendata_array = gencase_query(data)
    for gendata in gendata_array:
        db.myinsert_gencase(host, url, method, cookie, headers, gendata)

def test_testcase():
    data = '{"a":1,"b":1,"name":"123"}'
    jsondict = json.loads(data)
    gendict_array = gencase_json(jsondict)
    print(gendict_array)
    print(len(gendict_array))

    gendata = []
    for d in gendict_array:
        gendata.append(json.dumps(d))
    print(gendata)
    exit(0)


if __name__ == '__main__':
#     arr = gencase_query("wd=1&o=2&m=liujun")
#     print(arr)
#     print(len(arr))

    db=  myMySQL("test")
    db.myinsert_proxyed("www.baidu.com","http://www.baidu.com","GET")
    db.myinsert_proxyed("www.baidu.com", "http://www.baidu.com/s", "GET",data="wd=wd2021")
    db.myinsert_proxyed("www.baidu.com", "https://www.baidu.com/s", "GET",data="wd=wd2021&t=111")
    db.myinsert_proxyed("127.0.0.1", "http://127.0.0.1/post.php?baidu", "POST",data='{"id": 1, "sn":234 , "city": "beijing"}')

    results = db.myselect_proxyed("baidu",5)
    for  record in results:
         gen_testcase(db,record)

