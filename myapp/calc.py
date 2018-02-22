from math import *
from numpy import *

def listToMat(l):
    return array([l])

def listToMDMat(m):
    l = []
    p = m.__len__()
    l = [[m[0]]]
    for i in range(1,p):
        l.append([m[i]])
    return l

def success(cast_num, genre_num, act_dir_movie, act_dir_profit, prev_year_movie_genre,
            prev_year_avg_profit_genre, cast_profit, cast_vs_genre, dir_gross):

    #cast_num, genre_num, dir_gross single values --- done
    #rests are arrays

   # act_dir_movie = listToMat(act_dir_movie1)
   # act_dir_profit = listToMDMat(act_dir_profit1)

    print(act_dir_movie)
    print(act_dir_profit)
   # for i in range(0,cast_num):
       # if act_dir_movie[i] == 0:
           # act_dir_profit[0][i] =0

    sum=0
    for i in range(0,cast_num):
        m = act_dir_movie[i]*act_dir_profit[i]
        sum +=(m/10)

    a = log(sum)/cast_num*.143
    cast_dir_col = a


    genre_profit =0
    c=0
    for i in range(0,genre_num):
        a = prev_year_movie_genre[i]*log(prev_year_avg_profit_genre[i]/10)

        c = c+prev_year_movie_genre[i]
        genre_profit = genre_profit+a


    genre_profit = (genre_profit/c)*.033

    expertise=0
    cast_div=0

    for i in range(0,cast_num):
        a = 0
        for j in range(0,genre_num):
            a+= cast_vs_genre[j]
        b = log(cast_profit[i]/10)
        expertise = expertise+(a*b)
        k = b/(a+1)
        if k>cast_div:
            cast_div = k

    expertise = expertise/cast_num*(.007)
    dir_gross = dir_gross*.039

    score = 0

    if expertise<1:
        score-=2
    elif expertise>=1 and expertise<2:
        score-=1
    elif expertise >= 2 and expertise < 4:
        score -= 0
    elif expertise >= 4 and expertise < 7:
        score += 1
    elif expertise >= 7:
        score += 2

    if cast_div < .4:
        score -= 2
    elif cast_div >= .4 and cast_div < .8:
        score -= 1
    elif cast_div >= .8 and cast_div < 2:
        score -= 0
    elif cast_div >= 2 and cast_div < 10:
        score += 1
    elif cast_div >= 10:
        score += 2

    if dir_gross < 80000:
        score -= 12
    elif dir_gross >= 80000 and dir_gross < 150000:
        score -= 6
    elif dir_gross >= 150000 and dir_gross < 300000:
        score -= 0
    elif dir_gross >= 300000 and dir_gross < 500000:
        score += 6
    elif dir_gross >= 500000:
        score += 12

    if cast_dir_col < .2:
        score -= 40
    elif cast_dir_col >= .2 and cast_dir_col < .27:
        score -= 20
    elif cast_dir_col >= .27 and cast_dir_col < .29:
        score -= 0
    elif cast_dir_col >= .29 and cast_dir_col < .4:
        score += 20
    elif cast_dir_col >= .4:
        score += 40

    if genre_profit < .45:
        score -= 10
    elif genre_profit >= .45 and genre_profit < .49:
        score -= 5
    elif genre_profit >= .49 and genre_profit < .51:
        score -= 0
    elif genre_profit >= .51 and genre_profit < .6:
        score += 5
    elif cast_dir_col >= .6:
        score += 10

    s = ""
    if score >= 45:
        s = "Superhit"

    if score >= 30 and score < 45:
        s = "Hit"

    if score >-5 and score<30:
        s = "Okay"

    if score > -45 and score <= -5:
        s = "Flop"

    if score <= -45:
        s = "Superflop"
   # print(" genre expertise = ",expertise)
    #print("cast diversity = ",cast_div)
    #print("Director's gross profit = ", dir_gross)
    #print("cast and director collaboration = " , cast_dir_col)
    #print("annual profit by genre = ",genre_profit)

    return s


#############################################################


def success1():
    cast_num = 10
    genre_num = 7
    dir_num = 1
    dir_gross = random.randint(100000,500000000)


    #director based
    previous_movie = random.randint(21, size = (cast_num)) #number of movies an actor did
    previous_movie_profit = random.randint(100000, 500000000, size = (dir_num,cast_num))# profit of each cast

    for i in range(0,cast_num):
        if previous_movie[i] == 0:
            previous_movie_profit[0][i] =0


    #Avg. profit of actor-director collaboration

    a = log((previous_movie_profit.dot(previous_movie))/10)/cast_num*.143
    cast_dir_col = a[0]

    # genre based movie profit
    prev_year_movie = random.randint(100, size = (genre_num))
    prev_year_avg_profit = random.randint(100000,500000000, size = (genre_num))


    movie_genre = random.randint(2,size = genre_num) #for now, random. original data will be used from database
    cast_profit = random.randint(100000,500000000,size = cast_num)
    cast_vs_genre = random.randint(20, size = (cast_num,genre_num)) #do


    #genre based profit, previous year
    genre_profit =0
    c=0
    for i in range(0,genre_num):
        a = movie_genre[i]*prev_year_movie[i]*log(prev_year_avg_profit[i]/10)
        if movie_genre[i]==1:
            c = c+prev_year_movie[i]
        genre_profit = genre_profit+a


    genre_profit = (genre_profit/c)*.033

    expertise=0
    cast_div=0

    #calculates the Weighted Average Genre Expertise and cast novelty
    for i in range(0,cast_num):
        a = movie_genre.dot(cast_vs_genre[i])
        #print(a)
        b = log(cast_profit[i]/10)
        expertise = expertise+(a*b)
        k = b/(a+1)
        if k>cast_div:
            cast_div = k

    expertise = expertise/cast_num*(.007)
    dir_gross = dir_gross*.0039

    print(" genre expertise = ",expertise)
    print("cast diversity = ",cast_div)
    print("Director's gross profit = ", dir_gross)
    print("cast and director collaboration = " , cast_dir_col)
    print("annual profit by genre = ",genre_profit)

    score = 0

    if expertise<1:
        score-=2
    elif expertise>=1 and expertise<2:
        score-=1
    elif expertise >= 2 and expertise < 4:
        score -= 0
    elif expertise >= 4 and expertise < 7:
        score += 1
    elif expertise >= 7:
        score += 2

    if cast_div < .4:
        score -= 2
    elif cast_div >= .4 and cast_div < .8:
        score -= 1
    elif cast_div >= .8 and cast_div < 2:
        score -= 0
    elif cast_div >= 2 and cast_div < 10:
        score += 1
    elif cast_div >= 10:
        score += 2

    if dir_gross < 80000:
        score -= 12
    elif dir_gross >= 80000 and dir_gross < 150000:
        score -= 6
    elif dir_gross >= 150000 and dir_gross < 300000:
        score -= 0
    elif dir_gross >= 300000 and dir_gross < 500000:
        score += 6
    elif dir_gross >= 500000:
        score += 12

    if cast_dir_col < .2:
        score -= 40
    elif cast_dir_col >= .2 and cast_dir_col < .27:
        score -= 20
    elif cast_dir_col >= .27 and cast_dir_col < .29:
        score -= 0
    elif cast_dir_col >= .29 and cast_dir_col < .4:
        score += 20
    elif cast_dir_col >= .4:
        score += 40

    if genre_profit < .45:
        score -= 10
    elif genre_profit >= .45 and genre_profit < .49:
        score -= 5
    elif genre_profit >= .49 and genre_profit < .51:
        score -= 0
    elif genre_profit >= .51 and genre_profit < .6:
        score += 5
    elif cast_dir_col >= .6:
        score += 10

    s = ""
    if score >= 45:
        s = "Superhit"

    if score >= 10 and score < 45:
        s = "Hit"

    if score >-10 and score<10:
        s = "Okay"

    if score > -45 and score <= -10:
        s = "Flop"

    if score <= -45:
        s = "Superflop"

    print(s)

#success1()
