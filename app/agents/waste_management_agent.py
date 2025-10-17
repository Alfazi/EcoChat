import google.generativeai as genai
import os
from utils.prompt_builder import build_prompt
from utils.formatters import format_response

class WasteManagementAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("models/gemini-2.5-flash")

    def respond(self, user_name: str, question: str, tone: str) -> str:
        prompt = build_prompt(
            user_name=user_name,
            question=question,
            focus_area="Pengelolaan sampah rumah tangga dan pengurangan limbah sehari-hari",
            tone=tone
        )
        response = self.model.generate_content(prompt)
        return format_response(response.text)
