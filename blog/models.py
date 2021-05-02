from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=150)


    def __str__(self):
        return self.title
    
    
    
# One-to-many, one-to-one, and many-to-many relationships
# There are three types of foreign key relationships. The first, one-to-many, is what we have 
# with the customers and orders tables. One customer can place multiple orders. By using the 
# customer primary key as our foreign key in the orders table, we can keep track of this.

# An example of a one-to-one relationship would be a database tracking people and passports. 
# Each person can only have one passport, and vice versa, so those two tables would have 
# a one-to-one relationship.

# The third option is known as a many-to-many relationship. Let's imagine we have a database 
# tracking authors and books. Each author can write multiple books and each book can have 
# multiple authors. By defining a many-to-many relationship via foreign keys, we can link 
# these two tables together.



class University(models.Model):
    UNIVERSITY_TYPE = ( # new
        ('PUBLIC', 'A public university'),
        ('PRIVATE', 'A private university')
    )

    full_name = models.CharField(
        verbose_name='university full name',
    max_length=100
    )
    university = models.CharField( # new
        choices=UNIVERSITY_TYPE,
        max_length=12,
        verbose_name='type of university',
    )
