import streamlit as st
import pickle
import pandas as pd

with open('./src/best_model.pkl', 'rb') as file:
    best_model = pickle.load(file)

def run():
    # Pembuatan from
    with st.form(key='attrition_predict'):
        st.write('### Data Personal')
        
        age = st.number_input('Age', min_value=17, max_value=70, value=27, step=1, help='Usia karyawan')
        
        gender = st.selectbox('Gender', ('Female', 'Male'), index=1)
        
        maritialstatus = st.selectbox('Maritialstatus', ('Single', 'Married', 'Divorced'), index=1)
        
        education_levels = {'High School or Equivalent': 1,'Vocational': 2,'Bachelor': 3,"Master's Degree": 4,'Doctoral Degree': 5}
        education_options = list(education_levels.keys())
        education = st.selectbox('Educations', education_options, index=2)
        education_numeric = education_levels[education]
        
        distance = st.number_input('Distance', min_value=1, max_value=50, value=10, step=1, help='Jarak tempuh ke tempat kerja')
        
        educationfield = st.selectbox('Educationfield', ('Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'), index=0)
        
        bussinesstravel = st.selectbox('Bussinesstravel', ('Travel_Rarely', 'Travel_Frequently', 'Non-Travel'), index=0)
        
        stock_option_levels = {'None': 0,'Low': 1,'Medium': 2,'High': 3}
        stock_option_options = list(stock_option_levels.keys())
        stock_option = st.selectbox('Stock Option Level', stock_option_options, index=1)
        stock_option_numeric = stock_option_levels[stock_option]
        
        st.markdown('---')
        
        
        
        st.write('### Data Pekerjaan')
        
        employeeNumber = st.number_input('Employenumber', min_value=1, max_value=100000, value=1, step=1, help='ID karyawan, harus angka')
        
        departemen = st.selectbox('Departemen', ('Sales', 'Research & Development', 'Human Resources'), index=0)
        
        joblevel_levels = {'Entry Level': 1,'Junior': 2,'Mid-Level': 3,'Senior': 4,'Executive / Top Management': 5}
        joblevel_options = list(joblevel_levels.keys())
        joblevel = st.selectbox('Job Level', joblevel_options, index=0)
        joblevel_numeric = joblevel_levels[joblevel]
        jobrole = st.selectbox('Jobrole', ('Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'), index=0)
        
        monthlyincome = st.number_input('Monthlyincome', min_value=500, max_value=50000, value=1500, step=1, help='Gaji bulanan')
        
        monthlyrate = st.number_input('Monthlyrate', min_value=600, max_value=80000, value=5000, step=1, help='Rate cost bulanan')
        
        dailyrate = st.number_input('Dailyrate', min_value=80, max_value=3000, value=800, step=1, help='Rate cost harian')
        
        hourrate = st.number_input('Hourrate', min_value=30, max_value=300, value=60, step=1, help='Rate cost perjam')
        
        overtime = st.selectbox('Overtime', ('Yes', 'No'), index=1)
        
        performance_rating_levels = {'Good': 3,'Excellent': 4}
        performance_rating_options = list(performance_rating_levels.keys())
        performance_rating = st.selectbox('Performance Rating', performance_rating_options, index=0)
        performance_rating_numeric = performance_rating_levels[performance_rating]
        
        numcompaniesworked = st.number_input('Numcompaniesworked', min_value=1, max_value=20, value=2, step=1, help='Jumlah perusahaan tempat bekerja sebelumnya')
        
        percentsalaryhike = st.number_input('Percentsalaryhike', min_value=1, max_value=100, value=10, step=1, help='Percentase kenaikan gaji')
        
        totalworkingyears = st.number_input('Totalworkingyears', min_value=1, max_value=80, value=5, step=1, help='Total waktu bekerja')
        
        trainingtimeslastyear = st.number_input('Trainingtimeslastyear', min_value=0, max_value=80, value=1, step=1, help='Waktu terakhir mendapat pelatihan')
        
        yearsatcompany= st.number_input('Yearsatcompany', min_value=0, max_value=80, value=1, step=1, help='Lama tahun berada di perusahaan')
        
        yearsincurrentrole= st.number_input('Yearsincurrentrole', min_value=0, max_value=80, value=1, step=1, help='Lama tahun dengan pekerjaan yang sama')
        
        yearssinceLastpromotion= st.number_input('YearssinceLastpromotion', min_value=0, max_value=80, value=1, step=1, help='Lama tahun mendapat promosi')
        
        yearswithcurrmanager= st.number_input('Yearswithcurrmanager', min_value=0, max_value=80, value=1, step=1, help='Lama tahun bekerja dengan manager saat ini')
        
        st.markdown('---')
        
        
        
        st.write('### Penilaian Pribadi Karyawan')
        
        env_satisfaction_levels = {'Low': 1,'Medium': 2,'High': 3,'Very High': 4}
        env_satisfaction_options = list(env_satisfaction_levels.keys())
        env_satisfaction = st.selectbox('Environment Satisfaction', env_satisfaction_options, index=2)
        env_satisfaction_numeric = env_satisfaction_levels[env_satisfaction]

        job_involvement_levels = {'Low': 1,'Medium': 2,'High': 3,'Very High': 4}
        job_involvement_options = list(job_involvement_levels.keys())
        job_involvement = st.selectbox('Job Involvement', job_involvement_options, index=2)
        job_involvement_numeric = job_involvement_levels[job_involvement]
        
        job_satisfaction_levels = {'Low': 1,'Medium': 2,'High': 3,'Very High': 4}
        job_satisfaction_options = list(job_satisfaction_levels.keys())
        job_satisfaction = st.selectbox('Job Satisfaction', job_satisfaction_options, index=2)
        job_satisfaction_numeric = job_satisfaction_levels[job_satisfaction]
        
        relationship_satisfaction_levels = {'Low': 1,'Medium': 2,'High': 3,'Very High': 4}
        relationship_satisfaction_options = list(relationship_satisfaction_levels.keys())
        relationship_satisfaction = st.selectbox('Relationship Satisfaction', relationship_satisfaction_options, index=2)
        relationship_satisfaction_numeric = relationship_satisfaction_levels[relationship_satisfaction]
        
        work_life_balance_levels = {'Bad': 1,'Good': 2,'Better': 3,'Best': 4}
        work_life_balance_options = list(work_life_balance_levels.keys())
        work_life_balance = st.selectbox('Work Life Balance', work_life_balance_options, index=2)
        work_life_balance_numeric = work_life_balance_levels[work_life_balance]
        
        submitted = st.form_submit_button('Predict')
        
        # Make data to inference
        data_inf = {
        'Age' : age,
        'BusinessTravel' : bussinesstravel,
        'DailyRate' : dailyrate,
        'Department' : departemen,
        'DistanceFromHome' : distance,
        'Education' : education_numeric,
        'EducationField' : educationfield,
        'EmployeeNumber' : employeeNumber,
        'EnvironmentSatisfaction' : env_satisfaction_numeric,
        'Gender' : gender,
        'HourlyRate' : hourrate,
        'JobInvolvement' : job_involvement_numeric,
        'JobLevel' : joblevel_numeric,
        'JobRole' : jobrole,
        'JobSatisfaction' : job_satisfaction_numeric,
        'MaritalStatus' : maritialstatus,
        'MonthlyIncome' : monthlyincome,
        'MonthlyRate' : monthlyrate,
        'NumCompaniesWorked' : numcompaniesworked,
        'OverTime' : overtime,
        'PercentSalaryHike' : percentsalaryhike,
        'PerformanceRating' : performance_rating_numeric,
        'RelationshipSatisfaction' :  relationship_satisfaction_numeric,
        'StockOptionLevel' : stock_option_numeric,
        'TotalWorkingYears' : totalworkingyears,
        'TrainingTimesLastYear' : trainingtimeslastyear,
        'WorkLifeBalance' : work_life_balance_numeric,
        'YearsAtCompany' : yearsatcompany,
        'YearsInCurrentRole' : yearsincurrentrole,
        'YearsSinceLastPromotion' : yearssinceLastpromotion,
        'YearsWithCurrManager' : yearswithcurrmanager
        }

        # Make dataframe
        data_inf = pd.DataFrame([data_inf])
        data_inf
    
    if submitted:
        y_pred_inf = best_model.predict(data_inf)
        if y_pred_inf == 1:
            prediction = 'Yes'
        else:
            prediction = 'No'
        st.write('# Prediction Attriction :', str(prediction))
        
if __name__ == '__main__':
    run()