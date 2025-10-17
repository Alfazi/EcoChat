import re

def format_response(text: str) -> str:
    if not text:
        return "_(Tidak ada respon dari AI)_"

    formatted = re.sub(r"^\* ", "- ", text, flags=re.MULTILINE)
    formatted = formatted.replace("\n\n", "\n\n")

    return formatted.strip()
