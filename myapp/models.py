from django.db import models
from django.utils import timezone




class Genre(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    number = models.IntegerField(default=0)
    income =  models.IntegerField(default=10000000)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    #def __str__(self):
       # return self.year
    #sectionLink = models.URLField(blank=True, null=True)
   # def __str__(self):
   #     res = re.sub(r'\[|\]|<|>|"Section: "', "", self.name.capitalize())
      #  return res

    #def genLink(self):
       # return "http://localhost/" + self.name + "/"


class Actors(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    scifi = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    avgIncome = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Directors(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    scifi = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    avgIncome = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class ActorsVsDirectors(models.Model):
    actor = models.ForeignKey(Actors)
    director = models.ForeignKey(Directors)
    movieNum = models.IntegerField(default=0)
    income = models.IntegerField(default=100000)
    #id  = models.CharField(max_length=100, primary_key= True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()


