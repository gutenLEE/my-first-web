from django.db import models
from djongo import models
import pymongo
# the bridge between your database and server.
from pymongo import MongoClient
from bson import ObjectId


class test_db(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField(default=10, null=True)
    roll_number = models.CharField(max_length=20, null=True)

    city = models.CharField(max_length=20, null=True)
    gu = models.CharField(max_length=20, null=True)
    dong = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


