# list the possible movie recommendations
documentary = "Icarus"
drama = "A Beautiful Mind"
comedy = "Deadpool"
dramedy = "Birdman"
book = "We Are Our Brains by D.F.Swaab"

# find out what the user likes
print("Do you like documentaries? (Type yes or no)")
likes_documentaries = input().lower()
print("Do you like dramas? (Type yes or no)")
likes_dramas = input().lower()
print("Do you like comedies? (Type yes or no)")
likes_comedies = input().lower()

# make the recommendation
if likes_documentaries == 'yes':
    print("You might like this documentary:\n{}".format(documentary))
else:
    if likes_dramas == 'yes' and likes_comedies == 'yes':
        print("You might like this dramedy:\n{}".format(dramedy))
    elif likes_dramas == 'yes':
        print("You might like this drama:\n{}".format(drama))
    elif likes_comedies == 'yes':
        print("You might like this comedy:\n{}".format(comedy))
    else:
        print("Since you don't like any of the above genres, here's a book recommendation:\n{}".format(book))
