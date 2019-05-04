import requests
import json

class SendRequest:

    def send_get(self,url,data=None,header=None,cookie=None):
        if data:
            data = json.loads(data)
        if cookie and header:
            res = requests.get(url=url,params=data,headers=header,cookies=cookie)
        elif cookie and not header:
            res = requests.get(url=url,params=data,cookies=cookie)
        elif not cookie and header:
            res = requests.get(url=url,params=data,cookies=cookie)
        else:
            res = requests.get(url=url,params=data)
        return res

    def send_post(self,url,data,header=None,cookie=None):
        #解决请求中有中文之后截断的问题
        data = data.encode(encoding="utf-8")
        if cookie and header:
            res = requests.post(url=url,data=data,headers=header,cookies=cookie)
        elif cookie and not header:
            res = requests.post(url=url,data=data,cookies=cookie)
        elif not cookie and header:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res

    def send_put(self,url,data,header=None,cookie=None):
        # 解决请求中有中文之后截断的问题
        data = data.encode(encoding="utf-8")
        if cookie and header:
            res = requests.put(url=url,data=data,headers=header,cookies=cookie)
        elif cookie and not header:
            res = requests.put(url=url,data=data,cookies=cookie)
        elif not cookie and header:
            res = requests.put(url=url,data=data,headers=header)
        else:
            res = requests.put(url=url,data=data)
        return res

    def send_delete(self,url,data,header=None,cookie=None):
        # 解决请求中有中文之后截断的问题
        data = data.encode(encoding="utf-8")
        if cookie and header:
            res = requests.delete(url=url,data=data,headers=header,cookies=cookie)
        elif cookie and not header:
            res = requests.delete(url=url,data=data,cookies=cookie)
        elif not cookie and header:
            res = requests.delete(url=url,data=data,headers=header)
        else:
            res = requests.delete(url=url,data=data)
        return res

    def send_request(self,method,url,data=None,header=None,cookie=None):
        if method.lower() == "get":
            res = self.send_get(url=url,data=data,header=header,cookie=cookie)
        elif method.lower() == "post":
            res = self.send_post(url=url,data=data,header=header,cookie=cookie)
        elif method.lower() == "put":
            res = self.send_put(url=url,data=data,header=header,cookie=cookie)
        else:
            res = self.send_delete(url=url,data=data,header=header,cookie=cookie)
        return res

if __name__ == "__main__":
    s = SendRequest()
    #url = "http://study-perf.qa.netease.com/common/skuList"
    #data = {"goodsId":1}
    url = "http://study-perf.qa.netease.com/common/fgadmin/login"
    data = {
        "phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"
    }
    data = json.dumps(data)
    header = {
        "content-type":"application/json"
    }
    r = s.send_request("post",url,data,header)
    print(r.json())
    print(r.cookies)

