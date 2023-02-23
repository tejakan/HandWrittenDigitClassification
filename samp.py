import streamlit as st


st.title("Tejaswini")
st.header("Header")
st.subheader("subheader")
st.text("raw text")
st.caption("caption")
st.code('for i in range(10) : print i')
st.markdown('# *heading1*')
st.write('this is normal')
"""btn=st.button('click')
    if(btn):
        st.write("hey there")
        
        
btn=st.button('square it')
if(btn):
    st.write('# square of ', x, 'is',x*x)

        """

ch=st.checkbox('I agree')
if(ch):
    st.write("thanks for agreeing")

r=st.radio('choose a category',('business','politics','sports'))
if r:
    st.write("you choose",r)


st.multiselect('choose a category',['business','politics','sports'])

sl=st.slider('Choose a range',0,100)
if sl:
    st.write('you chose',sl)

# input

name=st.text_input('Name')
if name:
    st.write('welcome',name)
st.text_area('message')
st.number_input('Age')
st.time_input('Time')
st.date_input('Date')
st.color_picker('color')
st.file_uploader('your file')

x=st.number_input('Enter your number')
st.write('# Square is ',x*x)



