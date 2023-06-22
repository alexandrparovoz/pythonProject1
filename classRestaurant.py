#  создаем класс ресторан

class Restaurant():
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType

    def dscribeRestaurant(self):
        print('Name of this restaurant is ', self.restaurantName, 'and cuisine like', self.cuisineType)

    def openRestaurant(self):
        print('The ', self.restaurantName, "open until 12 o'clock.")

newRestaurant = Restaurant('Orion', 'Caribian ')
print("New rest is ", newRestaurant.restaurantName)
print('It have ', newRestaurant.cuisineType, 'kitchen.\n')

newRestaurant.dscribeRestaurant()
newRestaurant.openRestaurant()