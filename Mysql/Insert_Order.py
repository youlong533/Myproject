from Myproject.Mysql import MySQL

def search_class():
    database = 'knowledge'
    i = 1
    while i <1001:
        sql_text = "INSERT INTO `knowledge`.`t_customer_pay_order`(`id`, `product_code`, `customer_id`, `order_price`, `pay_amount`, `total_pay_amount`, `total_refund_amount`, `order_number`, `third_order_number`, `source_class_id`, `link_class_id`, `source_parent_id`, `package_id`, `pay_recommend`, `status`, `pay_type`, `is_live`, `app_id`, `mer_id`, `pay_method`, `pay_mode`, `pay_source`, `mobile`, `finished_time`, `order_scene`, `market_source`, `created_time`, `modified_time`, `operator_id`, `remark`) VALUES ('2408982398557491333'+%i, '200', '2607459007241392158'+%i, 1, 1, 0, 1, '2208982398553297028'+%i, '4200000358201907319045823568'+%i, '398875596192801339', '398875596192801339', NULL, '319933823424135170', NULL, 2, 1, b'1', 'wx91804ccd6aa71de2', '1492255782', 1, 1, NULL, NULL, '2021-01-31 16:21:38', NULL, NULL, '2021-01-31 16:21:27', '2021-01-31 17:39:56', 0, test);" % (i,i,i,i)
        MySQL.Ex_mysql.sort_sql_results(database,sql_text)

search_class()
