import tkinter as tk
from tkinter import ttk, BOTTOM, TOP, X, LEFT, RIGHT, Y
from PIL import ImageTk, Image
import sqlite3
from ttkthemes import ThemedTk
from tkcalendar import Calendar, DateEntry
from tkinter.filedialog import asksaveasfilename
import xlsxwriter

# Create our database / connect
conn = sqlite3.connect('transactions.db')

# Create our cursor
c = conn.cursor()

equi_bg_color = "#464646"

root = ThemedTk(theme="equilux")
root.configure(bg=equi_bg_color)
root.iconbitmap(default='./img/Coffee.ico')
root.wm_title('Transaction Manager')
root.geometry('400x400')

# # Remove title bar
# root.overrideredirect(1)

# Setup our Frames
root_frame = ttk.Frame(root)
root_frame.pack()
history_frame = ttk.Frame(root)
history_frame.pack()



# # Initialize table
# c.execute(""" CREATE TABLE transactions (
#                 first_name text,
#                 last_name text,
#                 date text,
#                 payment text,
#                 service text
#                 )""")




def update():
    # Connect to database
    conn = sqlite3.connect('transactions.db')
    # Create Cursor
    c = conn.cursor()

    record_id = transaction_id_entry.get()
    # Delete a record
    c.execute("""UPDATE transactions SET
            first_name = :first,
            last_name = :last,
            date = :date,
            payment = :payment,
            service = :service

            WHERE oid = :oid""",
            {
                "first": f_name_entry_edit.get(),
                "last": l_name_entry_edit.get(),
                'date': date_entry_edit.get(),
                'payment': payment_entry_edit.get(),
                'service': service_entry_edit.get(),
                "oid": record_id
            })

    # Commit changes to db
    conn.commit()

    # Close our connection to db
    conn.close()

    # Close our editor window
    history_window.destroy()
    view_history()
    editor_window.destroy()





def close_history():
    history_window.destroy()






# Define submit transaction button
def submit_transaction():
    # Create our database / connect
    conn = sqlite3.connect('transactions.db')

    # Create our cursor
    c = conn.cursor()

    # Insert into Table
    c.execute("INSERT INTO transactions VALUES (:f_name, :l_name, :date, :payment, :service)",
                    {
                        'f_name': f_name_entry.get(),
                        'l_name': l_name_entry.get(),
                        'date': date_entry.get(),
                        'payment': payment_entry.get(),
                        'service': service_entry.get()
                    })

    # Commit changes to db
    conn.commit()

    # Close our connection to db
    conn.close()

    # Close the windows
    view_history()
    add_window.destroy()






def add_transaction():

    global add_window
    global f_name_entry
    global l_name_entry
    global date_entry
    global payment_entry
    global service_entry


    add_window = ThemedTk(theme="equilux")
    add_window_frame = ttk.Frame(add_window)
    add_window_frame.pack()
    add_window.iconbitmap(default='./img/Coffee.ico')
    add_window.wm_title('Add Transaction')
    add_window.geometry('400x400')
    add_window.configure(bg=equi_bg_color)

    # Create and place labels
    f_name_label = ttk.Label(add_window_frame, text="First Name")
    f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
    l_name_label = ttk.Label(add_window_frame, text="Last Name")
    l_name_label.grid(row=1, column=0, padx=20, pady=(10, 0))
    date_label = ttk.Label(add_window_frame, text="Date")
    date_label.grid(row=2, column=0, padx=20, pady=(10, 0))
    payment_label = ttk.Label(add_window_frame, text="Payment")
    payment_label.grid(row=3, column=0, padx=20, pady=(10, 0))
    service_label = ttk.Label(add_window_frame, text="Service")
    service_label.grid(row=4, column=0, padx=20, pady=(10, 0))

    # Create and place entry fields
    f_name_entry = ttk.Entry(add_window_frame, width=30)
    f_name_entry.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_entry = ttk.Entry(add_window_frame, width=30)
    l_name_entry.grid(row=1, column=1, padx=20, pady=(10,0))
    date_entry = DateEntry(add_window_frame, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    date_entry.grid(row=2, column=1, padx=20, pady=(10,0))
    payment_entry = ttk.Entry(add_window_frame, width=30)
    payment_entry.grid(row=3, column=1, padx=20, pady=(10,0))
    service_entry = ttk.Entry(add_window_frame, width=30)
    service_entry.grid(row=4, column=1, padx=20, pady=(10,0))

    # Create Submit Transaction Button
    submit_transaction_button = ttk.Button(add_window_frame, text="Submit", command=submit_transaction)
    submit_transaction_button.grid(row=5, column=0, columnspan=2, padx=(44, 20), pady=10, ipadx=104)






def view_history():

    # Connect to database
    conn = sqlite3.connect('transactions.db')
    # Create Cursor
    c = conn.cursor()

    global history_window
    global transaction_id_entry


    history_window = ThemedTk(theme="equilux")
    history_window_frame = ttk.Frame(history_window)
    history_window_frame.pack()
    history_window.iconbitmap(default='./img/Coffee.ico')
    history_window.wm_title('Add Transaction')
    history_window.geometry('1200x400')
    history_window.configure(bg=equi_bg_color)


    # Query our Database (add oid to * to access the entry id as well as info)
    c.execute("SELECT *, oid FROM transactions")
    records = c.fetchall()

    # Convert tuples to list
    new_records = []
    for record in records:
        new_records.append(list(record))
    records = new_records
    print(records)

    # create Treeview with 3 columns
    cols = ('First', 'Last', 'Date', 'Payment', 'Service', 'Transaction Id')
    listBox = ttk.Treeview(history_window_frame, columns=cols, show='headings')

    # set column headings
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    # Insert Values to listBox
    for i, (first, last, date, payment, service, id) in enumerate(records, start=1):
        listBox.insert("", "end", values=(first, last, date, payment, service, id))

    history_label = ttk.Label(history_window_frame, text="Transaction History", font=("Arial",30))
    history_label.grid(row=0, columnspan=3)

    transaction_id_label = ttk.Label(history_window_frame, text="Transaction Id to Edit:")
    transaction_id_label.grid(row=4, column=0)

    transaction_id_entry = ttk.Entry(history_window_frame)
    transaction_id_entry.grid(row=5, column=0)


    update_transaction = ttk.Button(history_window_frame, text="Edit Transaction", width=15, command=edit_transaction)
    update_transaction.grid(row=6, column=0)

    close_button = ttk.Button(history_window_frame, text="Close Window", width=15, command=close_history)
    close_button.grid(row=5, column=1)

    # Commit changes to db
    conn.commit()
    # Close our connection to db
    conn.close()






def delete():
    # Connect to database
    conn = sqlite3.connect('transactions.db')
    # Create Cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from transactions WHERE oid= " + transaction_id_entry.get())

    # Commit changes to db
    conn.commit()

    # Close our connection to db
    conn.close()

    # Close our editor window
    history_window.destroy()
    view_history()
    editor_window.destroy()






# Create Function to Edit Record
def edit_transaction():
    global editor_window
    editor_window = ThemedTk(theme="equilux")
    editor_window_frame = ttk.Frame(editor_window)
    editor_window_frame.pack()
    editor_window.iconbitmap(default='./img/Coffee.ico')
    editor_window.wm_title('Transaction Editor')
    editor_window.geometry('400x400')
    editor_window.configure(bg=equi_bg_color)

    # Connect to database
    conn = sqlite3.connect('transactions.db')
    # Create Cursor
    c = conn.cursor()

    record_id = transaction_id_entry.get()

    # Query our Database (add oid to * to access the entry id as well as info)
    c.execute("SELECT * FROM transactions WHERE oid = " + record_id)
    record = c.fetchall()
    print(record)

    # Commit changes to db
    conn.commit()
    # Close our connection to db
    conn.close()

    # Create global variables for text box names
    global f_name_entry_edit
    global l_name_entry_edit
    global date_entry_edit
    global payment_entry_edit
    global service_entry_edit

    # Create and place labels
    f_name_label_edit = ttk.Label(editor_window_frame, text="First Name")
    f_name_label_edit.grid(row=0, column=0, padx=20, pady=(10, 0))
    l_name_label_edit = ttk.Label(editor_window_frame, text="Last Name")
    l_name_label_edit.grid(row=1, column=0, padx=20, pady=(10, 0))
    date_label_edit = ttk.Label(editor_window_frame, text="Date")
    date_label_edit.grid(row=2, column=0, padx=20, pady=(10, 0))
    payment_label_edit = ttk.Label(editor_window_frame, text="Payment")
    payment_label_edit.grid(row=3, column=0, padx=20, pady=(10, 0))
    service_label_edit = ttk.Label(editor_window_frame, text="Service")
    service_label_edit.grid(row=4, column=0, padx=20, pady=(10, 0))

    # Create and place entry fields
    f_name_entry_edit = ttk.Entry(editor_window_frame, width=30)
    f_name_entry_edit.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_entry_edit = ttk.Entry(editor_window_frame, width=30)
    l_name_entry_edit.grid(row=1, column=1, padx=20, pady=(10,0))
    date_entry_edit = DateEntry(editor_window_frame, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    date_entry_edit.grid(row=2, column=1, padx=20, pady=(10,0))
    payment_entry_edit = ttk.Entry(editor_window_frame, width=30)
    payment_entry_edit.grid(row=3, column=1, padx=20, pady=(10,0))
    service_entry_edit = ttk.Entry(editor_window_frame, width=30)
    service_entry_edit.grid(row=4, column=1, padx=20, pady=(10,0))

    # Fill in our record
    f_name_entry_edit.insert(0, record[0][0])
    l_name_entry_edit.insert(0, record[0][1])
    date_entry_edit.delete(0, 'end')
    date_entry_edit.insert(0, record[0][2])
    payment_entry_edit.insert(0, record[0][3])
    service_entry_edit.insert(0, record[0][4])

    # Create button to save changes
    update_btn = ttk.Button(editor_window_frame, text="Save Changes", command=update)
    update_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

    delete_btn = ttk.Button(editor_window_frame, text="DELETE Transaction", command=delete)
    delete_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=137)






def save_xls():

    # Connect to database
    conn = sqlite3.connect('transactions.db')
    # Create Cursor
    c = conn.cursor()

    c.execute("SELECT * FROM transactions")

    # Grab our data and save as excel file
    rows = c.fetchall()

    # Convert tuples to list
    new_rows = []
    for row in rows:
        new_rows.append(list(row))
    rows = new_rows

    fields = ['first_name', 'last_name', 'date', 'payment', 'service']
    files = [('Excel Sheet', '*.xls')]

    # Prompt user for file location
    csvfilename = asksaveasfilename(filetypes = files, defaultextension = files)

    # Write into excel file
    with xlsxwriter.Workbook(csvfilename) as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(rows):
            worksheet.write_row(row_num, 0, data)


    # Commit changes to db
    conn.commit()
    # Close our connection to db
    conn.close()





# Add buttons for interacting with database
add_transaction_button = ttk.Button(root_frame, text="Add Transaction", command=add_transaction)
add_transaction_button.grid(row=0, column=0, columnspan=2, padx=(44, 20), pady=10, ipadx=100)

view_history_button = ttk.Button(root_frame, text="View History", command=view_history)
view_history_button.grid(row=1, column=0, columnspan=2, padx=(44, 20), pady=10, ipadx=112)

save_xls_button = ttk.Button(root_frame, text="Save as Excel Sheet", command=save_xls)
save_xls_button.grid(row=2, column=0, columnspan=2, padx=(44, 20), pady=10, ipadx=94)

close_button = ttk.Button(root_frame, text="Close Application", command=root.quit)
close_button.grid(row=3, column=0, columnspan=2, padx=(44, 20), pady=10, ipadx=98)


# Commit changes to db
conn.commit()

# Close our connection to db
conn.close()

root.mainloop()
