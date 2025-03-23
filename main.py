 # # # # # # # # # # # # # # # # # # # # # # #
#        Project: Student Management System   #
#         Author: dreyyan                     #
#       Language: Python                      #
#   Date Started: 03/23/2025                  #
#  Date Finished: 03/23/2025                  #
 # # # # # # # # # # # # # # # # # # # # # # #
''' IMPORTS '''
import time, json, random, string
from abc import ABC, abstractmethod

''' MODULES '''
from modules.line_delay_animation import line_delay_animation
from modules.clear_screen import clear_screen
from modules.display_format import display_format

''' UTILITIES '''
# UTILITY: Simulate a time delay within specified seconds
def delay(s):
    time.sleep(s)

# UTILITY: Display formatted error message to the user
def error_message(message):
    print(f"ERROR: {message}.")
    delay(2)

# UTILITY: Display header for the interface /w appropriate formatting
def display_header(interface_name, space, is_odd):
    line_delay_animation("          [ STUDENT MANAGEMENT SYSTEM ]", 0.1)
    if is_odd:
        print(((space - 1) * '-'), end='') # Output spacing
    else:
        print((space * '-'), end='')  # Output spacing
    line_delay_animation(f" {interface_name} {(space * '-')}", 0.1)

# UTILITY: Display the function in the main menu
def display_function(index, function_name):
    line_delay_animation(f"[{index}] {function_name}", 0.1)

# UTILITY: Prompt the user to press the Enter key to continue
def press_enter_to_continue():
    user_input = input("Press 'Enter' to continue...")

# UTILITY: Print string input with proper spacing
def print_with_spacing(string_input, space):
    print((space * ' ') + string_input)
    delay(0.1)

# Store courses according to department in a dictionary
courses_list = {
    "CAS": {
        "name": "College of Arts & Sciences",
        "courses": {
            1: "BA in English Language Studies",
            2: "BA in Foreign Languages",
            3: "BA in Political Science",
            4: "BS in Applied Mathematics",
            5: "BS in Biology",
            6: "BS in Chemistry"
        }
    },
    "CBM": {
        "name": "College of Business & Management",
        "courses": {
            1: "BS in Business Administration",
            2: "BS in Cooperatives Management",
            3: "BS in Hospitality Management",
            4: "BS in Tourism Management"
        }
    },
    "COC": {
        "name": "College of Communication",
        "courses": {
            1: "BA in Broadcasting",
            2: "BA in Journalism",
            3: "BS in Development Communication"
        }
    },
    "COD": {
        "name": "College of Dentistry",
        "courses": {
            1: "Doctor of Dental Medicine"
        }
    },
    "COE": {
        "name": "College of Education",
        "courses": {
            1: "Bachelor of Early Childhood Education",
            2: "Bachelor of Elementary Education",
            3: "Bachelor of Secondary Education",
            4: "Bachelor of Special Needs Education"
        }
    },
    "COM": {
        "name": "College of Medicine",
        "courses": {
            1: "Doctor of Medicine"
        }
    },
    "CON": {
        "name": "College of Nursing",
        "courses": {
            1: "BS in Nursing"
        }
    },
    "COP": {
        "name": "College of PESCAR",
        "courses": {
            1: "Bachelor of Culture and Arts Education",
            2: "Bachelor of Performing Arts",
            3: "Bachelor of Physical Education",
            4: "Bachelor of Science in Exercise and Sports Sciences"
        }
    },
    "COL": {
        "name": "College of Law",
        "courses": {
            1: "Juris Doctor(J.D.) Program"
        }
    },
    "CICT": {
        "name": "College of Information & Communications Technology",
        "courses": {
            1: "Bachelor of Library and Information Science",
            2: "BS in Computer Science",
            3: "BS in Entertainment and Multimedia Computing",
            4: "BS in Information Systems",
            5: "BS in Information Technology"
        }
    }
}

# UTILITY: Display list of available departments
def display_departments():
    print("**************** DEPARTMENT  LIST ****************")
    delay(0.1)
    display_format('*', 50)

    counter = 0
    # Display departments
    print("  ", end='') # Offset
    for key in courses_list.keys():
        if counter % 6 == 0 and counter != 0:
            print()
            print("          ", end='')  # Offset
        print(f"[{key}]   ", end='')
        counter += 1
        delay(0.05)
    print()
    display_format('*', 50)

# UTILITY: Display list of available courses in specified department
def display_courses(department_key):
    print("****************** COURSES LIST ******************")
    delay(0.1)
    display_format('*', 50)

    # Display courses
    for key, values in courses_list[department_key]["courses"].items():
        print(f"[{key}] {values}")
        delay(0.1)
    display_format('*', 50)

''' INTERFACE: LOGIN/REGISTER '''
def go_to_register_menu():
    # USERNAME LOGIC
    while True:
        clear_screen()
        display_header("REGISTER", 8, False)
        display_format('*', 26)
        print("USERNAME ~ [5-20 chars.][no spaces]")
        display_format('*', 26)
        username = input(" Username: ")

        if ' ' in username:  # ERROR: Space character in username
            error_message("Username must not contain spaces")
        if len(username) < 5:  # ERROR: Below minimum character limit
            error_message("Username must be at least 5 characters")
        elif len(username) > 20:  # ERROR: Above maximum character limit
            error_message("Username must not exceed 20 characters")
        else: break

    # PASSWORD LOGIC
    while True:
        clear_screen()
        display_header("REGISTER", 8, False)
        display_format('*', 26)
        print("PASSWORD ~ [5-20 chars.][one symbol]")
        display_format('*', 26)
        password = input(" Password: ")

        if ' ' in password:  # ERROR: Space character in password
            error_message("Password must not contain spaces")
        if len(password) < 5:  # ERROR: Below minimum character limit
            error_message("Password must be at least 5 characters")
        elif len(password) > 20:  # ERROR: Above maximum character limit
            error_message("Password must not exceed 20 characters")
        else: break

    get_input = input("")


def go_to_login_menu():
    while True:
        clear_screen()
        display_header("LOGIN", 22, True)
        display_format('*', 50)
        username = input(" Username: ").strip()
    get_input = input("")

def go_to_menu():
    while True:
        clear_screen()
        display_header("MENU", 22, False)
        display_format('*', 50)
        print(" [1] Login")
        delay(0.1)
        print(" [2] Register")
        delay(0.1)
        display_format('*', 50)

        try:
            menu_choice = int(input(" Enter choice: ").strip())

            # Redirect menu
            if menu_choice == 1:
                go_to_login_menu()
                return
            elif menu_choice == 2:
                go_to_register_menu()
                return

        except ValueError:
            error_message("Invalid input, please enter a number")
            continue

''' CLASS: BASE '''
class Person:
    # CONSTRUCTOR: Default
    def __init__(self):
        pass

    # CONSTRUCTOR: Parameterized
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    ''' METHODS: BASE '''
    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def display_main_menu(self):
        pass

''' CLASS: DERIVED(Student) '''
class Student(Person):
    # CONSTRUCTOR
    def __init__(self, name="N/A", age=0, gender="N/A", student_id="N/A", department="N/A", course="N/A"):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.department = department
        self.course = course
        self.student_information_filled = False
        self.student_enrolled = False

        # FUNCTION LIST
        self.function_list = {
            1: self.enroll_course,
            2: self.drop_course,
            3: self.display_information,
            4: self.edit_information
        }

    ''' METHODS: UTILITY '''

    ''' METHODS: OPERATIONS '''
    def enroll_course(self):
        # DEPARTMENT LOGIC
        while True:
            clear_screen()
            display_header("ENROLL COURSE", 18, True)

            # Display list of departments
            display_departments()

            # Prompt user to enter the department key
            chosen_department = input("Enter department key: ").strip().upper()

            # Check if department key exists in the course list
            if chosen_department not in courses_list:
                error_message("Department key does not exist")
                continue

            else: break

        # COURSE LOGIC
        while True:
            clear_screen()
            display_header("ENROLL COURSE", 18, True)

            # Display list of courses
            display_courses(chosen_department)

            # Prompt user to enter course key according to
            chosen_course = int(input("Enter course: ").strip())

            # Check if department key exists in the course list
            if chosen_course not in courses_list[chosen_department]["courses"]:
                error_message("Course does not exist")
                continue

            else:
                break

        # Convert chosen course to the actual string value
        self.department = chosen_department
        self.course = courses_list[chosen_department]["courses"][chosen_course]

        # Student successfully enrolled in a course
        self.student_enrolled = True

        # Display Department and Course
        clear_screen()
        display_header("ENROLL COURSE", 18, True)
        display_format('*', 50)
        print(f" Department: {self.department}")
        delay(0.1)
        print(f" Course: {self.course}")
        delay(0.1)
        display_format('*', 50)

        # Return to menu
        press_enter_to_continue()

    def drop_course(self):
        while True:
            clear_screen()
            display_header("DROP COURSE", 19, True)
            display_format('*', 50)
            print(f"Current course: {self.course}[{self.department}]")
            display_format('*', 50)

            print("Are you sure you want to drop from the course?")
            delay(0.1)
            print("NOTE: This process cannot be undone.")
            delay(0.1)
            user_choice = input("(yes/no): ").strip().lower()

            # ERROR: Blank user choice
            if user_choice == "":
                error_message("Invalid input, please enter yes/no")
                continue
            elif user_choice not in ['y', 'yes', 'n', 'no']:
                error_message("Invalid input, please enter /no")
                continue
            else: break

        if user_choice in ['y', 'yes']:
            self.department = "N/A"
            self.course = "N/A"
            self.student_enrolled = False
            print("* Course dropped successfully")
        elif user_choice in ['n', 'no']:
            print("* Cancelling course drop request")

        # Return to menu
        press_enter_to_continue()

    def display_information(self):
        clear_screen()
        display_header("STUDENT DETAILS", 17, True)
        display_format('*', 50)

        # Display student information right-aligned
        print("{:>13}".format(f" Name:"), f"{self.name}")
        delay(0.1)
        print("{:>13}".format(f" Age:"), f"{self.age}")
        delay(0.1)
        print("{:>13}".format(f" Gender:"), f"{self.gender}")
        delay(0.1)
        print("{:>13}".format(f" Student ID:"), f"{self.student_id}")
        delay(0.1)
        print("{:>13}".format(f" Department:"), f"{self.department}")
        delay(0.1)
        print("{:>13}".format(f" Course:"), f"{self.course}")
        delay(0.1)
        display_format('*', 50)

        # Return to menu
        press_enter_to_continue()

    def edit_information(self):
        # NAME LOGIC
        while True:
            clear_screen()
            display_header("EDIT INFORMATION", 16, False)
            display_format('*', 50)

            # Prompt user to input name
            student_name = input("Name: ").strip()

            if student_name == "": # ERROR: Blank name input
                error_message("Student name is required")
                continue
            elif len(student_name) < 5: # ERROR: Name length < 5
                error_message("Student name must be at least 5 characters")
                continue
            else:
                # Set name
                self.name = student_name
                break

        # AGE LOGIC
        while True:
            clear_screen()
            display_header("EDIT INFORMATION", 16, False)
            display_format('*', 50)

            try:
                # Prompt user to input name
                student_age = int(input("Age: ").strip())

                if student_age < 1: # ERROR: Non-positive age
                    error_message("Student name is required")
                    continue
                else:
                    # Set age
                    self.age = student_age
                    break

            except ValueError:
                error_message("Invalid age, please enter a positive number.")
                continue

        # GENDER LOGIC
        while True:
            clear_screen()
            display_header("EDIT INFORMATION", 16, False)
            display_format('*', 50)

            # Prompt user to input name
            student_gender = input("Gender[M/F/\"\"]: ").strip().upper()

            # Check if gender input is not valid
            if student_gender not in ['M', "MALE", 'F', 'FEMALE', ""]:
                error_message("Please enter a valid gender[M/F]")
                continue
            else: break

            # Set blank student gender
            if student_gender == "":
                student_gender = "Prefer not to say"

            # Set student gender to 'M'
            if student_gender in ['M', "MALE"]:
                student_gender = 'M'
            # Set student gender to 'F'
            elif student_gender in ['F', "FEMALE"]:
                student_gender = 'F'

        self.gender = student_gender

        # STUDENT ID LOGIC
        # Generate random student id
        self.student_id = ''.join(random.choices(string.digits, k=12))

        # Student successfully filled out the information
        self.student_information_filled = True

        # Display student information
        self.display_information()
        return

        # Return to menu
        press_enter_to_continue()

    ''' METHODS: INTERFACE '''
    def display_main_menu(self):
        while True:  # Display menu interface
            if self.student_enrolled and self.student_information_filled:
                status = "Eligible"
                message = "You have completed all the requirements"
            elif not self.student_enrolled and not self.student_information_filled:
                status = "Ineligible"
                message = "You have not yet filled out the information\n   & enrolled"
            else:
                status = "Ineligible"
                if not self.student_enrolled:
                    message = "You have not yet enrolled in a course"
                else:
                    message = "Missing student information"

            clear_screen()
            display_header("MAIN MENU", 20, True)
            display_format('*', 50)
            print(f" STATUS: {status}\n - {message}")
            delay(0.1)
            display_format('*', 50)
            display_function(1, "Enroll Course")
            display_function(2, "Drop Course")
            display_function(3, "Display Information")
            display_function(4, "Edit Information")
            display_function(5, "Log Out")
            display_format('*', 50)

            try:
                # Prompt the user to enter a choice
                user_input = int(input("Enter a choice: ").strip())

                # Exit program
                if user_input == 5:
                    go_to_menu()
                    return

                # Invoke function
                if user_input in self.function_list:
                    self.function_list[user_input]()  # Call function

                else:
                    error_message("Invalid choice, function does not exist")
                    continue

            except ValueError:
                error_message("Invalid choice, please enter a number")
                continue

''' CLASS: DERIVED(Teacher) '''
class Teacher(Person):
    # CONSTRUCTOR: Parameterized
    def __init__(self, name="N/A", age=0, gender="N/A", teacher_id="N/A", department="N/A"):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.department = department
        self.courses_taught = []
        self.assigned_department = False
        self.teacher_information_filled = False

        # FUNCTION LIST
        self.function_list = {
            1: self.assign_department_and_course,
            2: self.remove_course,
            3: self.display_courses,
            4: self.display_information,
            5: self.edit_information
        }

    ''' METHODS: UTILITY '''

    ''' METHODS: OPERATIONS '''
    def assign_department_and_course(self):
        # DEPARTMENT LOGIC
        while True:
            clear_screen()
            display_header("ASSIGN DEPARTMENT & COURSE", 11, False)

            # Display list of departments
            display_departments()

            # Prompt user to enter the department key
            chosen_department = input("Enter department key: ").strip().upper()

            # Check if department key exists in the course list
            if chosen_department not in courses_list:
                error_message("Department key does not exist")
                continue

            else:
                break

        # COURSE LOGIC
        while True:
            course_exists = True
            clear_screen()
            display_header("ASSIGN COURSE", 18, True)

            # Display list of courses
            display_courses(chosen_department)

            # Prompt user to enter course key according to department
            print("NOTE: Separate courses in spaces(' ')")
            delay(0.1)
            chosen_courses = input("Enter course/s: ").split()

            # Convert input indices to integers
            chosen_courses = [int(i) for i in chosen_courses]

            # Check if department key exists in the course list
            for i in chosen_courses:
                if i not in courses_list[chosen_department]["courses"]:
                    course_exists = False
                    break

            # ERROR: Non-existing course
            if not course_exists:
                error_message("Course does not exist")
            else: break

        # Set department
        self.department = chosen_department
        # Add courses taught
        self.courses_taught = [courses_list[chosen_department]["courses"][i] for i in chosen_courses]

        # Teacher successfully assigned in a department
        self.assigned_department = True

        # Display Department and Course
        clear_screen()
        display_header("ASSIGN COURSE", 18, True)
        display_format('*', 50)
        print(f"Department: {self.department}")
        delay(0.1)
        print("Course/s taught:\n * " + "\n * ".join(self.courses_taught))
        delay(0.1)
        display_format('*', 50)

        # Return to menu
        press_enter_to_continue()

    def remove_course(self):
        while True:
            course_exists = True
            clear_screen()
            display_header("REMOVE COURSE", 18, True)
            display_format('*', 50)

            # Check if teacher is curerntly teaching at least one course
            if len(self.courses_taught) == 0:
                print("* You have no assigned courses.")
                display_format('*', 50)
                # Return to menu
                press_enter_to_continue()
                return

            else:
                print("Course/s taught:\n" + "\n".join(f" {i + 1}. {course}" for i, course in enumerate(self.courses_taught)))
            delay(0.1)

            display_format('*', 50)

            courses_to_remove = input("Remove course/s: ").split()
            delay(0.1)

            # Convert input indices to integers
            courses_to_remove = [int(i) for i in courses_to_remove]

            # Check if department key exists in the course list
            for i in courses_to_remove:
                if i < 1 or i > len(self.courses_taught):
                    course_exists = False
                    break

            # ERROR: Non-existing course
            if not course_exists:
                error_message("Course does not exist")
            else: break

        clear_screen()
        display_header("REMOVE COURSE", 18, True)
        display_format('*', 50)
        print("Course/s to remove:\n" + "\n".join(f" {i}. {self.courses_taught[i - 1]}" for i in courses_to_remove))
        display_format('*', 50)
        print("NOTE: This process cannot be undone.")
        delay(0.1)
        user_choice = input("(yes/no): ").strip().lower()

        clear_screen()
        display_header("REMOVE COURSE", 18, True)
        display_format('*', 50)
        if user_choice in ['y', 'yes']:
            # Remove selected courses
            self.courses_taught = [course for i, course in enumerate(self.courses_taught, start=1) if i not in courses_to_remove]
            print("* Course/s dropped successfully")
        elif user_choice in ['n', 'no']:
            print("* Cancelling course/s removal")

        # Return to menu
        press_enter_to_continue()

    def display_courses(self):
        clear_screen()
        display_header("COURSES TEACHING", 16, False)
        display_format('*', 50)

        # Check if teacher is curerntly teaching at least one course
        if len(self.courses_taught) == 0:
            print("* You have no assigned courses.")
            display_format('*', 50)
            # Return to menu
            press_enter_to_continue()
            return
        else:
            print("Course/s taught:\n * " + "\n * ".join(self.courses_taught))
        delay(0.1)
        display_format('*', 50)

        # Return to menu
        press_enter_to_continue()

    def display_information(self):
        clear_screen()
        display_header("TEACHER DETAILS", 17, True)
        display_format('*', 50)
        # Display student information right-aligned
        print("{:>12}".format(f" Name:"), f"{self.name}")
        delay(0.1)
        print("{:>12}".format(f" Age:"), f"{self.age}")
        delay(0.1)
        print("{:>12}".format(f" Gender:"), f"{self.gender}")
        delay(0.1)
        print("{:>12}".format(f" Teacher ID:"), f"{self.teacher_id}")
        delay(0.1)
        print("{:>12}".format(f" Department:"), f"{self.department}")
        delay(0.1)
        display_format('*', 50)

        # Return to menu
        press_enter_to_continue()

    def edit_information(self):
        # NAME LOGIC
        while True:
            clear_screen()
            display_header("EDIT INFORMATION", 16, False)
            display_format('*', 50)

            # Prompt user to input name
            teacher_name = input("Name: ").strip()

            if teacher_name == "":  # ERROR: Blank name input
                error_message("Teacher name is required")
                continue
            elif len(teacher_name) < 5:  # ERROR: Name length < 5
                error_message("Teacher name must be at least 5 characters")
                continue
            else:
                # Set name
                self.name = teacher_name
                break

        # AGE LOGIC
        while True:
            clear_screen()
            display_header("EDIT INFORMATION", 16, False)
            display_format('*', 50)

            try:
                # Prompt user to input name
                teacher_age = int(input("Age: ").strip())

                if teacher_age < 1:  # ERROR: Non-positive age
                    error_message("Student name is required")
                    continue
                else:
                    # Set age
                    self.age = teacher_age
                    break

            except ValueError:
                error_message("Invalid age, please enter a positive number.")
                continue

        # GENDER LOGIC
        while True:
            clear_screen()
            display_header("EDIT INFORMATION", 16, False)
            display_format('*', 50)

            # Prompt user to input name
            teacher_gender = input("Gender[M/F/\"\"]: ").strip().upper()

            # Check if gender input is not valid
            if teacher_gender not in ['M', "MALE", 'F', 'FEMALE', ""]:
                error_message("Please enter a valid gender[M/F]")
                continue
            else:
                break

            # Set blank student gender
            if teacher_gender == "":
                teacher_gender = "Prefer not to say"

            # Set student gender to 'M'
            if teacher_gender in ['M', "MALE"]:
                teacher_gender = 'M'
            # Set student gender to 'F'
            elif teacher_gender in ['F', "FEMALE"]:
                teacher_gender = 'F'

        self.gender = teacher_gender

        # TEACHER ID LOGIC
        # Generate random teacher id
        self.teacher_id = ''.join(random.choices(string.digits, k=6))

        # Student successfully filled out the information
        self.teacher_information_filled = True

        # Display student information
        self.display_information()
        return

        # Return to menu
        press_enter_to_continue()

    ''' METHODS: INTERFACE '''
    def display_main_menu(self):
        while True:  # Display menu interface
            if self.assigned_department and self.teacher_information_filled:
                status = "Complete"
                message = "Designated department: " + self.department
            elif not self.assigned_department and not self.teacher_information_filled:
                status = "Incomplete"
                message = "You have not yet filled out the information\n   & been assigned in a department"
            else:
                status = "Incomplete"
                if not self.assigned_department:
                    message = "You have not yet been assigned in a department"
                else:
                    message = "Missing teacher information"

            clear_screen()
            display_header("MAIN MENU", 20, True)
            display_format('*', 50)
            print(f" STATUS: {status}\n - {message}")
            delay(0.1)
            display_format('*', 50)
            display_function(1, "Assign Department/Course")
            display_function(2, "Remove Course")
            display_function(3, "Display Courses")
            display_function(4, "Display Information")
            display_function(5, "Edit Information")
            display_function(6, "Log Out")
            display_format('*', 50)

            try:
                # Prompt the user to enter a choice
                user_input = int(input("Enter a choice: ").strip())

                # Exit program
                if user_input == 6:
                    go_to_menu()
                    return

                # Invoke function
                if user_input in self.function_list:
                    self.function_list[user_input]()  # Call function

                else:
                    error_message("Invalid choice, function does not exist")
                    continue

            except ValueError:
                error_message("Invalid choice, please enter a number")
                continue

teacher_start_program = Teacher()
teacher_start_program.display_main_menu()

# student_start_program = Student()
# student_start_program.display_main_menu()