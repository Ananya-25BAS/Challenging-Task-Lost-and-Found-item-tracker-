import mysql.connector
from mysql.connector import Error
import time


 # connecting python with MySQL

        
import mysql.connector     #used for connecting python with MySQL

def get_db_connection():
    conn=None
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="Root@2025", database="data")
        print("Successfully connected to MySQL database")
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL",err)
        return None     # Return None on failure
    

# Create the table for lost and found items

def creating_tables():
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                type VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                location VARCHAR(255),
                contact_info VARCHAR(255),
                status VARCHAR(10) NOT NULL,
                date_lost DATETIME,
                date_found DATETIME)''')
        conn.commit()
       
    except Error as e:
         print(f"Error during creating: {e}")
    finally:
            if conn:
                conn.close()
    

 #adds detail of a lost item

def add_lostItem(itype,description,location,contact_info):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cur=conn.cursor()
        current_time=time.strftime('%Y-%m-%d %H:%M:%S')
        values=(itype,description,location,contact_info,current_time)
        a='''INSERT INTO items (type,description,location,contact_info,status,date_lost)
             VALUES (%s,%s,%s,%s,'LOST',%s)'''
        cur.execute(a,values)
        conn.commit()

        print('Lost item added successfully')
        print(f"Record Date:",current_time)

    except Error as e:
         print(f"Error during adding lost item: {e}")
         return None
    finally:
            if conn:
                conn.close()

                
 #update lost item as found

def update_itemFound(iid):
    conn=get_db_connection()
    if conn is None:
        return

    try:
        cur=conn.cursor()
        current_time=time.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute('SELECT status from items where id=%s',(iid,))
        item=cur.fetchone()

        if item is None:
            print('Item with id',iid,'not found')
            return


        if item[0]=='FOUND':
            print('Item id',iid,'is already marked as found')
            return

        a='''update items set status='FOUND',date_found=%s where id=%s'''
        cur.execute(a,(current_time,iid))
        conn.commit()

        print('Item found marked successfully')
        print(f"found date:",current_time)

    except Error as e:
              print(f"Error during search: {e}")
              return None
    finally:
            if conn:
                conn.close()


 #Displays item based on the status filter and returns the output

def get_items(stat_filter):
   conn=get_db_connection()
   if conn is None:
        return []
   try:
        cur=conn.cursor()
        items=[]
        if stat_filter=='ALL':
            cur.execute('Select id, type, description, location, contact_info, status, date_lost, date_found FROM items ORDER BY id DESC')
        elif stat_filter in('LOST', 'FOUND'):
            a='''SELECT id, type, description, location, contact_info, status, date_lost, date_found
                FROM items WHERE status = %s ORDER BY id DESC'''
            cur.execute(a,(stat_filter,))
        else:
            print("Invalid status filter.")
            return []

        items = cur.fetchall()
        return items

   except Error as e:
        print(f"Error viewing items: {e}")
        return []
   finally:
        if conn:
            conn.close()
            
#Searches for items based on a keyword and returns the output
    
def find_item(keyword):
    conn=get_db_connection() 
    if conn is None:
        return []
        
    try:
        cur=conn.cursor()
        search_term = f"%{keyword}%" # SQL wildcards for partial matching

        a= '''SELECT id, type, description, location, contact_info, status, date_lost, date_found
            FROM items WHERE type LIKE %s OR description LIKE %s
            ORDER BY id DESC'''
        cur.execute(a,(search_term, search_term))

        items = cur.fetchall()
        return items

    except Error as e:
        print(f"Error during search: {e}")
        return []
    finally:
        if conn:
            conn.close()
# Main execution block to run the functions
if __name__ == '__main__':
    # 1. Initialize the table
    print("--- 1. Starting Database Initialization ---")
    creating_tables()
    
    # 2. Add a new lost item
    print("\n--- 2. Adding a Lost Item ---")
    add_lostItem("Wallet", "Brown leather wallet with ID card", "Student Center Lounge", "john.doe@university.edu")
    
    # 3. View the current lost items to get its ID
    print("\n--- 3. Retrieving Item ID for Update ---")
    lost_items = get_items('LOST')
    
    if lost_items:
        # Get the ID of the most recently added item
        item_id_to_update = lost_items[0][0]
        print(f"Successfully retrieved Item ID: {item_id_to_update}")

        # 4. Mark the item as found
        print(f"\n--- 4. Marking Item ID {item_id_to_update} as FOUND ---")
        update_itemFound(item_id_to_update)
        
    else:
        print("No LOST items found to test the update.")

    # 5. Display ALL items
    print("\n--- 5. Listing ALL Items ---")
    all_items = get_items('ALL')
        
    
    # 6. Search for the item
    print("\n--- 6. Searching for 'wallet' ---")
    search_results = find_item('wallet')
    



        
        
        
        
