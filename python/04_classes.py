class User:
    firstName = ""
    lastName = ""
    emailAddress = ""
    phoneNumber = ""
    allergies = ""
    foodDiet = ""
    userType = ""
    isActive = ""

    def getFullName(self):
        return self.firstName + " " + self.lastName


class MealItem:
    name = ""
    description = ""
    servingSize = ""
    allergens = ""


class Order:
    ingredients = ""


class Price:
    pass


user = User()
user.firstName = "John"
user.lastName = "Doe"
user.emailAddress = "johnDoe@mail.com"
user.phoneNumber = "+2331234567890"
user.allergies = "eggs"
user.foodDiet = "vegetarian"
user.userType = "Fellow"
user.isActive = True

print(
    f"My name is {user.getFullName()}, I am a {user.userType} and I have allergies to {user.allergies}"
)


class Father:
    lastName = "Abdul"
    company = "Fuudia"
    __wife = ""


class Son(Father):
    firstName = ""


son = Son()

print(son)


# write a class to model the various objects in the mest_kitchen_app project
