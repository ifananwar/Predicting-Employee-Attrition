import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
    # Judul
    st.title('📊 HR Analytics Predicting Employee Attrition')
    
    image= Image.open('./src/image_1.jpg')
    st.image(image, caption='HR Analytics')
    
    st.markdown("""***HR analytics*** adalah process untuk menganalisa sumber daya manusia untuk meningkatkan performa dari suatu organisasi. Proces HR analytics bisa berupa menganalisa bakat, pekerja, ataupun calon pekerja. Dengan demikian dapat diperoleh bukti terukur secara objektif bagaimana SDM berkontribusi terhadap orginanisasi. Kinerja organisasi sangat bergantung pada kualitas pekerjanya. Berberapa tantangan yang harus dihadapi organisasi akibat pergantian karyawan adalah: """)

    st.subheader("🔍 Mengapa HR Analytics Penting?")
    st.markdown("""
    Kinerja organisasi sangat bergantung pada **kualitas dan stabilitas karyawannya**. Salah satu tantangan besar dalam manajemen SDM adalah **pergantian karyawan (employee attrition)** yang membawa dampak negatif seperti:

    - 💸 **Biaya pelatihan** dan waktu untuk pekerja baru.
    - 🧠 Kehilangan **pengalaman dan produktivitas**.
    - 📉 Dampak pada **produktivitas tim** dan morale.
    - 💼 Gangguan pada **lingkungan kerja** yang stabil.

    Dengan HR analytics, kita bisa:

    - 📈 Mendeteksi **pola-pola karyawan yang berpotensi keluar**.
    - 🧑‍💼 Mengambil langkah **proaktif dan humanis**, seperti check-in informal, stay interview.
    - 🛠️ Melakukan **root cause analysis** dan perbaikan sistemik: career path, rotasi, reward system.

    > Dengan pendekatan ini, HR tidak hanya reaktif terhadap turnover, tapi menjadi **mitra strategis** dalam retensi dan produktivitas.
    """)

    # Menyimpan Dataframe
    df = pd.read_csv('./src/dataset.csv')
    
    st.subheader("🔍 Exploratory Data Analysis")
    
    st.write('Menemukan pola dalam data melalui visualisasi dan menungkap rahasia tersembunyi data melalui grafik, analisis, dan diagram')
    st.write('**Data without analysis is just noise**')
    
    st.write('### Apakah Income merupakan alasan utama keluarnya seseorang ?')
    attrition_yes = df[df['Attrition'] == 'Yes']['MonthlyIncome']
    attrition_no = df[df['Attrition'] == 'No']['MonthlyIncome']
    fig = plt.figure(figsize=(15,5))
    plt.hist(attrition_no, bins=50, color='skyblue', edgecolor='black', alpha=0.6, label='Attrition = No')
    plt.hist(attrition_yes, bins=50, color='red', edgecolor='black', alpha=0.6, label='Attrition = Yes')
    plt.title('MonthlyIncome vs Attrition')
    plt.xlabel('MonthlyIncome')
    plt.ylabel('Count')
    plt.legend(title='Keterangan')
    st.pyplot(fig)
    st.write('**Analisis :** Pada monthly income dibawah 6.000 menunjukkan karyawan cenderung keluar dan berganti pekerjaan, mereka keluar biasanya mencari income yang lebih tinggi, tapi di angka 10.000 terjadi lonjakan kecil dimana ini dapat diartikan kelas menengah yang ingin mendapatkan standar pendapatan lebih baik.')

    st.write('### Apakah lingkungan kerja yang buruk berpengaruh terhadap keluarnya karyawan ?')
    envi = df[df['Attrition'] == 'Yes']
    envi_count = envi.groupby('EnvironmentSatisfaction')['Attrition'].count().reset_index(name='count_enviroment')
    fig = plt.figure(figsize=(15,5))
    sns.barplot(data=envi_count, x='EnvironmentSatisfaction', y='count_enviroment', hue='EnvironmentSatisfaction')
    plt.title('Environment Satisfaction vs Attrition')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xlabel('Environment Satisfaction')
    plt.ylabel('Count')
    st.pyplot(fig)
    st.markdown("""Keterangan :
    - Low : 1
    - Medium : 2
    - High : 3
    - Very High : 4""")
    st.write('**Analisis :** sekitar 70 orang keluar dengan alasan lingkugan yang buruk ini menindikasikan lingkungan dapat menjadi alasan seseorang berhenti bekerja, Tapi yang menarik pada lingkungan yang nyaman atau terlalu nyaman orang-orang juga akan keluar untuk mencari tantangan pada pekerjaan baru.')
    
    
    st.write('### Departemen apa yang paling banyak orang keluar ?')
    department = df[df['Attrition'] == 'Yes']
    department_count = department.groupby('Department')['Attrition'].count().reset_index(name='count_departement')
    fig = plt.figure(figsize=(15,5))
    plt.pie(x = department_count['count_departement'], labels =department_count['Department'], autopct='%1.1f%%') 
    st.pyplot(fig)
    st.write('**Analisis :** Sayangnya hanya ada tiga departemen untuk di analisis pada dataset ini, namun dari populasi orang yang berhenti bekerja departemen paling banyak adalah RnD dan Sales, kemungkinan pekerjaan yang memiliki target dan tingkat kerja yang berat dapat membuat orang keluar, Departemen Human Resources cenderung melakukan pekerjaan administratif sehingga orang yang berhenti sangat kecil.')
    
    st.write('### Bagaimana durasi kerja saat ini berdampak pada keluarnya karyawan?')
    fig = plt.figure(figsize=(15,5))
    duration = df[df['Attrition'] == 'Yes']
    duration_count = duration.groupby('YearsInCurrentRole')['Attrition'].count().reset_index(name='Count_YearsInCurrentRole')
    sns.lineplot(x=duration_count['YearsInCurrentRole'], y=duration_count['Count_YearsInCurrentRole'])
    plt.title('Years In Current Role')
    plt.xlabel('Years')
    plt.ylabel('Count')
    st.pyplot(fig)
    st.write('**Analisis :** Disini orang yang bekerja dibawah 1 tahun punya kecenderungan berhenti yang tinggi, hal ini karena biasanya orang yang baru masuk melewati masa onboarding dan awal beradaptasi dengan buadaya perusahaan, sehingga memiliki kemungkinan ketidak cocokan di awal, hal ini menurun pada 1 tahun dan kembali naik di tahun ke-2, kemungkinan karena kontrak yang memiliki jangka waktu satu tahun untuk berhenti. Setelah melewati tahun ke-2 karyawan yang berhenti mengalami penurunan, namun di tahun ke-7 naik kembali, karena karyawan sudah berpengalaman dan mengejar opportunity baru.')
    
    st.write('### Apakah orang resign karena jarak ker rumah yang jauh ?')
    fig = plt.figure(figsize=(15,5))
    attrition_yes = df[df['Attrition'] == 'Yes']['DistanceFromHome']
    attrition_no = df[df['Attrition'] == 'No']['DistanceFromHome']
    plt.hist(attrition_no, bins=30, color='skyblue', edgecolor='black', alpha=1, label='Attrition = No')
    plt.hist(attrition_yes, bins=30, color='red', edgecolor='black', alpha=1, label='Attrition = Yes')
    plt.title('DistanceFromHome vs Attrition')
    plt.xlabel('DistanceFromHome')
    plt.ylabel('Count')
    plt.legend(title='Keterangan')
    st.pyplot(fig)
    st.write('**Analisis :** Terlihat jarak tidak terlalu berpengaruh dengan keluarnya karyawan pada perusahaan ini, pada 1-2 KM jaraknya justru tinggi, tapi hal ini wajar jika dilihat dari jumlah karyawan yang berada pada jarak 1-2 km. Karena data antara karyawan yang keluar dan bertahan tidak seimbang.')
    
    st.write('### Apakah worklife balance yang menjadi masalah ?')
    fig = plt.figure(figsize=(15,5))
    worklifebalance = df[df['Attrition'] == 'Yes']
    worklifebalance_count = worklifebalance.groupby('WorkLifeBalance')['Attrition'].count().reset_index(name='count_WorkLifeBalance')
    sns.barplot(data=worklifebalance_count, x='WorkLifeBalance', y='count_WorkLifeBalance', hue='WorkLifeBalance')
    plt.title('WorkLifeBalance vs Attrition')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xlabel('WorkLifeBalance')
    plt.ylabel('Count')
    st.pyplot(fig)
    st.write('**Analisis :** Disini terlihat bahwa tingkat work life balance yang rendah dan tinggi malah memiliki jumlah karyawan yang keluar lebih sedikit. Pada work life balance yangburuj biasanya karyawan lebih fokus pada pekerjaan dan dapat terbiasa beradaptasi, namun saat meraksan work life balance yang lebih baik karyawan cenderung keluar untuk mencari yang lebih baik, hal ini bisa dilihat saat karyawan merasa sangat baik pada work life balance dia akan puas dan angka karyawan yang keluar berhenti')

    st.write('### Apakah kenaikan gaji efektif membuat karyawan bertahan ?')
    fig = plt.figure(figsize=(15,5))
    attrition_yes = df[df['Attrition'] == 'Yes']['PercentSalaryHike']
    attrition_no = df[df['Attrition'] == 'No']['PercentSalaryHike']
    plt.hist(attrition_no, bins=15, color='skyblue', edgecolor='black', alpha=1, label='Attrition = No')
    plt.hist(attrition_yes, bins=15, color='red', edgecolor='black', alpha=1, label='Attrition = Yes')
    plt.title('Percent Salary Hike vs Attrition')
    plt.xlabel('Percent Salary Hike')
    plt.ylabel('Count')
    plt.legend(title='Keterangan')
    st.pyplot(fig)
    st.write('**Analisis :** Persentase kenaikan gaji yang tinggi memotivasi karyawan untuk tetap bertahan di dalam perusahaan, hal ini dapat dilihat trend kenaikan gaji yang cenderung menurun saat presentase kenaikannya tinggi')
    
    
if __name__ == '__main__':
    run()