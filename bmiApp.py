import streamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ (Title สีเเดง)
st.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักเเละส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม:", min_value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0

#ส่วนที่ 3 สร้างปุ่มกดคำนวณ
if st.button("คำนวณค่า BMI 🎯"):
    # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณ BMI
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
