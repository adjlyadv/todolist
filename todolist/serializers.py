from rest_framework import serializers
from models import Todolist




class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model =Todolist
        fields = ("task_id",'task_introduction','task_createtime','task_isfinshed')