import streamlit as st

def app(my_classroom):
    st.subheader('all students')
    col1,col2,col3 = st.columns(3)
    with col1:
        if st.button('save data',use_container_width=True):
            my_classroom.save_students_to_csv()
            st.success('data saved successfully')
    with col2:
        if st.button('load data',use_container_width=True):
            my_classroom.load_students_from_csv()
            st.success('data loaded successfully')
    with col3:
        if st.button('sort by ID',use_container_width=True):
            my_classroom.sort_students_by_id()
            st.success('sorted by id')
    col4,col5,col6 = st.columns(3)
    with col4:
        if st.button('sort by bmi',use_container_width=True):
            my_classroom.sort_students_by_bmi()
            st.success('sorted by bmi')
    with col5:
        if st.button('sort by name',use_container_width=True):
            my_classroom.sort_students_by_name()
            st.success('sorted by name')
    with col6:
        if st.button('sort by grade',use_container_width=True):
            my_classroom.sort_students_by_grade()
            st.success('sorted by grade')


    st.dataframe(my_classroom.generate_dataframe(), height=300)