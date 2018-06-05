from django.db import models
from django.contrib.auth.models import User


class query_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_text = models.TextField(max_length=500)
    lang = models.CharField(max_length=10)
    count = models.CharField(max_length=3)
    from_data = models.CharField(max_length=12)
    to_data = models.CharField(max_length=12)

class query_data_analyse(models.Model):
    query_data = models.ForeignKey(query_data, on_delete=models.CASCADE)
    count = models.CharField(max_length=3)
    uni_count = models.CharField(max_length=3)
    rt_count = models.CharField(max_length=3)