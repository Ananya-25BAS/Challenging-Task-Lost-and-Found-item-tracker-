# Import functions from the Non_db_functions module
from Non_db_functions import clear_screen, display_results
# Import functions from the db module
from database_codes import get_db_connection,creating_tables,add_lostItem,update_itemFound,get_items,find_item


def view_items(stat_filter='LOST'):
    #Takes items and displays them based on the status filter
    print(f"\n--- {stat_filter} ITEMS ---")
    # Call the database function to fetch data
    items = get_items(stat_filter)
    # Call the Non_db_functions  to display data
    display_results(items, stat_filter)

def p_LItem():
    #Prompts the user for details to add a new lost item
    print("\n--- Add New Lost Item ---")
    itype = input("Enter Item Type (e.g., Wallet, Phone, Keys): ").strip()
    description = input("Enter Detailed Description (Color, brand, contents): ").strip()
    location = input("Enter Last Known Location (Where was it lost?): ").strip()
    contact_info = input("Enter Your Contact Info (Email or Phone): ").strip()

    if not all([itype, description, location, contact_info]):
        print(" All fields are required")
        return

    # Call the database function to add data
    add_lostItem(itype,description, location, contact_info)

def p_Fitems():
    #Prompts the user to mark a lost item as found
    # Display only lost items to choose from
    view_items('LOST') 
    print("\n--- Mark Item as Found ---")
    try:
        iid = input("Enter the ID of the item that was found: ").strip()
        if not iid.isdigit():
            print("Invalid input. Please enter a number for the ID.")
            return
            
        # Call the db function to update data
        update_itemFound(int(iid))
    except ValueError:
        print("Invalid input. Please enter a number for the ID.")

def p_search():
    #Prompts the user for a search keyword and displays output
    print("\n--- Search Lost & Found Items ---")
    keyword = input("Enter keyword (e.g., 'blue', 'Samsung', 'office'): ").strip()
    if keyword:
        # Call the db function to search data
        items = find_item(keyword)
        print(f"\n--- SEARCH RESULTS for '{keyword}' ---")
        # Call the Non_database_functions to display data
        display_results(items, "Search")
    else:
        print("Search cancelled.Keyword cannot be empty.")


def main():
    #Displays the main menu and handles user selection
    #get db 1st
    get_db_connection()

    while True:
        clear_screen()
        print("="*50)
        print("LOST AND FOUND ITEM TRACKER (PYTHON/MYSQL)")
        print("="*50)
        print("1. Record a LOST Item")
        print("2. View ALL LOST Items")
        print("3. Mark a LOST Item as FOUND")
        print("4. View ALL FOUND Items")
        print("5. Search Items by Keyword")
        print("6. View ALL Items (Lost & Found)")
        print("7. Exit")
        print("="*50)

        n= input("Enter your choice (1-7): ").strip()  #entering choice by the user

        if n=='1':
            prompt_for_lostItem()
        elif n== '2':
            view_items('LOST')
        elif n== '3':
            prompt_for_found()
        elif n== '4':
            view_items('FOUND')
        elif n== '5':
            prompt_for_search()
        elif n== '6':
            view_items('ALL')
        elif n== '7':
            print("Thank you for using the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        input("Press Enter to return to the main menu...")

# --- Entry Point ---
if __name__ == '__main__':
    main()





