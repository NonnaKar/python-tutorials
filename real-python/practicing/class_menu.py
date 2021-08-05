class Menu:
    calories = 0
    # class properties:
    #      Variables -
    #        a. Instance variables = food
    #        b. class variables = calories
    #      Methods
    #       is_healthy
    #       constructor (__init__)

    def __init__(self, food_choice):
        self.food = food_choice

    def is_healthy(self):
        message = ''
        if self.food == "hamburger":
            self.calories = 563
        elif self.food == "apple":
            self.calories = 95
        else:
            return "Oops, something went wrong. Please select a correct option from Menu..."
        if self.calories > 100:
            message = "Be careful! You will become a balloon!"
        else:
            message = "Your choice is healthy! Keep it up!"

        return message


# step 1
customer_choice = input(
    'Would you like to eat hamburger or apple ? (hamburger/apple)\n')

# step 2
print("You chose to eat", customer_choice)

# step3
# Now choice is an instance of class Menu
mchoice1 = Menu(food_choice=customer_choice)

# step 4
# trying to access the properties of class instance


def test_print():
    print(mchoice1.is_healthy())
    print(mchoice1.is_healthy())
    print(mchoice1.is_healthy())
    print(mchoice1.is_healthy())
    print(mchoice1.is_healthy())
    print(mchoice1.is_healthy())


test_print()
