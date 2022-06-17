from django.db import models


# Create your models here.
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name
