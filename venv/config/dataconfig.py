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
        return self.db_data and settings.BASE_URL + self.db_data[settings.URL]

    def get_method(self):
        return self.db_data and self.db_data[settings.METHOD]

    def get_header_info(self):
        return self.db_data and self.db_data[settings.HEADER_INFO] and json.loads(self.db_data[settings.HEADER_INFO])

    def is_write(self):
        header_info = self.get_header_info()
        if header_info and settings.IS_WRITE in header_info:
            return header_info[settings.IS_WRITE]
        else:
            return None

    def has_cookie(self):
        header_info = self.get_header_info()
        if header_info and settings.COOKIE in header_info:
            return header_info[settings.COOKIE]
        else:
            return None

    def get_header(self):
        header_info = self.get_header_info()
        if header_info and settings.HEADER in header_info:
            return header_info[settings.HEADER]
        else:
            return None

    def get_params(self):
        return self.db_data and self.db_data[settings.PARAMS] and json.loads(self.db_data[settings.PARAMS])

    def get_param(self):
        params = self.get_params()
        if params and settings.PARAM in params:
            return json.dumps(params[settings.PARAM])
        else:
            return None

    def get_data(self):
        params = self.get_params()
        if params and settings.DATA in params:
            return params[settings.DATA]
        else:
            return None

    def get_file(self):
        params = self.get_params()
        if params and settings.FILE in params:
            return json.dumps(params[settings.FILE])
        else:
            return None

    def get_is_run(self):
        return self.db_data and self.db_data[settings.IS_RUN]

    def get_depend_case_id(self):
        return self.db_data and self.db_data[settings.DEPEND_CASE_ID]

    def get_depend_request_field(self):
        return self.db_data and self.db_data[settings.DEPEND_REQUEST_FIELD]

    def get_depend_response_field(self):
        return self.db_data and self.db_data[settings.DEPEND_RESPONSE_FIELD]

    def get_post_action(self):
        return self.db_data and self.db_data[settings.POST_ACTION]

    def get_expext(self):
        return self.db_data and self.db_data[settings.EXPECT]

    def get_expect_for_db(self):
        expect = self.get_expext()
        if expect and "{" in expect:
            expect = json.loads(expect)
            if settings.EXPECT_SQL in expect:
                sql = expect[settings.EXPECT_SQL]
                expect = self.op_db.search_one(sql)
        return expect

    def get_result(self):
        return self.db_data and self.db_data[settings.RESULT]

    def write_result(self,sql,param):
        self.op_db.sql_DML(sql,param)

if __name__ == "__main__":
    db = OperationDB()
    sql = "select * from cases where case_id=%s"
    pa = ("qingguo_001",)
    data = db.search_one(sql,pa)
    d = DataConfig(data)
    r = d.get_data()
    print(r,type(r))