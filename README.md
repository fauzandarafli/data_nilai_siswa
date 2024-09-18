# data_nilai_siswa
# Student Data Management System

## Overview
This is a simple Student Management System (Data Nilai Siswa) built with Python. The system allows administrators, lecturers, and students to manage and view student information, including exam and capstone project scores. It supports various user roles with different access levels:
- **Administrator**:
  - Display All Student Data
  - Add Student Data
  - Update Student Data
  - Input/Update Student Grades
  - Delete Student Data
  - Search Student Data
  - Exit
- **Lecturer**:
  - Display All Student Data
  - Input/Update Student Grades
  - Search Student Data
  - Exit
- **Student**:
  - Display Student Grades
  - Exit

## Features
- **Login**: User authentication with roles Administrator, Lecturer, or Student.
- **Display Student Data**: Display student data in table format.
- **Add Student Data**: Add new students to the system.
- **Update Student Data**: Update the name and program of students.
- **Input Student Grades**: Enter or update students' exam and capstone grades.
- **Delete Student Data**: Remove student data from the system.
- **Search Student Data**: Search for student data by ID, name, or program.

## Requirements
- Python 3.x
- `tabulate` module
- `colorama` module

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required modules using pip:
   ```bash
   pip install tabulate colorama

### Usage
Upon running the application, you'll be prompted to log in with your credentials. Based on your role, you will have different access to manage and view student data. Follow the on-screen prompts to navigate through the system's features.

### Future Improvements
- Integrate a database for more permanent data storage.
- Enhance the user interface for better usability.
- Add more roles and features based on user feedback.

### Contributing
Feel free to fork the repository and submit pull requests. Any improvements or bug fixes are welcome!

### Acknowledgement
This code was created as a completion of the Capstone Project 1 Purwadhika Data Science program assignment.

### Contact
For any questions or issues, please contact **Rafli Fauzan Andara** (hello.fauzandarafli@gmail.com)
