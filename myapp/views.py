from django.shortcuts import render
from django.http import HttpResponse
from  myapp.models import  Actors, Directors, ActorsVsDirectors, Genre
from .forms import getInfo
from .calc import success
from numpy import *


def showRes(request) :
    cast_num = 6
    genre_num = 2
    act_dir_movie = []                         #done
    act_dir_profit = []                        #done
    prev_year_movie_genre=[]          #done
    prev_year_avg_profit_genre=[] #done
    cast_profit = []                               #done
    cast_vs_genre = []                          #done
    year = 2016
   # if request.method == "post":
    infoForm = getInfo(request.POST)
    if infoForm.is_valid():
        director = infoForm.cleaned_data['director']
        director = director.lower()

        d = Directors.objects.get(name=director)
        dir_gross = d.avgIncome

        genre1 = infoForm.cleaned_data['genre1']
        genre1 = genre1.lower()

        #a = Movies.objects.get(year=year)
        a = Genre.objects.get(name=genre1)
        b = a.number
        prev_year_movie_genre.append(b)
        b  = a.income
        prev_year_avg_profit_genre.append(b)

        genre2 = infoForm.cleaned_data['genre2']
        genre2 = genre2.lower()

        if genre2 == "n/a":
            genre_num -= 1
        else:
            a = Genre.objects.get(name=genre2)
            b = a.number
            prev_year_movie_genre.append(b)
            b = a.income
            prev_year_avg_profit_genre.append(b)

        actor1 = infoForm.cleaned_data['actor1']
        actor1 = actor1.lower()

        a = Actors.objects.get(name=actor1)

        b = a.avgIncome
        cast_profit.append(b)
        t=0
        if genre1=="scifi" or genre2=="scifi":
            t+= a.scifi
        if genre1=="action" or genre2=="action":
            t+= a.scifi
        if genre1=="comedy" or genre2=="comedy":
            t+= a.scifi
        if genre1=="romance" or genre2=="romance":
            t+= a.scifi
        if genre1=="fantasy" or genre2=="fantasy":
            t+= a.scifi
        if genre1=="family" or genre2=="family":
            t+= a.scifi
        if genre1=="horror" or genre2=="horror":
            t+= a.scifi
        cast_vs_genre.append(t)
        a = ActorsVsDirectors.objects.get(actor=actor1,director=director)
        b = a.movieNum
        act_dir_movie.append(b)
        b = a.income
        act_dir_profit.append(b)

        actor2 = infoForm.cleaned_data['actor2']
        actor2 = actor2.lower()

        a = Actors.objects.get(name = actor2)
        b = a.avgIncome
        cast_profit.append(b)
        t = 0
        if genre1 == "scifi" or genre2 == "scifi":
            t += a.scifi
        if genre1 == "action" or genre2 == "action":
            t += a.scifi
        if genre1 == "comedy" or genre2 == "comedy":
            t += a.scifi
        if genre1 == "romance" or genre2 == "romance":
            t += a.scifi
        if genre1 == "fantasy" or genre2 == "fantasy":
            t += a.scifi
        if genre1 == "family" or genre2 == "family":
            t += a.scifi
        if genre1 == "horror" or genre2 == "horror":
            t += a.scifi
        cast_vs_genre.append(t)
        a = ActorsVsDirectors.objects.get(actor=actor2, director=director)
        b = a.movieNum
        act_dir_movie.append(b)
        b = a.income
        act_dir_profit.append(b)


        actor3 = infoForm.cleaned_data['actor3']
        actor3 = actor3.lower()

        if actor3=="n/a":
            cast_num -=1
        else:
            a = Actors.objects.get(name=actor3)
            b = a.avgIncome
            cast_profit.append(b)

            t = 0
            if genre1 == "scifi" or genre2 == "scifi":
                t += a.scifi
            if genre1 == "action" or genre2 == "action":
                t += a.scifi
            if genre1 == "comedy" or genre2 == "comedy":
                t += a.scifi
            if genre1 == "romance" or genre2 == "romance":
                t += a.scifi
            if genre1 == "fantasy" or genre2 == "fantasy":
                t += a.scifi
            if genre1 == "family" or genre2 == "family":
                t += a.scifi
            if genre1 == "horror" or genre2 == "horror":
                t += a.scifi
            cast_vs_genre.append(t)

            a = ActorsVsDirectors.objects.get(actor=actor3, director=director)
            b = a.movieNum
            act_dir_movie.append(b)
            b = a.income
            act_dir_profit.append(b)



        actor4 = infoForm.cleaned_data['actor4']
        actor4 = actor4.lower()

        if actor4 == "n/a":
            cast_num -= 1
        else:
            a = Actors.objects.get(name=actor4)
            b = a.avgIncome
            cast_profit.append(b)

            t = 0
            if genre1 == "scifi" or genre2 == "scifi":
                t += a.scifi
            if genre1 == "action" or genre2 == "action":
                t += a.scifi
            if genre1 == "comedy" or genre2 == "comedy":
                t += a.scifi
            if genre1 == "romance" or genre2 == "romance":
                t += a.scifi
            if genre1 == "fantasy" or genre2 == "fantasy":
                t += a.scifi
            if genre1 == "family" or genre2 == "family":
                t += a.scifi
            if genre1 == "horror" or genre2 == "horror":
                t += a.scifi
            cast_vs_genre.append(t)

            a = ActorsVsDirectors.objects.get(actor=actor4, director=director)
            b = a.movieNum
            act_dir_movie.append(b)
            b = a.income
            act_dir_profit.append(b)



        actor5 = infoForm.cleaned_data['actor5']
        actor5 = actor5.lower()

        if actor5 == "n/a":
            cast_num -= 1
        else:
            a = Actors.objects.get(name=actor5)
            b = a.avgIncome
            cast_profit.append(b)

            t = 0
            if genre1 == "scifi" or genre2 == "scifi":
                t += a.scifi
            if genre1 == "action" or genre2 == "action":
                t += a.scifi
            if genre1 == "comedy" or genre2 == "comedy":
                t += a.scifi
            if genre1 == "romance" or genre2 == "romance":
                t += a.scifi
            if genre1 == "fantasy" or genre2 == "fantasy":
                t += a.scifi
            if genre1 == "family" or genre2 == "family":
                t += a.scifi
            if genre1 == "horror" or genre2 == "horror":
                t += a.scifi
            cast_vs_genre.append(t)

            a = ActorsVsDirectors.objects.get(actor=actor5, director=director)
            b = a.movieNum
            act_dir_movie.append(b)
            b = a.income
            act_dir_profit.append(b)


        actor6 = infoForm.cleaned_data['actor6']
        actor6 = actor6.lower()

        if actor6 == "n/a":
            cast_num -= 1
        else:
            a = Actors.objects.get(name=actor6)
            b = a.avgIncome
            cast_profit.append(b)

            t = 0
            if genre1 == "scifi" or genre2 == "scifi":
                t += a.scifi
            if genre1 == "action" or genre2 == "action":
                t += a.scifi
            if genre1 == "comedy" or genre2 == "comedy":
                t += a.scifi
            if genre1 == "romance" or genre2 == "romance":
                t += a.scifi
            if genre1 == "fantasy" or genre2 == "fantasy":
                t += a.scifi
            if genre1 == "family" or genre2 == "family":
                t += a.scifi
            if genre1 == "horror" or genre2 == "horror":
                t += a.scifi
            cast_vs_genre.append(t)

            a = ActorsVsDirectors.objects.get(actor=actor6, director=director)
            b = a.movieNum
            act_dir_movie.append(b)
            b = a.income
            act_dir_profit.append(b)



        b = Actors.objects.get(name=actor1)
        #if b.DoesNotExist() == True:
           # i=0
        #else:
        i = b.avgIncome
    result = success(cast_num,genre_num,act_dir_movie,act_dir_profit,prev_year_movie_genre,
                     prev_year_avg_profit_genre,cast_profit,cast_vs_genre,dir_gross)
    return render(request,'showRes.html',{'result':result})




#############


#def home(request):
   # movies = Movies.objects.all()
   # actors = Actors.objects.all()
    #movieWiseActors = {}
  #  for mov in movies:
     #   artList = []
        #for art in actors:
           # if art.movieId == mov.movieId:
              #  artList.append(art)
        #movieWiseActors[mov] = artList
    #return render(request,'home.html', {})