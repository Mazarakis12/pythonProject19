import streamlit as st
from students import Student, Classroom

def app(my_class_room):
    st.title("Student to Delete Record")
    # Input for the student ID
    min_id = 1
    student_id = st.number_input("Enter Student ID", min_value=1, value=min_id)
    student = my_class_room.get_student_by_id(student_id)

    # Button to search for the student
    if st.button("Search"):
        student = my_class_room.get_student_by_id(student_id)
        if student:
            st.write(f"Found: {student.fname} {student.lname}")

    if student:
        delete_st(my_class_room, student)
    else:
        st.write("Student not Found!")

def delete_st(my_class_room, student):
    st.write(f"First Name: {student.fname}")
    st.write(f"Last Name: {student.lname}")
    st.write(f"Gender: {student.gender}")

        # Button to delete the grades
    if st.button("Delete Now", use_container_width=True):
        deleted = my_class_room.delete_student(student.id)
        if deleted:
            st.success("Student has been deleted successfully!")