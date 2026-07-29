import csv


journal_entries = []

FILE_NAME = "data/journal_entries.csv"

def load_entries():
    global journal_entries

    journal_entries = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            journal_entries.append(row)

def save_entries():
    fieldnames = [
        "entry_id",
        "student_name",
        "country",
        "city",
        "date_visited",
        "academic_field",
        "organization",
        "observation_type",
        "observation",
        "reflection"
    ]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(journal_entries)

def add_entry():
    if journal_entries:
        entry_id = int(journal_entries[-1]["entry_id"]) + 1
    else:
        entry_id = 1

    student_name = input("Enter student name: ")
    country = input("Enter country: ")
    city = input("Enter city: ")
    date_visited = input("Enter date visited: ")
    academic_field = input("Enter academic field: ")
    organization = input("Enter organization visited: ")
    observation_type = input("Enter observation type: ")
    observation = input("Enter observation: ")
    reflection = input("Enter cultural reflection: ")

    entry = {
        "entry_id": entry_id,
        "student_name": student_name,
        "country": country,
        "city": city,
        "date_visited": date_visited,
        "academic_field": academic_field,
        "organization": organization,
        "observation_type": observation_type,
        "observation": observation,
        "reflection": reflection
    }

    journal_entries.append(entry)
    save_entries()

    print("\nJournal entry added successfully.")

def view_entries():
    if not journal_entries:
        print("\nNo journal entries found.")
        return

    print("\n--- All Journal Entries ---")

    for entry in journal_entries:
        print(f"\nEntry ID: {entry['entry_id']}")
        print(f"Student Name: {entry['student_name']}")
        print(f"Country: {entry['country']}")
        print(f"City: {entry['city']}")
        print(f"Date Visited: {entry['date_visited']}")
        print(f"Academic Field: {entry['academic_field']}")
        print(f"Organization: {entry['organization']}")
        print(f"Observation Type: {entry['observation_type']}")
        print(f"Observation: {entry['observation']}")
        print(f"Reflection: {entry['reflection']}")
        print("-" * 40)

def search_entries():
    search_country = input("Enter a country to search: ")

    found = False

    for entry in journal_entries:
        if entry["country"].lower() == search_country.lower():
            print("\nEntry ID:", entry["entry_id"])
            print("Student Name:", entry["student_name"])
            print("Country:", entry["country"])
            print("City:", entry["city"])
            print("Date Visited:", entry["date_visited"])
            print("Academic Field:", entry["academic_field"])
            print("Organization:", entry["organization"])
            print("Observation Type:", entry["observation_type"])
            print("Observation:", entry["observation"])
            print("Reflection:", entry["reflection"])
            print("-" * 40)
            found = True

    if not found:
        print("No entries found.")

def delete_entry():
    entry_id = input("Enter the Entry ID to delete: ")

    for entry in journal_entries:
        if str(entry["entry_id"]) == entry_id:
            confirm = input("Are you sure you want to delete this entry? (yes/no): ")

            if confirm.lower() == "yes":
                journal_entries.remove(entry)
                save_entries()
                print("Journal entry deleted successfully.")
            else:
                print("Deletion canceled.")

            return

    print("Entry ID not found.")

def display_summary():
    if not journal_entries:
        print("\nNo journal entries available.")
        return

    countries = []
    cities = []
    academic_fields = []

    for entry in journal_entries:
        if entry["country"] not in countries:
            countries.append(entry["country"])

        if entry["city"] not in cities:
            cities.append(entry["city"])

        if entry["academic_field"] not in academic_fields:
            academic_fields.append(entry["academic_field"])

    print("\n--- Journal Summary ---")
    print("Total Entries:", len(journal_entries))
    print("Countries Visited:", len(countries))
    print("Cities Visited:", len(cities))
    print("Academic Fields:", len(academic_fields))

def edit_entry():
    entry_id = input("Enter the Entry ID to edit: ")

    for entry in journal_entries:
        if str(entry["entry_id"]) == entry_id:
            print("Press Enter to keep the current value.")

            student_name = input(
                f"Student Name [{entry['student_name']}]: "
            )
            country = input(
                f"Country [{entry['country']}]: "
            )
            city = input(
                f"City [{entry['city']}]: "
            )
            date_visited = input(
                f"Date Visited [{entry['date_visited']}]: "
            )
            academic_field = input(
                f"Academic Field [{entry['academic_field']}]: "
            )
            organization = input(
                f"Organization [{entry['organization']}]: "
            )
            observation_type = input(
                f"Observation Type [{entry['observation_type']}]: "
            )
            observation = input(
                f"Observation [{entry['observation']}]: "
            )
            reflection = input(
                f"Reflection [{entry['reflection']}]: "
            )

            if student_name:
                entry["student_name"] = student_name
            if country:
                entry["country"] = country
            if city:
                entry["city"] = city
            if date_visited:
                entry["date_visited"] = date_visited
            if academic_field:
                entry["academic_field"] = academic_field
            if organization:
                entry["organization"] = organization
            if observation_type:
                entry["observation_type"] = observation_type
            if observation:
                entry["observation"] = observation
            if reflection:
                entry["reflection"] = reflection

            save_entries()
            print("Journal entry updated successfully.")
            return

    print("Entry ID not found.")



def main():
    load_entries()

    while True:
        print("\n--- Culture to Classroom ---")
        print("1. Add Journal Entry")
        print("2. View Journal Entries")
        print("3. Search Journal Entries")
        print("4. Edit Journal Entry")
        print("5. Delete Journal Entry")
        print("6. Display Summary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            edit_entry()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            display_summary()
        elif choice == "7":
            print("Thank you for using Culture to Classroom.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

