# app.py (Streamlit frontend)
import streamlit as st
# from your_model_prediction_module import predict_skin_disease 
# আপনার মডেল প্রেডিকশন ফাংশন এখানে ইম্পোর্ট করুন
import tempfile
import os

st.title("ত্বকের রোগ নির্ণয় টুল")
st.write("আপনার ত্বকের সমস্যার ছবি আপলোড করে রোগ নির্ণয় করুন।")

uploaded_file = st.file_uploader("একটি ছবি আপলোড করুন...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # আপলোড করা ফাইল সেভ করুন যাতে মডেল এটি লোড করতে পারে
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name

    st.image(uploaded_file, caption='আপলোড করা ছবি', use_column_width=True)
    st.write("")
    st.write("বিশ্লেষণ করা হচ্ছে...")

    # disease, confidence = predict_skin_disease(temp_path)

    # st.success(f"সম্ভাব্য রোগ: **{disease}**")
    # st.info(f"আত্মবিশ্বাস: **{confidence*100:.2f}%**")

    os.remove(temp_path) # টেম্পোরারি ফাইল মুছে দিন
