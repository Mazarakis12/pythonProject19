import streamlit as st

st.header('This is a header')

st.text('Hello this is my web')

st.success('Sucsesful')

st.warning('You should to put your email')

st.info('This is information')

st.error('This is error')

fname = st.text_input('Enter your name here...')
password = st.text_input('Enter your password here...', type = 'password')

message = st.text_area('Write your comments',height = 100)

height = st.number_input('Enter your height',1.0,2.0)

birthday = st.date_input('Enter your birthday')

mytime = st.time_input('My time')

color = st.color_picker('Select color')

mylanguage =['python','go','javascript','lua']

choice = st.selectbox('language', mylanguage)
st.write(f'You selected {choice}')

SpokerLanguage = ['greek','english','japanese','french','spanish']
mylag = st.multiselect('Spoker lag',SpokerLanguage,default = 'greek')

age = st.slider('Your age',18,60)
