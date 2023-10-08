
# Create an empty shopping list
shopping_list = []

# Function to display the current items on the list
def display_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")

# Function to add an item to the list
def add_item():
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

# Function to delete an item from the list
def delete_item():
    display_list()
    if not shopping_list:
        print("There are no items to delete.")
        return

    item_to_delete = input("Enter the item you want to delete: ")
    if item_to_delete in shopping_list:
        shopping_list.remove(item_to_delete)
        print(f"{item_to_delete} has been removed from your shopping list.")
    else:
        print(f"{item_to_delete} is not on your shopping list.")

# Menu loop
while True:
    print("\nMenu:")
    print("1. Display shopping list")
    print("2. Add item to shopping list")
    print("3. Delete item from shopping list")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_list()
    elif choice == '2':
        add_item()
    elif choice == '3':
        delete_item()
    elif choice == '4':
        print("Thank you for using the supermarket system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")