# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter number a number that is more than zero\n"
    while True:

         try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

         except ValueError:
            print(error)

# Main Routine Goes Here

keep_going = ""
while keep_going == "":
    # Get width and height and cost per meter
    width = num_check("Enter the width of the fence (m):")
    height = num_check("Enter the height of the fence (m):")
    cost = num_check("Enter the cost per meter ")

    # Calculate perimeter and price
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter:{perimeter} units")
    print(f"Price: ${price:.2f}")


    # Ask use if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit")
    print()


