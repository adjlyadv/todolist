from django.db import models



class Todolist(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_introduction = models.TextField(max_length=300,blank=False,default=' ')
    task_isfinshed = models.BooleanField(default = False)
    task_createtime = models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ('-task_createtime',)