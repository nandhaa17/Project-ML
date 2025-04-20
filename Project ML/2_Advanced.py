import streamlit as st

st.set_page_config(
    page_title='Heart Disease',
    page_icon='💓',
)


st.title("Heart Disease Prediction")
st.caption("Try Simple option for easy access")

try:

    # Getting input via form

    with st.form("input_form"):
        age1=st.text_input("Age")
        sex1=st.selectbox("Sex",["Male","Female"],index=None)

        cp1=st.selectbox("Chest Pain Type",["Typical Angina","Atypical Angina","Non Anginal Pain","Asymptomatic"],index=None)

        trestbps1=st.text_input("Resting Blood Pressure")
        chol1=st.text_input("Cholesterol")
        fbs1=st.selectbox("Fasting blood Sugar greater than 120 mg/dl?",["Yes","No"],index=None)

        restecg1=st.selectbox("Resting ECG",["Normal","ST-T wave abnormality","Left ventricular hypertrophy"],index=None)

        thalach1=st.text_input("Maximum Heart rate during workout")
        exang1=st.selectbox("Do you feel chest pain while exercising",["Yes","No"],index=None)

        oldpeak1=st.text_input("ST Depression induced by exercise")
        slope1=st.selectbox("Slope of Peak Exercise ST segment",["Upsloping","Flat","Downsloping"],index=None)

        ca1=st.selectbox("Number of Major Vessels",[0,1,2,3],index=None)
        thal1=st.selectbox("Talessemia Type",["Normal","Fixed Defect","Reversible Defect"],index=None)

        submitted=st.form_submit_button("Submit")

    # Changing data types

    age1=int(age1)

    if sex1=="Male":
        sex1=1
    elif sex1=="Female":
        sex1=0


    if cp1=="Typical Angina":
        cp1=0
    elif cp1=="Atypical Angina":
        cp1=1
    elif cp1=="Non Anginal Pain":
        cp1=2
    elif cp1=="Asymptomatic":
        cp1=3

    trestbps1=int(trestbps1)

    chol1=int(chol1)

    if fbs1=="Yes":
        fbs1=1
    elif fbs1=="No":
        fbs1=0

    if restecg1=="Normal":
        restecg1=0
    elif restecg1=="ST-T wave abnormality":
        restecg1=1
    elif restecg1=="Left ventricular hypertrophy":
        restecg1=2

    thalach1=int(thalach1)

    if exang1=="Yes":
        exang1=1
    elif exang1=="No":
        exang1=0

    oldpeak1=float(oldpeak1)

    if slope1=="Upsloping":
        slope1=0
    elif slope1=="Flat":
        slope1=1
    elif slope1=="Downsloping":
        slope1=2

    if thal1=="Normal":
        thal1=1
    elif thal1=="Fixed Defect":
        thal1=2
    elif thal1=="Reversible Defect":
        thal1=3
        


    temp={'age':age1,'sex':sex1,'cp':cp1,'trestbps':trestbps1,'chol':chol1,'fbs':fbs1,'restecg':restecg1,'thalach':thalach1,'exang':exang1,'oldpeak':oldpeak1,'slope':slope1,'ca':ca1,'thal':thal1}

    # Importing training dataset

    import pandas as pd
    df=pd.read_csv('heart.csv')
    from sklearn.model_selection import train_test_split
    x=df.iloc[:,0:13]

    y=df.iloc[:,13]

    inp=pd.DataFrame(temp,index=[0])

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

    # Aplying machie learning algorithm

    from sklearn.naive_bayes import GaussianNB
    gnb=GaussianNB()
    gnb.fit(x_train,y_train.values.ravel())
    y=gnb.predict_proba(inp)
    st.write(pd.DataFrame([['No',y[0][0]],['Yes',y[0][1]]]).values)

    yes_val=round(y[0][1]*100)


    # Printing output chart

    out={"Yes":yes_val,"No":100-yes_val}
    out=pd.DataFrame(out,index=[0])
    st.markdown('\n\n\n\n\n')
    st.header("**Predicted Graph**")
    st.markdown("\n\n\n\n\n")
    st.bar_chart(out,y_label="Percentage of attack",stack=False)

    # Conclusion message

    if yes_val<45:
        st.header(':green[You are in Healthy Condition]')
    elif yes_val<70 and yes_val>=45:
        st.header(':yellow[You Have Low Risk of Heart Dissease]')
    else:
        st.header(':red[You Have High Risk of Heart Dissease]')
    
except:

    # Alerting the user to give all inputs
    
    st.caption("**:red[_Please fill out the details_ !]**")

import pandas as pd

import pandas as pd
import requests
from io import StringIO
import streamlit as st

def load_original_data():
    url = 'https://raw.githubusercontent.com/nandhaa17/Project-ML/refs/heads/main/Project%20ML/heart.csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None
df=load_original_data()
st.write(df)
#df=pd.read_csv('pages/heart.csv')

from sklearn.model_selection import train_test_split
x=df.iloc[:,0:13]

y=df.iloc[:,13]

inp=pd.DataFrame(temp,index=[0])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)

    # Aplying machie learning algorithm

from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(x_train,y_train.values.ravel())
y=gnb.predict_proba(inp)
st.write(pd.DataFrame([['No',y[0][0]],['Yes',y[0][1]]]).values)

yes_val=round(y[0][1]*100)


    # Printing output chart

out={"Yes":yes_val,"No":100-yes_val}
out=pd.DataFrame(out,index=[0])
st.markdown('\n\n\n\n\n')
st.header("**Predicted Graph**")
st.markdown("\n\n\n\n\n")
st.bar_chart(out,y_label="Percentage of attack",stack=False)

    # Conclusion message

if yes_val<45:
    st.header(':green[You are in Healthy Condition]')
elif yes_val<70 and yes_val>=45:
    st.header(':yellow[You Have Low Risk of Heart Dissease]')
else:
    st.header(':red[You Have High Risk of Heart Dissease]')
