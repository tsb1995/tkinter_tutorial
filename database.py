from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Address Book")
root.iconbitmap('./img/Coffee.ico')
root.geometry('400x400')

# Create our database / connect
conn = sqlite3.connect('address_book.db')

# Create our cursor
c = conn.cursor()

# Create a table (only run once)

# c.execute(""" CREATE TABLE addresses (
#                 first_name text,
#                 last_name text,
#                 address text,
#                 city text,
#                 state text,
#                 zipcode integer
#                 )""")

# Create Save Function
def update():
    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Delete a record
    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",
            {
                "first": f_name_edit.get(),
                "last": l_name_edit.get(),
                "address": address_edit.get(),
                "city": city_edit.get(),
                "state": state_edit.get(),
                "zipcode": zipcode_edit.get(),
                "oid": record_id
            })

    # Commit changes to db
    conn.commit()

    # Close our connection to db
    conn.close()

    # Close our editor window
    editor.destroy()

# Create Function to Edit Record
def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap('./img/Coffee.ico')
    editor.geometry('400x250')

    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    record_id = delete_box.get()

    # Query our Database (add oid to * to access the entry id as well as info)
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    record = c.fetchall()

    # Commit changes to db
    conn.commit()
    # Close our connection to db
    conn.close()

    # Create global variables for text box names
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    # Create and display entry text boxes
    f_name_edit = Entry(editor, width=30)
    f_name_edit.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_edit = Entry(editor, width=30)
    l_name_edit.grid(row=1, column=1)
    address_edit = Entry(editor, width=30)
    address_edit.grid(row=2, column=1)
    city_edit = Entry(editor, width=30)
    city_edit.grid(row=3, column=1)
    state_edit = Entry(editor, width=30)
    state_edit.grid(row=4, column=1)
    zipcode_edit = Entry(editor, width=30)
    zipcode_edit.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label_edit = Label(editor, text="First Name")
    f_name_label_edit.grid(row=0, column=0, padx=20, pady=(10, 0))
    l_name_label_edit = Label(editor, text="Last Name")
    l_name_label_edit.grid(row=1, column=0)
    address_label_edit = Label(editor, text="Address")
    address_label_edit.grid(row=2, column=0)
    city_label_edit = Label(editor, text="City")
    city_label_edit.grid(row=3, column=0)
    state_label_edit = Label(editor, text="State")
    state_label_edit.grid(row=4, column=0)
    zipcode_label_edit = Label(editor, text="Zipcode")
    zipcode_label_edit.grid(row=5, column=0)

    # Fill in our record
    f_name_edit.insert(0, record[0][0])
    l_name_edit.insert(0, record[0][1])
    address_edit.insert(0, record[0][2])
    city_edit.insert(0, record[0][3])
    state_edit.insert(0, record[0][4])
    zipcode_edit.insert(0, record[0][5])

    # Create button to save changes
    update_btn = Button(editor, text="Save Changes", command=update)
    update_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=137)



# Create Function to Delete Record
def delete():
    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())

    # Commit changes to db
    conn.commit()

    # Close our connection to db
    conn.close()


# Create Submit Function for DB
def submit():
    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()


    # Insert into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                    {
                        'f_name': f_name.get(),
                        'l_name': l_name.get(),
                        'address': address.get(),
                        'city': city.get(),
                        'state': state.get(),
                        'zipcode': zipcode.get()
                    })


    # Commit changes to db
    conn.commit()

    # Close our connection to db
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function
def query():
    # Connect to database
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Query our Database (add oid to * to access the entry id as well as info)
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    # Loop through features in our records and add to variable
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    # Create label to display our records
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    # Commit changes to db
    conn.commit()
    # Close our connection to db
    conn.close()



# Create and display entry text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="ID Number to Select: ")
delete_box_label.grid(row=9, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=1, padx=(10, 0), pady=10, ipadx = 50)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=10, column=1, columnspan=1,pady=10, ipadx = 50)


# Commit changes to db
conn.commit()

# Close our connection to db
conn.close()



root.mainloop()
