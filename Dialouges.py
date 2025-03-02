while True:
    Topic = input(
        "Please select a topic:\n1. Coffee \n2. Pizza \n3. Car \n4. Restaurant \n5. Phone \n"
    )

    if Topic in ["Coffee", "Pizza", "Car", "Restaurant", "Butcher"]:
        break  # Exit loop when a valid topic is chosen
    else:
        print("Invalid choice! Please select a valid topic.")

if Topic == "Coffee":
    print("Great choice! Welcome to the coffee center!")
    print("We have: \n1. Latte \n2. Cappuccino \n3. Espresso \n4. Mocha")

    while True:
        Choice = input(
            "What would you like to have? (Reply with the name of the coffee) ")
        if Choice in ["Latte", "Cappuccino", "Espresso", "Mocha"]:
            print(f"Sure! We will prepare your {Choice} in a minute.")
            input("Press enter to continue...")
            print("Here's your coffee!")
            input("Press enter to continue...")

            while True:
                feedback = input(
                    "How was the coffee? (Reply with either 'Good' or 'Bad') ")
                if feedback in ["Good", "Bad"]:
                    if feedback == "Good":
                        print("Thanks! Have a great day!")
                    else:
                        print("We are sorry! We will improve next time.")
                    break
                else:
                    print("Invalid response! Please reply with 'Good' or 'Bad'.")
            break
        else:
            print("Invalid choice! Please select from the available options.")


if Topic == "Pizza":
    print("Fantastic! Welcome to Ibrahim's Pizza!")
    print("We have: \n1. Veg Extravaganza \n2. Farmhouse \n3. Paneer \n4. Corn \n5. Margherita")

    while True:
        x = input(
            "What would you like to have? (Reply with the name of the Pizza) ")
        if x in ["Veg Extravaganza", "Farmhouse", "Paneer", "Corn", "Margherita"]:
            print(f"Sure! We will be getting your {x} in some time...")
            input("Press enter to continue...")
            print(f"Here's your freshly baked {x} pizza!")
            input("Press enter to continue!")

            while True:
                y = input(
                    "How was the pizza? (Reply with either 'Good' or 'Bad') ")
                if y in ["Good", "Bad"]:
                    if y == "Good":
                        print("Thanks! Have a great day!")
                    else:
                        print("We are sorry! We will improve next time.")
                    break
                else:
                    print("Invalid response! Please reply with 'Good' or 'Bad'.")
            break
        else:
            print("Invalid choice! Please select from the available options.")


if Topic == "Car":
    print("Incredible choice! Welcome to Ibrahim's Car Showroom!")

    def show_cars():
        cars = {
            "Tesla Model S": "$89,990",
            "BMW X5": "$65,700",
            "Mercedes-Benz C-Class": "$46,850",
            "Ford Mustang": "$30,920",
            "Audi Q7": "$59,200",
            "Toyota Camry": "$26,420",
            "Honda Accord": "$27,295",
        }
        print("We have the following cars available:")
        for car, price in cars.items():
            print(f"- {car}: {price}")
        return cars

    cars = show_cars()

    while True:
        selected_car = input(
            "Which car would you like to know more about? (Reply with the car name) "
        )
        if selected_car in cars:
            print(
                f"Great choice! The {selected_car} is available for {cars[selected_car]}."
            )
            input("Press enter to continue...")
            print(
                f"Would you like to take the {selected_car} for a test drive?")
            test_drive = input("Reply with 'Yes' or 'No': ")
            if test_drive == "Yes":
                print(f"Enjoy your test drive in the {selected_car}!")
                input("Press enter to continue...")
                z = input("Did you like the car? (Reply with 'Yes' or 'No') ")
                if z == "Yes":
                    Buying = input(
                        "Ok! Would you like to buy the car? (Reply with YES or NO) "
                    )
                    if Buying == "Yes":
                        print("Car bought!")
                        exit()
                    else:
                        print("No worries! See you next time!")
                        exit()

            print("No worries! Let us know if you have any other preferences.")
            see_cars_again = input(
                "Would you like to see the cars again? (Yes/No) ")
            if see_cars_again.lower() == "yes":
                cars = show_cars()
            else:
                print("Thank you for visiting!")
                exit()
        else:
            print("Invalid choice! Please select from the available cars.")


if Topic == "Restaurant":
    print("Welcome to Ibrahim's Restaurant!")
    print("We offer:")
    dishes = ["Burger", "Pasta", "Steak", "Salad", "Sushi"]
    for dish in dishes:
        print(f"- {dish}")

    while True:
        selected_dish = input(
            "What would you like to order? (Reply with dish name) ")
        if selected_dish in dishes:
            print(f"Spectacular!! Your {selected_dish} will be ready soon.")
            input("Press enter to continue...")
            print(f"Here is your delicious {selected_dish}!")
            input("Press enter to continue...")
            feedback = input(
                "How was your meal? (Reply with 'Good' or 'Bad') ")
            if feedback == "Good":
                print("Thank you! We hope to see you again!")
            else:
                print("We're sorry! We'll improve next time.")
            break
        else:
            print("Invalid choice! Please select from the available dishes.")


if Topic == "Phones":
    print("Welcome to Ibrahim's Mobile Store!")
    phones = {
        "iPhone 15 Pro": "$999",
        "Samsung Galaxy S23 Ultra": "$1199",
        "Google Pixel 8": "$699",
        "OnePlus 11": "$799",
        "Xiaomi 13 Pro": "$899"
    }
    print("We have the following mobile phones available:")
    for phone, price in phones.items():
        print(f"- {phone}: {price}")

    while True:
        selected_phone = input(
            "Which phone would you like to know more about? (Reply with the phone name) ")
        if selected_phone in phones:
            print(
                f"Great choice! The {selected_phone} is available for {phones[selected_phone]}.")
            input("Press enter to continue...")
            print("Would you like to buy this phone?")
            buy_phone = input("Reply with 'Yes' or 'No': ")
            if buy_phone == "Yes":
                print("Congratulations on your new phone!")
                exit()
            else:
                print("No worries! Let us know if you have any other preferences.")
        else:
            print("Invalid choice! Please select from the available phones.")
