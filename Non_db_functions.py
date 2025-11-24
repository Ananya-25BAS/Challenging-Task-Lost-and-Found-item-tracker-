import os

#Clears the console screen for better readability
def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display list of item
def display_results(items, stat_filter): 
    
    if not items:
        print(f"No {stat_filter.lower()} items found.") 
        return

    # Header for the table display
    h=f"{'ID':<4} | {'Type':<15} | {'Description':<30} | {'Location':<15} | {'Contact':<20} | {'Status':<6} | {'Date Lost':<19} | {'Date Found':<19}"
    sep= "-"*len(h)
    print(sep) 
    print(h)
    print(sep)

    for item in items:
        item_id, item_type, description, location, contact, status, date_lost, date_found = item
        
        # Datetime objects need to be formatted as strings
        date_lost_str = date_lost.strftime('%Y-%m-%d %H:%M:%S') if hasattr(date_lost, 'strftime') and date_lost else "N/A"
        date_found_str = date_found.strftime('%Y-%m-%d %H:%M:%S') if hasattr(date_found, 'strftime') and date_found else "N/A"
        
        # Format output neatly, handling truncation for Description and Contact
        print(f"{item_id:<4} | {item_type:<15} | {description[:27] + '...' if len(description) > 30 else description:<30} | {location:<15} | {contact[:17] + '...' if len(contact) > 20 else contact:<20} | {status:<6} | {date_lost_str:<19} | {date_found_str:<19}")

    print(sep)
