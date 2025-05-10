from django.db import models

class NatoMember(models.Model):
    country_name = models.CharField(max_length=100, unique=True)
    join_date = models.DateField()
    population = models.IntegerField()
    is_active = models.BooleanField(default=True)
    bio = models.TextField(default='')


    def __str__(self):
        return self.country_name + ' ' + str(self.population) + self.bio

    class Meta:
        db_table = 'NatoMember'


