current_movies = {'The Grinch':'11:00am',
                    'Rudolph': '1:00pm',
                    'Frosty then snowman':'3:00pm',
                    'Christmas Vacation':'5:00pm'}
print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('What movie would you like the showtime for?\n')

show_time = current_movies.get(movie);
if show_time == None:
    print("Requested showtime is'nt playing")
else:
    print("show time for movie is ",movie,show_time)