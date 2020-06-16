from django.db import models

# Create your models here.
# Python or Django creates the SQL commands needed for the database

class UserInput(models.Model):
    # creates the model needed for the database to setup and insert data into the table. The created table is called nst_UserInput and has an ID and the user input, in this case the paintings name
    paintings_name = models.CharField(max_length=300)
    # the length of the paintings name can be adjusted if it turns out to be too short