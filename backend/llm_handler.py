import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables independently
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment variables")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

def predict_risk(data):
    """Analyzes blood data and returns clot risk prediction"""
    try:
        prompt = f"""
        Analyze these blood results for clotting risk:
        {json.dumps(data, indent=2)}
        
        Guidelines:
        - Platelets (x10³/µL): 150-450 [Normal]
        - Clotting Time (mins): 4-10 [Normal]
        - Fibrinogen (mg/dL): 200-400 [Normal]
        - D-Dimer (ng/mL): <0.5 [Normal]
        
        Return ONLY: "Low Risk", "Moderate Risk", or "Critical Risk".
        """
        
        response = model.generate_content(prompt)
        risk_level = response.text.strip()
        
        if risk_level not in {"Low Risk", "Moderate Risk", "High Risk"}:
            return "Unknown Risk"
        
        print(risk_level)
        return risk_level
    except Exception as e:
        # Consider adding logging here if needed
        return "Prediction Error"
