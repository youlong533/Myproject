# _*_coding:utf8 _*_
import pymysql

class Ex_mysql:

    def ex_mysql(db,sql):
        conn = pymysql.connect(
            host='test.kakahui.net',
            port=3306,
            user='testuser',
            passwd='test@cdELk3',
            db=db,
            charset='utf8')#测试环境
        # conn = pymysql.connect(
        #     host='tbj.kakahui.net',
        #     port=13311,
        #     user='youlong_reader',
        #     passwd='abc@123',
        #     db=db,
        #     charset='utf8')#生成环境
        cur = conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            raise e
        else:
            res = cur.fetchall()
            cur.close()
            return res

    def sort_sql_results(db,sql):
        results = Ex_mysql.ex_mysql(db,sql)
        for i in results:
            print(i)





if __name__ == '__main__':
    datebase = 'smart_crm'
    sql_text = 'select * from t_customer;'
    Ex_mysql.sort_sql_results(datebase, sql_text)
    # r=Ex_mysql.ex_mysql(datebase,sql_text)
    # print(r)
