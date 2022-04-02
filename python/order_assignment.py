class meal:
    name = ""
    ingredients = ""
    imageUrl = ""
    Id = ""


class order:
    userName = ""
    userType = ""
    mealId = ""
    orderId = ""
    extraPortion = False
    toBePacked = False


class eitOrder(order):
    toBeDelivered = False
    deliveryLocation = ""
    hasInformedTrainingDirector = False


class nonEitOrder(order):
    toBeDeliveredToOffice = False
    willBeLate = False


class menu(meal):
    breakfastId = ""
    lunchId = ""
    dinnerId = ""


class user:
    userType = ""
    userId = ""
    firstName = ""
    lastName = ""
    emailAddress = ""
    phoneNumber = ""
    allergies = ""
    foodDiet = ""
    isActive = ""
