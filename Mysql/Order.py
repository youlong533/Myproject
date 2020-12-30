from Myproject.Mysql import MySQL



def search_class():
    class_id = int(input('请输入班级id:'))
    sql_t1 = 'SELECT * FROM t_live_class WHERE id = %s;' %class_id
    db = 'smart_crm'
    res = MySQL.Ex_mysql.ex_mysql(db,sql_t1)
    print(res)

search_class()