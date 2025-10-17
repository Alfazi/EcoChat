from agents.waste_management_agent import WasteManagementAgent
from agents.recycling_agent import RecyclingAgent
from agents.sorting_agent import SortingAgent
from agents.green_tech_agent import GreenTechAgent

class EcoChatAgent:
    def __init__(self):
        self.agents = {
            "Pengelolaan Sampah Rumah Tangga": WasteManagementAgent(),
            "Daur Ulang": RecyclingAgent(),
            "Pemilahan Sampah": SortingAgent(),
            "Inovasi Teknologi Hijau": GreenTechAgent()
        }

    def handle_query(self, user_name: str, question: str, focus_area: str, tone: str) -> str:
        selected_agent = self.agents.get(focus_area)
        if not selected_agent:
            return "_Area fokus tidak dikenali._"

        return selected_agent.respond(user_name, question, tone)
