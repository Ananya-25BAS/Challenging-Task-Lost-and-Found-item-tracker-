# Challenging-Task(Lost-and-Found item tracker)
My Vithyarthi project
Overview of the project
This Lost and Found Item Tracker is a simple application you run on your computer using text commands (a CLI application). It is built using Python to help quickly manage and keep track of things that are lost and found in a school,office etc.
The system is organized into three main parts:
1.	Main App (main_app.py): This runs the menu and takes your commands.
2.	Database Code (database_codes.py): This talks to a MySQL database to save, load, and update all the item information.
3.	Display Code (Non_db-functions.py): This handle’s clearing the screen and making the search results look neat and easy to read.
Main goal was to create one effective and efficient platform where everyone can quickly search for items and see if a lost item has been found.
Features:
#This tool is used for keeping track of things that are lost and things that are found. Everything is done by typing commands into yhe computer(CLI).
1.  Item Management(What the App Does):
    Adds detail of lost items: We can easily type the details and description of the lost items.
  	Adds detail of items found: We can easily type the details and description of the items found.
  	Search items using keywords:Finds and displays the details of item by entering any keyword (like colour, brand etc of the lost item).
  	Update Item Status:When someone claims their item, we can change the item's status from'LOST' to'FOUND'.
  	Displays lost and found items seperately in a table.
  	Displays all lost and found items together ina table.
2.  The Command Line (How You Use It):
*  Simple Menu: When we start the program, it gives us a simple list of choices, like:
1.  Record a LOST Item  2. View ALL LOST Items  3.  Mark a LOST Item as FOUND  4.  View ALL FOUND Items  5.  Search Items by Keyword  6.  View ALL Items (Lost & Found)  7.  Exit
*  Type and Go:We should just enter a number (like 3 to Search) and then type the details it asks for. It's fast and focused.
*  Clear Results: The search results show up right on your screen in a table that is easy to read.
Technologies/tools used:
	Programming language- Python 3.14
	Database- MySQL
	User interface- Command Line Interface (CLI)
Steps to install & run the project:
1]  Install python,do necessary setup and add python to path.
2]  Install MySQL and connect it with Python.
3]  Organize the required project files and configure the database.
4]  To run it,open the codes and run in python and now we are ready to track our items.
  	
