import pandas as pd
from datetime import datetime
import random
class Student:
    def __init__(self, id, fname, lname, dateBirth, height, weight, gender):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.dateBirth = dateBirth
        self.height = height
        self.weight = weight
        self.gender = gender
        self.courses = {'Math': -1, 'History': -1, 'Physics': -1, 'English': -1, 'Biology': -1}

    def add_grade(self, course_name, grade):
        self.courses[course_name] = grade

    def average_grade(self):
        return sum(self.courses.values()) / len(self.courses)

    def get_bmi(self):
        """
        Calculate and return the BMI (Body Mass Index).
        Formula: weight (kg) / height (m)^2
        Note: Height should be converted from cm to m.
        """
        height_m = self.height / 100  # converting height to meters
        bmi = self.weight / (height_m ** 2)
        return bmi

    def get_bmi_category(self):
        """
        Return the BMI category of the student based on their BMI value.

        Categories:
        - Underweight: Below 18.5
        - Normal: 18.5-25
        - Overweight: 25.0-30
        - Obesity: 30 and above
        """

        bmi = self.get_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:  # bmi >= 30
            return "Obesity"

    def __str__(self):
        return f"id: {self.id} first name: {self.fname}, last name: {self.lname} genter: {self.gender} "


#st1 = Student(1, "Alice", "Johnson", "2000-01-01", 153, 49, "Female")
#st2 = Student(2, "Bob", "Smith", "2001-02-02", 165, 59, "Male")

class Classroom:
    def __init__(self,room_name):
        self.room_name = room_name
        self.students = []
        self.filename = room_name + "_csv"

    def add_demo_data(self):
        # Create student instances with specific data
        students_data = [
            [1, "Alice", "Johnson", "2000-01-01", 153, 49, "Female"],
            [2, "Bob", "Smith", "2001-02-02", 165, 59, "Male"],
            [3, "Charlie", "Brown", "2002-03-03", 159, 65, "Male"],
            [4, "Diana", "White", "2003-04-04", 169, 64, "Female"],
            [5, "Eva", "Black", "2004-05-05", 180, 80, "Female"],
            [6, "Frank", "Taylor", "2000-06-06", 165, 78, "Male"],
            [7, "Grace", "Lee", "2001-07-07", 155, 60, "Female"],
            [8, "Henry", "Miller", "2002-08-08", 192, 84, "Male"],
            [9, "Ivy", "Davis", "2003-09-09", 168, 58, "Female"],
            [10, "Jack", "Wilson", "2004-10-10", 178, 72, "Male"],
            [11, "Kathy", "Moore", "2000-11-11", 162, 64, "Female"],
            [12, "Liam", "White", "2001-12-12", 183, 95, "Male"],
            [13, "Mia", "Harris", "2002-01-13", 171, 80, "Female"],
            [14, "Noah", "Nelson", "2003-02-14", 176, 90, "Male"],
            [15, "Olivia", "Martin", "2004-03-15", 181, 71, "Female"],
            [16, "Paul", "Garcia", "2000-04-16", 187, 87, "Male"],
            [17, "Quincy", "Adams", "2001-05-17", 188, 92, "Male"],
            [18, "Rosa", "Martinez", "2002-06-18", 174, 95, "Female"],
            [19, "Sam", "Lee", "2003-07-19", 167, 60, "Male"],
            [20, "Tina", "Turner", "2004-08-20", 164, 54, "Female"]
        ]
        # id, fname, lname, dateBirth, height,weight, gender
        # Courses list
        courses = ['Math', 'History', 'Physics', 'English', 'Biology']
        # Add the students to the classroom
        for data in students_data:
            student = Student(id=data[0], fname=data[1], lname=data[2],
                              dateBirth=datetime.strptime(data[3], "%Y-%m-%d").date(),  # Convert string to datetime
                              height=data[4], weight=data[5], gender=data[6])

            # Add random grades for each course
            for course in courses:
                student.add_grade(course, random.randint(8, 20))  # Assign random grades between 8 and 20

            self.add_student(student)

    def add_student(self, st):
        self.students.append(st)

    def average_grad_class(self):
        if len(self.students) == 0:
            return -1

        sum_grades = 0
        for st in self.students:
            sum_grades+= st.average_grade()

        return sum_grades / len(self.students)

    def student_exists(self, searchID):
        for st in self.students:
            if st.id == searchID:
                return True

        return False

    def get_next_student_id(self):
        if len(self.students) == 0:
            return 1

        max_id = 1
        for st in self.students:
            if st.id > max_id:
                max_id = st.id
        return max_id + 1

    def get_student_by_id(self, searchID):
        for st in self.students:
            if st.id == searchID:
                return st

        return None

    def update_student(self, id, fname, lname, dateBirth, height, weight, gender):
        st = self.get_student_by_id(id)
        if st:
            st.fname = fname
            st.lname = lname
            st.dateBirth = dateBirth
            st.height = height
            st.weight = weight
            st.gender = gender
            return True

        return False

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.id == student_id:
                del self.students[i]
                return True  # Student was found and deleted

        return False  # Student was not found

    def get_students_data(self):
        data = []
        for student in self.students:
            data.append({
                'ID': student.id,
                'First Name': student.fname,
                'Last Name': student.lname,
                'Date of Birth': student.dateBirth,
                'Height': student.height,
                'Weight': student.weight,
                'Gender': student.gender,
                'Courses': student.courses
            })
        return data


    def generate_dataframe(self):

            data = []

            for student in self.students:
                student_data = {
                    'ID':student.id,
                    'Last Name':student.lname,
                    'First Name':student.fname,
                    'Date of Birth':student.dateBirth,
                    'Height':student.height,
                    'Weight':student.weight,
                    'Gender':student.gender,
                    'Math':student.courses['Math'],
                    'History':student.courses['History'],
                    'Physics':student.courses['Physics'],
                    'English':student.courses['English'],
                    'Biology':student.courses['Biology'],
                    'Average Grade':student.average_grade(),
                    'BMI':student.get_bmi(),
                    'BMI':student.get_bmi_category()
                }
                data.append(student_data)

                # Creating a DateFrame
            df = pd.DataFrame(data)

                # Setting 'ID' as the index
            df.set_index('ID', inplace=True)

            return df

    def save_students_to_csv(self):
        df = pd.DataFrame(self.get_students_data())
        df.to_csv(self.filename, index=False)

    def load_students_from_csv(self):
            df = pd.read_csv(self.filename)
            self.students = []
            for index, row in df.iterrows():
                student = Student(
                    row['ID'],
                    row['First Name'],
                    row['Last Name'],
                    row['Date of Birth'],
                    row['Height'],
                    row['Weight'],
                    row['Gender']
                )
                student.courses = eval(row['Courses'])
                self.students.append(student)

    def sort_students_by_id(self):
        self.students.sort(key=lambda student:student.id)

    def sort_students_by_name(self):
        self.students.sort(key=lambda student:student.lname)

    def sort_students_by_bmi(self):
        self.students.sort(key=lambda student:student.get_bmi())

    def sort_students_by_grade(self):
        self.students.sort(key=lambda student:student.average_grade())
