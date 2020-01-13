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


structured_file = find_restaurant_ratings("scores.txt")
print_restaurant_ratings(structured_file)
