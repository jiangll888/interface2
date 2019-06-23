CASE_ID = "case_id"
CASE_NAME = "case_name"
URL = "url"
METHOD = "method"
HEADER_INFO = "header_info"
IS_WRITE = "is_write"
COOKIE = "cookie"
TOKEN = "token"
HEADER = "header"
PARAMS = "params"
PARAM = "param"
DATA = "data"
FILE = "file"
IS_RUN = "is_run"
DEPEND_CASE_ID = "depend_case_id"
DEPEND_REQUEST_FIELD = "depend_request_field"
DEPEND_RESPONSE_FIELD = "depend_response_field"
POST_ACTION = "post_action"
POST_PARAMS = "post_params"
EXPECT = "expect"
EXPECT_SQL = "SQL"
RESULT = "result"

DB_TYPE = "mysql"
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWD = "122901"
DB_PORT = 3306
DB_NAME = "testing"
TABLE_NAME = "`cases`"

BASE_URL = "http://study-perf.qa.netease.com"

URL_ENCODE = {"Content-Type":"application/x-www-form-urlencode"}
URL_RE = "^https?://(\d{1,3}.){3}\d{1,3}:\d{1,5}|^https?://.*com/"

TEST_CASE_SQL = "select * from {};".format(TABLE_NAME)
CLEAR_RESULT_SQL = "update {} set {}='';".format(TABLE_NAME,RESULT)
UPDATE_RESULT_SQL = "update {} set {}=%s where {}=%s;".format(TABLE_NAME,RESULT,CASE_ID)
LINE_DATA_SQL = "select * from {} where {}=%s;".format(TABLE_NAME,CASE_ID)
GET_RESULT_SQL = "select {}  from {};".format(RESULT,TABLE_NAME)

EMAIL_CONTENT = "本次接口自动化执行了{}个测试用例。\n" \
                "其中运行成功{}个，运行失败{}个\n"\
                "测试报告地址:{}\n"\
                "可在数据库中查看运行结果，数据库类型：{}，数据库地址：{}，用户名：{}，密码：{}，"\
                "数据库库名：{}，数据库表名：{}"

EMAIL_SUB = "接口自动化测试报告   {}"
EMAIL_RECEIVER = ["jiangliulin@163.com"]


