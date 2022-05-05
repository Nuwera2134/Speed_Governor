import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image

st.set_page_config(
    page_title = 'Speed Governor ',
    page_icon = '✅',
    layout = 'wide'
)
st.header("Detection of Speed Governor Tempering")

# selected ='Home'

# if selected == 'Home':
#      pass 


st.sidebar.title("Select Accordingly ")


# st.sidebar.markdown("Select the Charts/Plots accordingly:")

df = pd.read_csv("Speed.csv")


selected_status = st.sidebar.selectbox('Select the Time/Average accordingly',
									('','AV SPEED(8H-9H)', 'AV SPEED(11H-12H)', 'AV SPEED(14H-15H)', 'AV SPEED(18H-19H)','PREDICTION'))


if selected_status =='':
     st.markdown("The dashboard will help a researcher to get to know \
 more about the given datasets and it's output")

     st.dataframe(df)
elif selected_status == 'AV SPEED(8H-9H)':
    st.markdown("Rate of Speed With Proportion of time")
    chart_1 = pd.DataFrame({'index':list(df[' TIME SINCE START (ms)']),  'Speed': df['AV SPEED(8H-9H)(km/h)']})
    st.line_chart(chart_1['Speed'])
    im1=Image.open('Figure_1.jpeg')
    st.image(im1)

elif selected_status == 'AV SPEED(11H-12H)':
    st.markdown("Rate of Speed With Proportion of time")
    chart_2 = pd.DataFrame({'index':list(df[' TIME SINCE START (ms)']),  'Speed': df['AV SPEED(11H-12H)(km/h)']})
    st.line_chart(chart_2['Speed'])
    im2=Image.open('Figure_2.jpeg')
    st.image(im2)

elif selected_status == 'AV SPEED(14H-15H)':
    st.markdown("Rate of Speed With Proportion of time")
    chart_3 = pd.DataFrame({'index':list(df[' TIME SINCE START (ms)']),  'Speed': df['AV SPEED(14H-15H)(km/h)']})
    st.line_chart(chart_3['Speed'])
    im2=Image.open('Figure_2.jpeg')
    st.image(im2)

elif selected_status == 'AV SPEED(18H-19H)':
    st.markdown("Rate of Speed With Proportion of time")
    chart_4 = pd.DataFrame({'index':list(df[' TIME SINCE START (ms)']),  'Speed': df['AV SPEED(18H-19H)(km/h)']})
    st.line_chart(chart_4['Speed'])
      
    im4=Image.open('Figure_4.jpeg')
    st.image(im4) 
     
    # chart_5 = pd.DataFrame(columns=['AV SPEED(8H-9H)(km/h)','AV SPEED(11H-12H)(km/h)','AV SPEED(18H-19H)(km/h)'])
    # st.bar_chart(chart_5)

    

elif selected_status == 'PREDICTION':
    Speed = st.number_input('Enter the Car Speed in Km/h')
    
    Power = st.number_input('Enter the Engine Power ')
    
    Acc = st.number_input('Enter the Acceralation m/s2')
    


    st.button("Predict Tempering")
    
# with chart2:


# with chart3:
# chart_3 = pd.DataFrame({'index':list(df[' TIME SINCE START (ms)']),  'Speed': df['AV SPEED(14H-15H)(km/h)']})
# st.line_chart(chart_3['Speed']) 

# # with chart4:
# chart_4 = pd.DataFrame({'index':list(df[' TIME SINCE START (ms)']),  'Speed': df['AV SPEED(18H-19H)(km/h)']})
# st.line_chart(chart_4['Speed'])