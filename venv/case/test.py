import json
import re
# with open("./gl.json","a") as fp:
#     json.dump({"test":"a"},fp)
# with open("./gl.json","a") as fp:
#     json.dump({"test1":"a"},fp)
# with open("./gl.json") as fp:
#     print(json.load(fp))
# global
# gl1.test = "a"
# print(gl1.test)
a = "http://study-perf.qa.netease.com/common/fgadmin/login"
r=re.search(r'^https?://(\d{1,3}.){3}\d{1,3}:\d{1,5}|^https?://.*com/',a)
print(r)
print (r[0])