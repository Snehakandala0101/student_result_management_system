<h1 align="center"> Student Result Management System (SRMS)</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue">
  <img src="https://img.shields.io/badge/Status-Completed-green">
  <img src="https://img.shields.io/badge/Focus-Backend-orange">
</p>

**A modular command-line based backend application built using Python that manages student academic records efficiently.**

This project demonstrates structured file handling, logging configuration, CSV data manipulation, and JSON result generation.

---

## :pushpin: Project Description

The Student Result Management System (SRMS) is a CLI-based backend mini project that allows users to manage student academic records efficiently.

It performs full CRUD operations (Create, Read, Update, Delete) on student data stored in a CSV file and generates structured results in JSON format.

The project is designed with modular architecture and separate logging configuration to simulate real-world backend development practices.

---
## 🎯 Objective

This project was built to strengthen backend fundamentals including file handling, data serialization, structured logging, and modular application design.

---
## Technologies Used
- Python
- CSV (for data storage)
- JSON (for result generation)
- Logging module (for activity tracking)
- File Handling

---
## :rocket:Features
:white_check_mark: Add new student records
:white_check_mark: View all student records
:white_check_mark: Search student by roll number
:white_check_mark: Update student marks
:white_check_mark: Delete student record
:white_check_mark: Generate Pass/Fail result in JSON
:white_check_mark: Activity logging system
:white_check_mark: Exception handling

---
## :gear:How It Works
:one: **Data Management (CSV)**
Student records are stored in ```data.csv```
**CSV structure:**
```Name, Roll_No, Marks```
The system:
- Automatically creates header if file is new
- Preserves header during updates and deletions
- Rewrites file safely after modifications

:two: **Result Processing (JSON)**

When the user selects Generate Result:

- CSV file is read
- Marks are converted to numeric values
- Pass/Fail is calculated
    - Pass if Marks ≥ 35
    - Fail if Marks < 35
- Results are stored in ```results.json```

**Example Output:**
```JSON
[
    {
        "name": "Sneha",
        "roll_no": "101",
        "marks": 78,
        "result": "Pass"
    }
]
```
:three: **Logging System**

Logging is configured separately in `logger_config.py.`

- Logs are stored in ```logs/system.log```
- Tracks:
    - Student addition
    - Updates
    - Deletions
    - Searches
    - Errors
    - Program exit

This improves traceability and debugging.

----

## Project Architecture
```
Student_result_management_system/
│
├── logs/
│   └── system.log       # Log file
├── data.csv             # Student records
├── logger_config.py     # Logging configuration
├── main.py              # Core application logic
├── results.json         # Generated results
└── README.md
```
---
## Requirements
- Python 3.10 or above

---
## How to Run

:one: Clone the repository
```bash
git clone https://github.com/Snehakandala0101/student_result_management_system.git
```
:two: Navigate into project folder
```bash
cd student_result_management_system
```
:three: Run the application
```bash
python main.py
```
---
## Concepts Practiced
- Python file handling
- CSV file operations
- JSON serialization
- Logging with FileHandler
- Exception handling

---
### Future Enhancements
:diamonds: Convert to Flask web application
:diamonds: Integrate SQLite database
:diamonds: Add authentication system

---


#### Author

Sneha Kandala