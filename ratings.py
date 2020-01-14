"""Restaurant rating lister."""


# put your code here

def find_restaurant_ratings(filename):

    file = open(filename)

    dict_of_restaurants = {}

    for line in file:
        line = line.rstrip()
        restaurant_ratings = line.split(':')
        dict_of_restaurants[restaurant_ratings[0]] = restaurant_ratings[1]

    return dict_of_restaurants


def print_restaurant_ratings(dict_of_restaurants):

    alpha_restaurants = sorted(dict_of_restaurants.keys())

    for restaurant_name in alpha_restaurants:
        print(f"{restaurant_name} is rated at {dict_of_restaurants[restaurant_name]}.")


def add_new_rating(current_dictionary):

    while True:

        restaurant_name_to_add = input("What restaurant would you like to add? ")
        rating_to_add = input("How would you rate it on a scale of 1-5? ")

        current_dictionary[restaurant_name_to_add] = rating_to_add

        continue_adding = input("Do you want to add another restaurant? Y or N? ")

        if continue_adding.upper() == "N":
            break

    return print_restaurant_ratings(current_dictionary)


restaurant_dictionary = find_restaurant_ratings("scores.txt")
add_new_rating(restaurant_dictionary)

