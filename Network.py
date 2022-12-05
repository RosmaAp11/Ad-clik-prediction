import pickle
import streamlit as st

# membaca model
Network_model =  pickle.load(open('Network_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi pelanggan mengklik iklan')

Gender = st.text_input('Jenis Kelamin')

Age = st.text_input('Masukan usia konsumen')

EstimatedSalary = st.text_input('Masukan jumlah rata-rata penghasilan pelanggan')


# code untuk kelompok jenis jaringan
Network_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    Network_prediction = Net_model.predict([[Gender, Age, EstimatedSalary]])
    
    if(Network_prediction[0] == 1):
        Network_diagnosis = 'Pelanggan Mengklik Iklan'
    else :
        Network_diagnosis = 'Pelanggan Tidak Mengklik Iklan'

    st.success(Network_diagnosis)
