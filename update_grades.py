import streamlit as st
from students import Student, Classroom


def app(my_class_room):
    st.title("Student Grades Modifier")
    # Input for the student ID
    updated = False
    student_id = st.number_input("Enter Student ID", min_value=1, value=1)
    student = my_class_room.get_student_by_id(student_id)
    # Button to search for the student
    if st.button("Search"):
        student = my_class_room.get_student_by_id(student_id)
    if student:
        st.write(f'Found:{student.fname}{student.lname}')
        update_values(student)
        st.success('successfully update')
    else:
        st.write(f"There isn't student with this id {student_id}")

def update_values(student):
    with st.form(key='graceform'):
        courses=student.courses
        Math_grade=st.number_input('grade for Math',min_value=0,max_value=100,value=courses['Math'])
        History_grade = st.number_input('grade for History', min_value=0, max_value=100, value=courses['History'])
        Physics_grade = st.number_input('grade for Physics', min_value=0, max_value=100, value=courses['Physics'])
        English_grade = st.number_input('grade for English', min_value=0, max_value=100, value=courses['English'])
        Biology_grade = st.number_input('grade for Biology', min_value=0, max_value=100, value=courses['Biology'])
        submitted = st.form_submit_button('update grades')

    if submitted:
        student.add_grade('Math',Math_grade)
        student.add_grade('History',History_grade)
        student.add_grade('Physics',Physics_grade)
        student.add_grade('English',English_grade)
        student.add_grade('Biology',Biology_grade)




