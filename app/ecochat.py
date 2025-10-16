import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from utils.prompt_builder import build_prompt
from utils.formatters import format_response

# Load .env file
load_dotenv()

# Konfigurasi API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("API key tidak ditemukan. Pastikan sudah diset di file .env sebagai GEMINI_API_KEY.")
else:
    genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-1.5-flash"

# Konfigurasi tampilan Streamlit
st.set_page_config(page_title="EcoChat – AI Konsultan Pengelolaan Sampah", layout="wide")

# Header
st.title("♻️ EcoChat – AI Konsultan Pengelolaan Sampah")
st.write("Solusi cerdas untuk mendukung **pengelolaan sampah berkelanjutan** dan masa depan yang lebih hijau 🌱")

# Sidebar
with st.sidebar:
    st.header("🔧 Pengaturan")
    user_name = st.text_input("Nama pengguna", value="Eco User")
    focus_area = st.selectbox(
        "Fokus konsultasi",
        ["Pengelolaan Sampah Rumah Tangga", "Daur Ulang", "Pemilahan Sampah", "Inovasi Teknologi Hijau"]
    )
    tone = st.selectbox("Gaya respon AI", ["Formal", "Santai", "Instruktif"], index=0)
    st.info("Gunakan fitur ini untuk berdialog langsung dengan AI yang fokus pada pengelolaan lingkungan.")

# Input utama
user_input = st.text_area("💬 Tanyakan sesuatu seputar pengelolaan sampah:", height=150)

if st.button("Kirim Pertanyaan"):
    if not user_input.strip():
        st.warning("Harap masukkan pertanyaan terlebih dahulu.")
    else:
        with st.spinner("🤖 EcoChat sedang berpikir..."):
            try:
                # Bangun prompt dinamis
                prompt = build_prompt(user_name, user_input, focus_area, tone)

                # Panggil model Gemini
                model = genai.GenerativeModel(MODEL_NAME)
                response = model.generate_content(prompt)

                formatted_output = format_response(response.text)
                st.success("✅ Jawaban dari EcoChat:")
                st.markdown(formatted_output)

            except Exception as e:
                st.error(f"Terjadi kesalahan: {str(e)}")

# Footer
st.markdown("---")
st.caption("© 2025 EcoChat – Powered by Google Gemini | Built with Streamlit")
