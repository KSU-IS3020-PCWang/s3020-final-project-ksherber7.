# IS 3020 Final Project

## Student and Project Information

- Student name: Sarah Herbert
- GitHub username:ksherber7
- Project title: Culture to Classroom 
- Application purpose: Culture to Classroom is a Python application that helps study abroad students document, organize, and review their academic experiences while studying internationally.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.

- Python 3.x
- PyCharm
- The project folder must include:
  - `culture_to_classroom.py`
  - `data/journal_entries.csv` 

1. Open the project in PyCharm.
2. Verify that the `data` folder contains the `journal_entries.csv` file.
3. Open `culture_to_classroom.py`.
4. Click the **Run** button or press **Shift + F10**.
5. When the menu appears, enter a number (1–7) to choose a menu option.
6. Follow the prompts to add, view, search, edit, delete, or summarize journal entries.
7. Select **7** to exit the application.


## Major Features

List the major user-facing features implemented in the final application.

- Add a new journal entry
- View all journal entries
- Search journal entries by country
- Edit existing journal entries
- Delete journal entries
- Display a summary of journal entries
- Save and load journal entries using a CSV file

## Python Concepts Used

Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.

- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- User input
- CSV file handling
- File input/output


## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.

The application stores all journal entries in a CSV file named `journal_entries.csv`, located in the `data` folder. Each row represents one journal entry created by the user.

The fields are:

| `entry_id` | A unique identification number assigned to each journal entry. |
| `student_name` | The name of the student creating the journal entry. |
| `country` | The country where the experience took place. |
| `city` | The city where the experience took place. |
| `date_visited` | The date the location / organization was visited. |
| `academic_field` | The student's academic field or major in relation to the experience. |
| `organization` | The company, university, museum, or organization.. etc visited. |
| `observation_type` | The type of observation recorded (for example, technology, culture, education, or business). |
| `observation` | A detailed description of what the student observed. |
| `reflection` | The student's personal reflection or takeaway from their experience. |



## Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.

- The application was tested by running each menu option in PyCharm to check that it worked correctly.
Major Test Scenarios

- Added new journal entries and confirmed they were saved to the CSV file.
- Viewed all journal entries to verify that stored information displayed correctly.
- Searched for journal entries by country using both existing and non-existing countries.
- Edited existing journal entries and confirmed that changes were saved to the CSV file.
- Deleted journal entries and verified they were removed from the CSV file.
- Displayed the journal summary to confirm the total number of entries, countries, cities, and academic fields.

Invalid Input Testing

- Entered a country that did not exist during a search to confirm the program displayed "No entries found."
- Entered an invalid Entry ID when editing or deleting to confirm the program displayed "Entry ID not found."
- Entered an invalid menu option to verify the program displayed "Invalid choice. Please try again."

File Testing 

- Verified that journal entries were successfully loaded from `journal_entries.csv` when the program started.
- Verified that new, edited, and deleted entries were correctly written back to the CSV file.
  
## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.

AI was used to help me with improving the project after the initial development and be more concise with my idea while being able to execute. The most significant improvements included debugging some Python errors, organizing functions, improving the menu structure, and implementing the search, edit, delete, and summary features. AI also helped explain some error messages and reviewed the final project to ensure it met the assignment requirements. All suggested changes were tested in PyCharm before being included in the final application.
