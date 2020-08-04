# -*- coding=utf-8 -*-
import pymysql.cursors
import re

from warnings import filterwarnings
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
            self.cursor .execute(query)
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
 #       print("the query results is: %s" % (results,))
        return results, fields

