import operator as op
import json

class Compare:
    def str_cmp(self,expect,result):
        if expect in result:
            return True
        else:
            return False

    def dict_cmp(self,expect,result):
        '''
        字典的完整比较
        :param expect:
        :param result:
        :return:
        '''
        if op.eq(expect,result):
            return True
        else:
            return False

    def dict_partial_cmp(self,expect,result):
        '''
        字典的部分比较
        :param expect:
        :param result:
        :return:
        '''
        for key,value in expect.items():
            if key in result and value == result[key]:
                return True
            else:
                return False

    def compare(self,expect,result):
        if "{" not in expect:
            return self.str_cmp(expect,result)
        else:
            expect = json.loads(expect)
            return self.dict_partial_cmp(expect,result)

if __name__ == "__main__":
    a = "a"
    b = {"a":1,"b":2}
    c = Compare()
    r = c.compare(a,b)
    print(r)
