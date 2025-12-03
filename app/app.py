import streamlit as st
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="Modeling Animal Shelter Outcomes", layout="wide")

tab1, tab2 = st.tabs(["Project Overview", "Results Visualization"])

with tab1:
    st.title("Modeling Animal Shelter Outcomes with MLPs and Time Series")
    st.write("""
    Animal shelters often face challenges with properly managing capacity and 
    improving adoption outcomes while only having limited resources. This project 
    aims to predict adoption outcomes to help optimize resources and improve 
    animal welfare. Using the Austin Animal Center Outcomes dataset, which 
    contains detailed records of ~173k animals from 2013-2025, including 
    attributes such as breed, color, age, sex, and outcome type. We explore 
    patterns that influence whether an animal is adopted, transferred, 
    returned to owner, euthanized, or has died. We additionally look into the 
    seasonal patterns within animal adoption over time.
    \n
    To address this problem, the project uses two approaches. First, a 
    multi-layer perceptron (MLP) model in Python, which predicts individual 
    animal outcomes based on their characteristics, capturing relationships that 
    traditional methods often miss. Second, time series models, which analyzes 
    adoption and transfer outcome counts over time to identify seasonal and long-term trends 
    that may help shelters anticipate capacity needs.
    """)
    image = Image.open("app/shelter_img.jpg")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image, width=700)

with tab2:
    st.header("Model Results")
    st.write("""
    After training and evaluation on the test set, the MLP model 
    achieved the following performance metrics:\n
    - Accuracy: 0.711\n
    - Precision: 0.687\n
    - Recall: 0.711\n
    - F1 Score: 0.683\n
    Below is an interactive confusion matrix, describing the true versus predicted 
    values for the animal outcomes. The graph shows that the MLP reliably 
    predicts common outcomes like ‘Adoption’ and ‘Transfer,’ while rarer classes 
    such as ‘Euthanasia’ and ‘Died’ are often misclassified. Some errors, like 
    confusing ‘Return to Owner’ with ‘Adoption,’ may have resulted from class imbalance.
    """)

    components.html(open("app/confusion_matrix.html", "r").read(), height=500)
