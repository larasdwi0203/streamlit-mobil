import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil', value=2019.0)
mileage = st.number_input('Input Km Mobil', value=5000.0)
tax = st.number_input('Input Pajak Mobil', value=145.0)
mpg = st.number_input('Input Konsumsi BBM Mobil', value=30.20)
engineSize = st.number_input('Input Engine Size', value=2.0)

def format_koma(angka):
    return f"{float(angka):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def format_rupiah(angka):
    return f"Rp {format_koma(angka)}"

nilai_ponds = 0.0
nilai_idr = 0.0

if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    nilai_ponds = float(predict[0])
    nilai_idr = nilai_ponds * 19000

st.write('Estimasi harga mobil bekas dalam Ponds :')
st.metric(label="value", value=format_koma(nilai_ponds))

st.write('Estimasi harga mobil bekas dalam IDR (Juta) :')
st.metric(label="value", value=format_rupiah(nilai_idr))
