# _*_coding:utf8 _*_
import pymysql,json

conn = pymysql.connect('test.kakahui.net','testuser','test@cdELk3','smart_crm')

cur = conn.cursor()


cur.execute("SELECT * FROM t_live_entry_record WHERE class_id = 343097086064959911")
while True:
    res = cur.fetchone()
    if res is None:
        break #表示已完结
    print(type(res))
    #r = json.dumps(res)
    print(res)