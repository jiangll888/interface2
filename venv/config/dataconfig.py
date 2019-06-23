from util import opera_db
from config import settings
from util.opera_db import OperationDB
import json
from base.opera_token import OperaToken
from util.read_ini import ReadIni

class DataConfig:

    def __init__(self,data):
        self.db_data = data
        self.op_db = OperationDB()
        self.read_i = ReadIni()

    def get_case_id(self):
        return self.db_data and self.db_data[settings.CASE_ID]

    def get_case_name(self):
        return self.db_data and self.db_data[settings.CASE_NAME]

    def get_url(self):
        if self.db_data:
            url =  self.db_data[settings.URL]
            base_url = self.read_i.get_value("base_url","url")
            #如果用例里没写base_url才加上
            if base_url not in url:
                url = base_url + url
        return url

    def get_method(self):
        return self.db_data and self.db_data[settings.METHOD]

    def get_header_info(self):
        if self.db_data and not self.db_data[settings.HEADER_INFO]:
            return settings.URL_ENCODE
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
        if header_info:
            if not (settings.HEADER in header_info or
                settings.IS_WRITE in header_info or
                settings.COOKIE in header_info):
                header = header_info
            elif settings.HEADER in header_info:
                header = header_info[settings.HEADER]
            if settings.TOKEN in header:
                ot = OperaToken()
                header[settings.TOKEN] = ot.get_token()
            return header
        else:
            return None

    def get_params(self):
        return self.db_data and self.db_data[settings.PARAMS] and json.loads(self.db_data[settings.PARAMS])

    def get_data(self):
        params = self.get_params()
        if params:
            if not (settings.PARAM in params or
                    settings.FILE in params or
                    settings.DATA in params):
                data = params
            elif settings.DATA in params:
                data = params[settings.DATA]
            return data
        else:
            return None


    def get_param(self):
        params = self.get_params()
        if params and settings.PARAM in params:
            return params[settings.PARAM]
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
        if self.db_data:
            post_action = self.db_data[settings.POST_ACTION]
            if post_action:
                post_action_list = post_action.split("|")
                # for i,post_action in post_action_list:
                #     if "case_id" in post_action:
                #         post_action_list[i] = post_action.split("case_id=")[1]
            return post_action_list
        return None

    def get_post_params(self):
        if self.db_data:
            post_params = self.db_data[settings.POST_PARAMS]
            if post_params:
                post_params_list = post_params.split("|")
                for i,post_params in enumerate(post_params_list):
                    if "{" in post_params:
                        if "##" in post_params:
                            post_params_list[i] = self.replace_rand_param(json.loads(post_params))
                        else:
                            post_params_list[i] = json.loads(post_params)
                return post_params_list
        return None

    def replace_rand_param(self):
        pass

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
    r = d.get_header()
    print(r,type(r))