import re

def format_response(text: str) -> str:
    """
    Format teks keluaran AI agar lebih rapi di tampilan Streamlit.
    """
    if not text:
        return "_(Tidak ada respon dari AI)_"

    # Ubah tanda bintang (*) jadi bullet point Streamlit
    formatted = re.sub(r"^\* ", "- ", text, flags=re.MULTILINE)

    # Pisahkan paragraf
    formatted = formatted.replace("\n\n", "\n\n")

    return formatted.strip()
