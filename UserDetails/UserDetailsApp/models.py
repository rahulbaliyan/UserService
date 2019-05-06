from djongo import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    age = models.IntegerField()
    state = models.CharField(max_length=128)
    zip = models.IntegerField()
    email = models.EmailField(max_length=128)
    objects = models.DjongoManager()