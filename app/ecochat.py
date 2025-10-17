import os
import streamlit as st
from dotenv import load_dotenv
from agents.main_agent import EcoChatAgent

# Load .env file
load_dotenv()

<<<<<<< HEAD
st.set_page_config(page_title="EcoChat AI Multi-Agent", layout="wide")
=======
# Konfigurasi API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("API key tidak ditemukan. Pastikan sudah diset di file .env sebagai GEMINI_API_KEY.")
else:
    genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-1.5-flash"

# Konfigurasi tampilan Streamlit
st.set_page_config(page_title="EcoChat – AI Konsultan Pengelolaan Sampah", layout="wide")
>>>>>>> parent of ae74db3 (change model)

# Header
st.title("♻️ EcoChat AI Multi-Agent Konsultan Pengelolaan Sampah")
st.write("Kini EcoChat dilengkapi sub-agent khusus untuk berbagai topik lingkungan 🌱")

# Sidebar
with st.sidebar:
    st.header("🔧 Pengaturan")
    user_name = st.text_input("Nama pengguna", value="Eco User")
    focus_area = st.selectbox(
        "Fokus konsultasi",
        [
            "Pengelolaan Sampah Rumah Tangga",
            "Daur Ulang",
            "Pemilahan Sampah",
            "Inovasi Teknologi Hijau"
        ]
    )
    tone = st.selectbox("Gaya respon AI", ["Formal", "Santai", "Instruktif"], index=0)

user_input = st.text_area("💬 Tanyakan sesuatu seputar pengelolaan sampah:", height=150)

if st.button("Kirim Pertanyaan"):
    if not user_input.strip():
        st.warning("Harap masukkan pertanyaan terlebih dahulu.")
    else:
        with st.spinner("🤖 EcoChat sedang menganalisis..."):
            agent = EcoChatAgent()
            answer = agent.handle_query(user_name, user_input, focus_area, tone)
            st.success("✅ Jawaban dari EcoChat:")
            st.markdown(answer)

st.markdown("---")
st.caption("© 2025 EcoChat Multi-Agent Powered by Google Gemini | Built with Streamlit")
