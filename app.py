import streamlit as st
from streamlit_option_menu import option_menu
import about,add_student,home,delete_student,edit_student,update_grades
from students import Classroom

def main():
    st.set_page_config(layout='wide')
    menu = ['home','add student','edit student','search student','update grades','delete','about']
    # Initialize session state for the classroom if it doesn't exist
    if 'my_class_room' not in st.session_state:
        st.write("Initializing classroom...")  # Debug message
        st.session_state.my_class_room = Classroom('b_class')
        st.session_state.my_class_room.add_demo_data()
        st.write("Classroom initialized!")  # Debug message
    else:
        st.write("Classroom already initialized!")  # Debug message
    with st.sidebar:
        page = option_menu(
            menu_title='M E N U',
            options=menu,
            icons=['house', 'person-fill', 'pencil-square', 'binoculars-fill', 'building-add', 'trash3', 'info-circle'],
            menu_icon='chat-text-fill',
            orientation="vertical",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"}, }
        )

    if page == 'about':
        about.app()
    elif page == 'add student':
        add_student.app(st.session_state.my_class_room)
    elif page == 'home':
        home.app(st.session_state.my_class_room)
    elif page == 'delete':
        delete_student.app(st.session_state.my_class_room)
    elif page == 'edit student':
        edit_student.app(st.session_state.my_class_room)
    elif page == 'update grades':
        update_grades.app(st.session_state.my_class_room)
if __name__== '__main__':
    main()