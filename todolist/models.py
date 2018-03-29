from django.db import models



class Todolist(models.Model):
    id = models.AutoField(primary_key=True)
    text= models.TextField(max_length=300,blank=False,default=' ')
    completed = models.BooleanField(default = False)
    create= models.DateTimeField(auto_now_add=True)
    class Meta:
       ordering = ('-create',)