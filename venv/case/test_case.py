import unittest,ddt
from util.opera_db import OperationDB
from base.send_main import SendMain
from config import settings

op_db = OperationDB()
sql = "select * from cases;"
data = op_db.search_all(sql)

@ddt.ddt
class RunCase(unittest.TestCase):
    @ddt.data(*data)

    @ddt.unpack
    def test01(self,*args,**kwargs):
        sm = SendMain(kwargs)
        res = sm.run_main()
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()
