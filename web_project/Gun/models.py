from django.db import models

class Gun(models.Model):
    gunName = models.TextField()
    quote = models.TextField()
    type = models.TextField()
    DPS = models.TextField()
    mag = models.TextField()
    ammo = models.TextField()
    rate = models.TextField()
    reload = models.TextField()
    shotspd = models.TextField()
    range = models.TextField()
    force = models.TextField()
    spread = models.TextField()

    def __str__(self):
        """returns a string repre of a gun"""
        return f"'{self.gunName}' '{self.quote}' '{self.type}' '{self.DPS}' '{self.ammo}'"

# Create your models here.
'''
With Django, your work with your database almost exclusively through the models you define in code. 
Django's "migrations" then handle all the details of the underlying database automatically as you evolve the models over time. The general workflow is as follows:

Make changes to the models in your models.py file.
Run python manage.py makemigrations to generate scripts in the migrations folder that migrate the database from its current state to the new state.
Run python manage.py migrate to apply the scripts to the actual database.
The migration scripts effectively record all the incremental changes you make to your data models over time. 
By applying the migrations, Django updates the database to match your models. Because each incremental change has its own script, 
Django can automatically migrate any previous version of a database (including a new database) to the current version. 
As a result, you need concern yourself only with your models in models.py, never with the underlying database schema or the migration scripts. You let Django do that part!
'''