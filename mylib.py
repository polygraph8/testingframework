# -*- coding=utf-8 -*-
import pymysql.cursors
import re

from warnings import filterwarnings
import hashlib
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
            self.cursor.execute(query)
            insert_id= self.connect.insert_id()
            self.connect.commit()
            label = True
        except Exception as e:
            print(e)
        except pymysql.Warning as e:
            print(e)
        finally:
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

            results = self.cursor.fetchall()

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

        sql= "insert into gencase(host,url,method,cookie,headers,data,datamd5,response_header,response_cookie,response_text,response_status_code) values('%s','%s','%s','%s',\"%s\",'%s','%s',\"%s\",'%s','%s','%s')" %  \
                                (host, url, method, cookie, headers, data, datamd5, response_header, response_cookie, response_text, response_status_code)

        self.myquery(sql)

    def myselect_case(self,  url_pattern="", limit_num=0 ,table="proxyed",fields="host, url, method, cookie,headers, data"):

        sql=""
        if url_pattern == "":
            sql = "select %s from %s "  % (fields,table)
        else:
            sql = "select "+fields+" from "+table+" where url like '%"+url_pattern+"%'"

        if limit_num > 0 :
            sql = sql +"limit " + str(limit_num)
        result,fields = self.myselect(sql)
        return result







