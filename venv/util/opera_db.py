#coding:utf-8
import cx_Oracle
import pymysql
from config import  settings
import threading

class OperationDB:
    _instance_lock = threading.Lock()

    def __init__(self,db_type=settings.DB_TYPE,username=settings.DB_USER,passwd=settings.DB_PASSWD,host=settings.DB_HOST,port=settings.DB_PORT,ins_name=settings.DB_NAME):
        self.db_type = db_type
        if db_type == 'oracle':
            tns = cx_Oracle.makedsn(host,port,ins_name)
            self.db = cx_Oracle.connect(username,passwd,tns)
        else:
            # 创建数据库连接
            self.db = pymysql.connect(
                host = host,
                port = port,
                user = username,
                passwd = passwd,
                db = ins_name,
                charset = 'utf8',
                # 加上cursorclass之后就可以直接把字段名捞出来，和字段值组成键值对的形式
                cursorclass = pymysql.cursors.DictCursor
            )
        # 创建游标
        self.cur = self.db.cursor()

    def __new__(cls, *args, **kwargs):
        '''
        实现单例模式
        :param args:
        :param kwargs:
        :return:
        '''
        if not hasattr(cls,"_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super().__new__(cls)
        return cls._instance

    #获取一条数据
    def search_one(self,sql,param=None):
        self.cur.execute(sql,param)
        res = self.cur.fetchone()
        if self.db_type == 'oracle':
            res = self.makeDictFactory(*res)
        return res

    #获取所有数据
    def search_all(self,sql,param=None):
        self.cur.execute(sql,param)
        res = self.cur.fetchall()
        if self.db_type == 'oracle':
            res = self.makeDictFactory(*res)
        return res

    #新增/删除/更新数据
    def sql_DML(self,sql,param=None):
        try:
            self.cur.execute(sql,param)
            self.db.commit()
        except:
            self.db.rollback()

    #将返回的结果和字段名映射成字典
    def makeDictFactory(self,*args):
        columnNames = [d[0] for d in self.cur.description]
        if isinstance(args[0],list):
                return [dict(z) for z in [zip(columnNames,data) for data in args]]
        return dict(zip(columnNames,args))



    #关闭游标和数据库连接
    def close(self):
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    opera_db = OperationDB('mysql','root','122901','127.0.0.1',3306,'testing')
    res = opera_db.search_one("select result from `cases` where case_id='11';")
    # res = opera_db.search_one("select user_name,telphone,source,status from t_activity_order WHERE source='PAWH'" )
    print("111111111111")
    print(res)
    #print([r["result"] for r in res])
    # # res1 = opera_db.makeDictFactory(*res)
    # # print(type(res1))
    # opera_db.close()
    # a = ["col1","col2","col3"]
    # b = [[1,2,3],[4,5,6]]
    # r = [dict(z) for z in [(zip(a,data)) for data in b]]
    # print(r)
    s = "'1'"
    print(eval(s),type(eval(s)))
    print(None == None)