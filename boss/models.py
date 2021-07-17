from django.db import models

# Create your models here.

class BossTable (models.Model):
    boss_name = models.CharField(max_length=50)
    boss_password = models.CharField(max_length=50)

    def __str__(self): 
        return self.boss_name


class CustomerQuery (models.Model):
    customer_email = models.EmailField(max_length=254)
    customer_query = models.TextField()
    query_status = models.IntegerField(default=1)

    def __str__(self):
        return self.customer_email


 