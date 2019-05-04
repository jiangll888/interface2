import pymysql
from functools import wraps

class OperaDB:
    def __init__(self,host,username,passwd,database,charset="utf8"):
        self.conn = self.get_conn(host,username,passwd,database,charset)

    def get_conn(self,host,username,passwd,database,charset):
        try:
            conn = pymysql.connect(
                host=host,
                user=username,
                password=passwd,
                database=database,
                use_unicode=True,
                charset=charset,
                cursorclass=pymysql.cursors.DictCursor
            )
            return conn
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0],e.args[1]))
            return None

    def decorator(func):
        @wraps(func)
        def wrapper(self,*args,**kwargs):
            try:
                if self.conn:
                    with self.conn.cursor() as cur:
                        cur.execute(*args,**kwargs)
                        return func(self,cur)
            except pymysql.Error as e:
                print(e.args[0],e.args[1])
                self.conn.rollback()
                return None
        return wrapper

    @decorator
    def get_one(self,cur):
        '''
        获取1条，不指定的时候则是默认获取第一条
        :param cur:
        :return:
        '''
        return cur.fetchone()

    @decorator
    def get_all(self,cur):
        return cur.fetchall()

    @decorator
    def dml(self,cur=None):
        self.conn.commit()

if __name__ == "__main__":
    op = OperaDB("127.0.0.1","root","122901","testing")
    #sql = "select * from students where id=%(id)s;"
    sql = "select * from `cases` where `case_id`=%(id)s;"
    #sql = "insert into students(name,nickname,sex,in_time) values('te','tee','女','2019-03-20 15:23:23')"
    res = op.get_one(query=sql,args={"id":"qingguo_006"})
    #op.dml(sql)
    #res = op.get_o("select * from students;")
    print(res)



