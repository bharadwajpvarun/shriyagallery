from django.db import models

class imagecount(models.Model):
 n=models.IntegerField(null=True)


def __str__(self):
	return self.n