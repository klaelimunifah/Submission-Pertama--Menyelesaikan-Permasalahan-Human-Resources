import pandas as pd
import streamlit as st
import joblib
from category_encoders import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Fungsi data_preparation(data_input)
''' Mengolah data input yang akan diprediksi'''
def data_preparation(data_input):
    employee_data = pd.read_csv("employee_data.csv")
    employee_data = employee_data.drop(columns = ['EmployeeId', 'Attrition', 'Status'])
    data_prep = pd.concat([employee_data, data_input])
    data_prep_cat = data_prep.select_dtypes(include = ['object'])
    preprocessor = ColumnTransformer(transformers=[('onehot', OneHotEncoder(), data_prep_cat.columns)], remainder='passthrough')
    X_transformed = preprocessor.fit_transform(data_prep)
    output = pd.DataFrame(X_transformed, columns=['1', '2', '3','4', '5', '6',
                                                  '7', '8', '9','10', '11', '12',
                                                  '13', '14', '15','16', '17', '18',
                                                  '19', '20', '21','22', '23', '24',
                                                  '25', '26', '27','28', '29', '30',
                                                  '31', '32', '33','34', '35', '36',
                                                  '37', '38', '39','40', '41', '42',
                                                  '43', '44', '45','46', '47', '48',
                                                  '49', '50', '51','52', '53', '54'])
    nunique = output.nunique()
    cols_to_drop = nunique[nunique == 1].index
    output = output.drop(cols_to_drop, axis=1)
    output = output.tail(1).to_numpy()
    return output

# Main
st.title("Jaya Jaya Maju Employee Status Prediction")                   # Judul

# Input data yang akan diprediksi
Age = st.number_input("Age",
                      min_value = 18,
                      max_value= 60,
                      value= None,
                      step = 1)

Gender = st.selectbox("Gender",
                      ("Male", "Female"))

Edutxt = st.selectbox("Education",
                         ("Below College", "College", "Bachelor", "Master", "Doctor"))

if (Edutxt == "Below College"):
    Education = 1
elif (Edutxt == "College"):
    Education = 2
elif (Edutxt == "Bachelor"):
    Education = 3
elif (Edutxt == "Master"):
    Education = 4
else:
    Education = 5

EducationField = st.selectbox("Education Field",
                               ("Human Resources", "Life Sciences", "Marketing",
                                "Medical", "Technical Degree", "Other"))

JobLevel = st.selectbox("Job Level",
                               ("1", "2", "3", "4", "5"))

Department = st.selectbox("Department",
                               ("Human Resources", "Research & Development", "Sales"))

JobRole = st.selectbox("JobRole",
                               ("Healthcare Representative", "Human Resources",
                                "Laboratory Technician", "Manager",
                                "Manufacturing Director", "Research Director",
                                "Research Scientist", "Sales Executive", "Sales Representative"))

BusinessTravel = st.selectbox("Business Travel",
                               ("Non-Travel", "Travel_Rarely", "Travel_Frequently"))

MonthlyIncome = st.number_input("Monthly Income (USD)",
                      value=None,
                      step = 1)

SalaryCategory = st.selectbox("Salary Category",
                               ("Under 5000", "5000-10000", "10000-15000", "Above 15000"))

PercentSalaryHike = st.number_input("Percent Salary  Hike (%)",
                      min_value = 0,
                      max_value= 100,
                      value=None,
                      step = 1)

TotalWorkingYears = st.number_input("Total Working Years",
                      min_value = 0,
                      max_value= 50,
                      value=None,
                      step = 1)

MaritalStatus = st.selectbox("Marital Status",
                               ("Single", "Married", "Divorced"))

PerformanceRating = st.select_slider("Performance Rating",
                                     options=["1", "2", "3", "4", "5"],
                                     label_visibility="visible")

JobSatisfaction = st.select_slider("Job Satisfaction",
                                     options=["1", "2", "3", "4", "5"],
                                     label_visibility="visible")
EnvironmentSatisfaction = st.select_slider("Environment Satisfaction",
                                     options=["1", "2", "3", "4", "5"],
                                     label_visibility="visible")
RelationshipSatisfaction = st.select_slider("RelationshipSatisfaction",
                                     options=["1", "2", "3", "4", "5"],
                                     label_visibility="visible")
WorkLifeBalance = st.select_slider("Work Life Balance",
                                     options=["1", "2", "3", "4", "5"],
                                     label_visibility="visible")

# Menyimpan data yang akan diprediksi dalam sebuah dataframe
data = [[Age, Gender, Education,
       EducationField, Edutxt, int(JobLevel), Department, JobRole,
       BusinessTravel, MonthlyIncome, SalaryCategory,
       PercentSalaryHike, TotalWorkingYears, MaritalStatus,
       int(PerformanceRating), int(JobSatisfaction), int(EnvironmentSatisfaction),
       int(RelationshipSatisfaction), int(WorkLifeBalance)]]
data_df = pd.DataFrame(data, columns=[ 'Age', 'Gender', 'Education',
       'EducationField', 'Edutxt', 'JobLevel', 'Department', 'JobRole',
       'BusinessTravel', 'MonthlyIncome', 'SalaryCategory',
       'PercentSalaryHike', 'TotalWorkingYears', 'MaritalStatus',
       'PerformanceRating', 'JobSatisfaction', 'EnvironmentSatisfaction',
       'RelationshipSatisfaction', 'WorkLifeBalance'])

# Load Model Machine Learning
model = joblib.load("employee_model.sav", mmap_mode="r")

# Menu prediksi
if st.button("PREDICT"):
    with st.container():
        input = data_preparation(data_df)
        prediction = model.predict(input)
        if prediction == 1:
            st.subheader('Employee Status: Inactive',  divider='red')
        else:
            st.subheader('Employee Status: Active',  divider='blue')
            
        if st.button("Reset"):
            st.rerun()
