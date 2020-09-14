from django.db import models

# Create your models here.
class Home(models.Model):
    search=models.CharField(max_length=100)
#to gove the name of search instaed of home.object
    created=models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'searched this {} at {}'.format(self.search,self.created)


    '''to change the name of table in admin page'''    
    class Meta:
        verbose_name_plural = "homies"