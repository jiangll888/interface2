from util import opera_db
from config import settings
from util.opera_db import OperationDB
import json

class DataConfig:

    def __init__(self,data):
        self.db_data = data
        self.op_db = OperationDB()

    def get_case_id(self):
        return self.db_data and self.db_data[settings.CASE_ID]

    def get_case_name(self):
        return self.db_data and self.db_data[settings.CASE_NAME]

    def get_url(self):
        return self.db_data and self.db_data[settings.URL]

    def get_method(self):
        return self.db_data and self.db_data[settings.METHOD]

    def get_header_info(self):
        return self.db_data and self.db_data[settings.HEADER_INFO]

    def is_write(self):
        header_info = self.get_header_info()
        header_info = json.loads(header_info)
        if header_info and settings.IS_WRITE in header_info:
            return header_info[settings.IS_WRITE]
        else:
            return None

    def has_cookie(self):
        header_info = self.get_header_info()
        header_info = json.loads(header_info)
        if header_info and settings.COOKIE in header_info:
            return header_info[settings.COOKIE]
        else:
            return None

    def get_header(self):
        header_info = self.get_header_info()
        header_info = json.loads(header_info)
        if header_info and settings.HEADER in header_info:
            return header_info[settings.HEADER]
        else:
            return None

    def get_params(self):
        return self.db_data and self.db_data[settings.PARAMS]

    def get_is_run(self):
        return self.db_data and self.db_data[settings.IS_RUN]

    def get_depend_case_id(self):
        return self.db_data and self.db_data[settings.DEPEND_CASE_ID]

    def get_depend_request_field(self):
        return self.db_data and self.db_data[settings.DEPEND_REQUEST_FIELD]

    def get_depend_response_field(self):
        return self.db_data and self.db_data[settings.DEPEND_RESPONSE_FIELD]

    def get_expext(self):
        return self.db_data and self.db_data[settings.EXPECT]

    def get_result(self):
        return self.db_data and self.db_data[settings.RESULT]

    def write_result(self,sql,param):
        self.op_db.sql_DML(sql,param)

if __name__ == "__main__":
    # d = {1:'a',3:4}
    # d = None
    # r = d and d[1]
    # print(r)
    # print(settings.CASE_ID)
    db = OperationDB()
    sql = "select * from cases where case_id=%s"
    pa = ("qingguo_006",)
    data = db.search_one(sql,pa)
    print(type(data))
    d = DataConfig(data)
    #r = d.get_header_info()
    r = d.get_depend_response_field()
    print(r)
    sql1 = "update cases set result=%s where case_id=%s"
    para1 = ("pass","qingguo_login")
    d.write_result(sql1,para1)