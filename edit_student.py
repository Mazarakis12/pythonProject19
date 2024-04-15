import streamlit as st
from students import Student, Classroom
from datetime import datetime

def app(myclassroom):
    st.title('edit student banana')
    student_id=st.number_input('enter student id to search',1,1000)
    student=myclassroom.get_student_by_id(student_id)
    if student:
        # Step 2: Display and Edit Student Data
        with st.form("edit_student"):
            st.subheader(f'Editing Data for Student ID: {student.id}')
            fname = st.text_input('First Name', value=student.fname)
            lname = st.text_input('Last Name', value=student.lname)
            dateBirth = st.date_input('Birth Date', value=student.dateBirth)
            gender = st.radio('Gender', ['Male', 'Female'], index=(0 if student.gender == 'Male' else 1))
            weight = st.slider('Weight', 30, 150, value=student.weight)
            height = st.slider('Height', 130, 200, value=student.height)

            # Submit button to save changes
            submitted = st.form_submit_button("Save Changes", use_container_width=True)
            if submitted:
                myclassroom.update_student(student_id, fname, lname, dateBirth, height, weight, gender)
                st.success('Student data updated successfully!')
    else:
        st.warning('No student found with the provided ID.')
