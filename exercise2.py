# list the possible movie recommendations
documentary = "Icarus"
drama = "A Beautiful Mind"
comedy = "Deadpool"
dramedy = "Birdman"
book = "We Are Our Brains by D.F.Swaab"

# find the user's rating of each genre
print("How much do you like documentaries? (Rate from 1 to 5)")
documentaries_rating = int(input())
print("How much do you like dramas? (Rate from 1 to 5)")
dramas_rating = int(input())
print("How much do you like comedies? (Rate from 1 to 5)")
comedies_rating = int(input())
all_ratings = [documentaries_rating, dramas_rating, comedies_rating]

# make the recommendation
if documentaries_rating >= 4:
    print("You might like this documentary:\n{}".format(documentary))
else:
    if dramas_rating >= 4 and comedies_rating >= 4:
        print("You might like this dramedy:\n{}".format(dramedy))
    elif dramas_rating >= 4:
        print("You might like this drama:\n{}".format(drama))
    elif comedies_rating >= 4:
        print("You might like this comedy:\n{}".format(comedy))
    else:
        max_rating = max(documentaries_rating, dramas_rating, comedies_rating)
        count_less = 0
        for r in all_ratings:
            if r < max_rating:
                count_less += 1
        if count_less == 2:
            max_index = all_ratings.index(max_rating)
            print("You rated the above genres pretty low, but here's the best recommendation I can give you.")
            if max_index == 0:
                print("You might like this documentary:\n{}".format(documentary))
            elif max_index == 1:
                print("You might like this drama:\n{}".format(drama))
            else:
                print("You might like this comedy:\n{}".format(comedy))
        else:
            print("Since you don't really like any of the above genres, here's a book recommendation:\n{}".format(book))
