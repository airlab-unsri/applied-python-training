import streamlit as st

st.title("Simple Calculator 🧮")

angka_1 = st.number_input("Angka 1")
angka_2 = st.number_input("Angka 2")
operasi = st.radio(
    "Operasi",
    ["\+", "\-", "\*", "\/"],
)

if st.button("Hitung"):
    if operasi == "\+":
        hasil = angka_1 + angka_2
    elif operasi == "\-":
        hasil = angka_1 - angka_2
    elif operasi == "\*":
        hasil = angka_1 * angka_2
    elif operasi == "\/":
        hasil = angka_1 / angka_2
    st.write(f"Hasil: {hasil}")
