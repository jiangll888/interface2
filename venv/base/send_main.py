from base.send_request import SendRequest
from config.dataconfig import DataConfig
from base.opera_cookie import OperaCookie
from base.depend_data import DependData
from util.opera_db import OperationDB
from util.compare import Compare
import json
import threading
from config import settings

class SendMain:
    _instance_lock = threading.Lock()

    def __init__(self,data):
        self.data = data
        self.get_field()

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

    def get_field(self):
        dc = DataConfig(self.data)
        self.case_id = dc.get_case_id()
        self.url = dc.get_url()
        self.method = dc.get_method()
        self.is_write = dc.is_write()
        self.is_run = dc.get_is_run()
        self.has_cookie = dc.has_cookie()
        self.header = dc.get_header()
        self.request_param = dc.get_param()
        self.request_data = dc.get_data()
        self.request_file = dc.get_file()
        self.depend_case_id = dc.get_depend_case_id()
        self.expect = dc.get_expect_for_db()
        self.post_action = dc.get_post_action()
        
    def run_main(self):
        sr = SendRequest()
        oc = OperaCookie()
        dd = DependData(self.data)
        if self.is_run:
            if self.depend_case_id:
                self.request_data = dd.replace_request_data()
            if self.has_cookie:
                cookie = oc.get_cookie()
                res = sr.send_request(self.method,self.url,self.request_data,self.request_file,self.request_param,self.header,cookie)
            else:
                res = sr.send_request(self.method, self.url, self.request_data,self.request_file,self.request_param, self.header)
            if self.is_write:
                oc.write_cookie(res)
            cmp = Compare()
            r = cmp.compare(self.expect, res.json())
            self.write_res(r)
            return r

    def write_res(self,res):
        dc = DataConfig(self.data)
        sql = settings.UPDATE_RESULT_SQL
        if res:
            para = ("pass", self.case_id)
        else:
            para = ("fail", self.case_id)
        dc.write_result(sql,para)

    def post_act(self):
        '''
        数据清理操作
        :return:
        '''
        if self.post_action:
            op_db = OperationDB()
            op_db.sql_DML(self.post_action)        #直接用sql语句做数据清理


if __name__ == "__main__":
    #data = {'case_id': 'qingguo_login', 'case_name': '登录', 'url': 'http://study-perf.qa.netease.com/common/fgadmin/login', 'method': 'post', 'header_info': '{"is_write":"true","header":{"Content-Type": "application/json"}}', 'params': '{"phoneArea":"86","phoneNumber":"20000000000","password":"netease123"}', 'is_run': 1, 'depend_case_id': None, 'depend_request_field': None, 'depend_response_field': None, 'expect': "{'message': 'success', 'code': 200}", 'result': 'pass'}
    data = {'case_id': 'qingguo_skulist_with_goodsid', 'case_name': '商品详情', 'url': 'http://study-perf.qa.netease.com/common/skuList', 'method': 'get', 'header_info': '{"header":{"Content-Type": "application/json"}}', 'params': {"goodsId":1}, 'is_run': 1, 'depend_case_id': None, 'depend_request_field': None, 'depend_response_field': None, 'expect': '"message":"success"', 'result': None}
    s = SendMain(data)
    r = s.run_main()
    print(r)
