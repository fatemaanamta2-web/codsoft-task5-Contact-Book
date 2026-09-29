print("NEW CODE IS RUNNING")
import re

contacts = []


# ---------- VALIDATION FUNCTIONS ----------

def get_valid_name():
    while True:
        name = input("Enter name: ").strip()

        if name == "":
            print("Error: Name cannot be empty!")
        elif not all(char.isalpha() or char.isspace() for char in name):
            print("Error: Name should contain only letters and spaces!")
        else:
            return name


def get_valid_phone():
    while True:
        phone = input("Enter phone number: ").strip()

        if not phone.isdigit():
            print("Error: Phone number should contain only digits!")
        elif len(phone) != 10:
            print("Error: Phone number must contain exactly 10 digits!")
        else:
            return phone


def get_valid_email():
    while True:
        email = input("Enter email: ").strip()

        if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
            return email
        else:
            print("Error: Enter a valid email!")
            print("Example: example@gmail.com")


def get_valid_address():
    while True:
        address = input("Enter address: ").strip()

        if address == "":
            print("Error: Address cannot be empty!")
        elif len(address) < 5:
            print("Error: Please enter a valid address!")
        else:
            return address


# ---------- CONTACT BOOK ----------

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    # ---------- ADD CONTACT ----------

    if choice == "1":

        print("\n--- ADD CONTACT ---")

        name = get_valid_name()
        phone = get_valid_phone()
        email = get_valid_email()
        address = get_valid_address()

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)

        print("\nContact added successfully!")


    # ---------- VIEW CONTACTS ----------

    elif choice == "2":

        if not contacts:
            print("\nNo contacts found!")

        else:
            print("\n===== CONTACT LIST =====")

            for i, contact in enumerate(contacts, start=1):

                print(f"\nContact {i}")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])


    # ---------- SEARCH CONTACT ----------

    elif choice == "3":

        if not contacts:
            print("\nNo contacts found!")

        else:

            search = input(
                "Enter name or phone number to search: "
            ).strip().lower()

            found = False

            for contact in contacts:

                if (search in contact["name"].lower()
                        or search in contact["phone"]):

                    print("\nContact Found!")
                    print("Name:", contact["name"])
                    print("Phone:", contact["phone"])
                    print("Email:", contact["email"])
                    print("Address:", contact["address"])

                    found = True

            if not found:
                print("\nContact not found!")


    # ---------- UPDATE CONTACT ----------

    elif choice == "4":

        if not contacts:
            print("\nNo contacts found!")

        else:

            search = input(
                "Enter name of contact to update: "
            ).strip().lower()

            found = False

            for contact in contacts:

                if contact["name"].lower() == search:

                    print("\n--- ENTER NEW DETAILS ---")

                    contact["name"] = get_valid_name()
                    contact["phone"] = get_valid_phone()
                    contact["email"] = get_valid_email()
                    contact["address"] = get_valid_address()

                    print("\nContact updated successfully!")

                    found = True
                    break

            if not found:
                print("\nContact not found!")


    # ---------- DELETE CONTACT ----------

    elif choice == "5":

        if not contacts:
            print("\nNo contacts found!")

        else:

            search = input(
                "Enter name of contact to delete: "
            ).strip().lower()

            found = False

            for contact in contacts:

                if contact["name"].lower() == search:

                    contacts.remove(contact)

                    print("\nContact deleted successfully!")

                    found = True
                    break

            if not found:
                print("\nContact not found!")


    # ---------- EXIT ----------

    elif choice == "6":

        print("\nThank you for using Contact Book!")
        break


    # ---------- INVALID MENU CHOICE ----------

    else:

        print("\nInvalid choice! Please enter a number from 1 to 6.")