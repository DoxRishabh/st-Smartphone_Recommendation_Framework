import streamlit as st
import pickle
import pandas as pd
import numpy as np

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color:black;
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()





def fetch_features(smartphone_features):
    return smartphone.loc[smartphone['phonename'] == smartphone_features]





def recommend(phone):
    phone_index = smartphone[smartphone['phonename'] == phone].index[0]
    distances = similarity[phone_index]
    phones_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_phone=[]
    recommend_features=[]
    for i in phones_list:
        smartphone_features=i[1]
        recommended_phone.append(smartphone.iloc[i[0]].phonename)
        recommend_features.append(fetch_features(smartphone_features))
    return recommended_phone,recommend_features

smartphone_list=pickle.load(open('st-Smartphone_Recommendation_Framework/smartphone_recommendation_system-main/smartphone.pkl','rb'))

similarity=pickle.load(open('.\similarity1.pkl','rb'))
smartphone=pd.DataFrame(smartphone_list)

#sam=pickle.load(open('smartphone_recommendation_system-main\smartphone.pkl','rb'))
#smartphone1=pd.DataFrame(sam)

st.title("Smartphone Recommendation Framework")

selectsmartphone = st.selectbox(
    'Select the smartphone which you have in your mind?',
    smartphone['phonename'].values)
if st.button('recommend'):
    names,features=recommend(selectsmartphone)


    with st.expander(names[0]):
        st.markdown('''---''')
        test=smartphone.loc[smartphone['phonename'] == names[1]]
        st.write("Price: ₹",test['phoneprice'].values[0])

    with st.expander(names[1]):
        st.markdown('''---''')
        test=smartphone.loc[smartphone['phonename'] == names[1]]
        st.write("Price: ₹",test['phoneprice'].values[0])

    with st.expander(names[2]):
        st.markdown('''---''')
        test=smartphone.loc[smartphone['phonename'] == names[1]]
        st.write("Price: ₹",test['phoneprice'].values[0])

    with st.expander(names[3]):
        st.markdown('''---''')
        test=smartphone.loc[smartphone['phonename'] == names[1]]
        st.write("Price: ₹",test['phoneprice'].values[0])

    with st.expander(names[4]):
        st.markdown('''---''')
        test=smartphone.loc[smartphone['phonename'] == names[1]]
        st.write("Price: ₹",test['phoneprice'].values[0])
