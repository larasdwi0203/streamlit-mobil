import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil', step=1, format='%d')
mileage = st.number_input('Input Km Mobil', step=100, format='%d')
tax = st.number_input('Input Pajak Mobil', step=5, format='%d')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    price_pounds = float(predict[0])
    price_idr = price_pounds * 19000

    formatted_pounds = f"{price_pounds:,.0f}".replace(",", ".")
    formatted_idr = f"{price_idr:,.0f}".replace(",", ".")

    st.success(f"Estimasi harga mobil bekas dalam Ponds : £ {formatted_pounds}")
    st.success(f"Estimasi harga mobil bekas dalam IDR : Rp {formatted_idr}")