import unittest,ddt
from util.opera_db import OperaDB
from base.send_main import SendMain
from config import settings

op_db = OperaDB(settings.DB_HOST,settings.DB_USER,settings.DB_PASSWD,settings.DB_NAME)
sql = "select * from cases;"
data = op_db.get_all(sql)

@ddt.ddt
class RunCase(unittest.TestCase):
    @ddt.data(*data)

    @ddt.unpack
    def test01(self,*args,**kwargs):
        sm = SendMain(kwargs)
        res = sm.run_main()
        #print(res)

if __name__ == "__main__":
    unittest.main()
