import sqlite3

def display_entries():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone_number FROM Entries")
    rows = cursor.fetchall()
    print("ID | Name | Phone Number")
    print("----------------------------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    conn.close()

def add_entry(name, phone_number):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Entries (name, phone_number) VALUES (?, ?)", (name, phone_number))
    conn.commit()
    conn.close()
    print("Entry added successfully.")

def update_entry(entry_id, name, phone_number):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Entries SET name = ?, phone_number = ? WHERE id = ?", (name, phone_number, entry_id))
    conn.commit()
    conn.close()
    print("Entry updated successfully.")

def delete_entry(entry_id):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Entries WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    print("Entry deleted successfully.")

def main():
    while True:
        print("\nPhonebook Management")
        print("1. View Entries")
        print("2. Add Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_entries()

        elif choice == '2':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_entry(name, phone_number)

        elif choice == '3':
            entry_id = int(input("Enter entry ID to update: "))
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            update_entry(entry_id, name, phone_number)

        elif choice == '4':
            entry_id = int(input("Enter entry ID to delete: "))
            delete_entry(entry_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

# Matthew Beekman
# 12/4/2024
# Program 4