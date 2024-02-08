import streamlit as st
import pandas as pd
st.title('NS Coaching Center')
st.subheader('---Bridge for Success')
st.image('ns.jpg')
tab1,tab2=st.tabs(['Admission Details','Fee Structure'])
with tab1:
    col1,col2=st.columns(2)
    with col1:
        st.text_input('First Name :')
        st.text_input('Fathers Name')
        with col2:
            st.text_input('Last Name :')
            st.text_input('Mothers Name')
    st.text_area('Address')
    st.radio('Gender',['Male','Female','Transgender'])
    st.selectbox('Admission for Std',['7th','8th','9th','10th','11th sci','11th Com','12th Sci','12th Com'])
    st.button('Submit')
with tab2:
    data=pd.read_csv('NS.csv')
    data