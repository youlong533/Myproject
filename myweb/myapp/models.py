from django.db import models

# Create your models here.
class Case(models.Model):
    '''自定义Stu表对应的Model类'''
    #定义属性：默认主键自增id字段可不写
    id = models.AutoField("编号",primary_key=True)
    name = models.CharField("模块",max_length=16)
    url = models.CharField("URL",max_length=1000)
    run = models.CharField("是否运行",max_length=3)
    req=models.CharField("请求类型",max_length=8)

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%s:%s:%s"%(self.id,self.name,self.url,self.run,self.req)

    # 自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table="case"
        verbose_name = '测试用例'
        verbose_name_plural = '测试用例'