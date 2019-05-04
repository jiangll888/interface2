from base.send_request import SendRequest
from config.dataconfig import DataConfig
from base.opera_cookie import OperaCookie
from base.depend_data import DependData
import json

class SendMain:
    def __init__(self,data):
        self.data = data
        self.get_field()

    def get_field(self):
        dc = DataConfig(self.data)
        self.case_id = dc.get_case_id()
        self.url = dc.get_url()
        self.method = dc.get_method()
        self.is_write = dc.is_write()
        self.is_run = dc.get_is_run()
        self.has_cookie = dc.has_cookie()
        self.header = dc.get_header()
        self.request_data = dc.get_params()
        self.depend_case_id = dc.get_depend_case_id()
        self.expect = dc.get_expext()
        self.result = dc.get_result()

    def run_main(self):
        sr = SendRequest()
        oc = OperaCookie()
        dd = DependData(self.data)
        if self.is_run:
            self.request_data = dd.handle_depend_data()
            if self.has_cookie:
                cookie = oc.get_cookie()
                res = sr.send_request(self.method,self.url,self.request_data,self.header,cookie)
            else:
                res = sr.send_request(self.method, self.url, self.request_data, self.header)
            if self.is_write:
                oc.write_cookie(res)
            return res.json()

if __name__ == "__main__":
    #data = {'case_id': 'qingguo_login', 'case_name': '登录', 'url': 'http://study-perf.qa.netease.com/common/fgadmin/login', 'method': 'post', 'header_info': '{"is_write":"true","header":{"Content-Type": "application/json"}}', 'params': '{"phoneArea":"86","phoneNumber":"20000000000","password":"netease123"}', 'is_run': 1, 'depend_case_id': None, 'depend_request_field': None, 'depend_response_field': None, 'expect': "{'message': 'success', 'code': 200}", 'result': 'pass'}
    data = {'case_id': 'qingguo_skulist_with_goodsid', 'case_name': '商品详情', 'url': 'http://study-perf.qa.netease.com/common/skuList', 'method': 'get', 'header_info': '{"header":{"Content-Type": "application/json"}}', 'params': {"goodsId":1}, 'is_run': 1, 'depend_case_id': None, 'depend_request_field': None, 'depend_response_field': None, 'expect': '"message":"success"', 'result': None}
    s = SendMain(data)
    r = s.run_main()
    print(r)
