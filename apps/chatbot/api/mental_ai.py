import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class MentalHealthChat:
    def get_response(self, message):
        model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-pro
        response = model.generate_content(message)
        return response.text

