from flask import Flask,jsonify
from flask_cors import CORS
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv
from llm_handler import predict_risk

load_dotenv()

app=Flask(__name__)
CORS(app)

def get_latest_data():
    data_path = os.getenv("BLOOD_DATA_PATH", "blood_data.csv")
    print(data_path)
    try:
        if not os.path.exists(data_path):
            return None
            
        df = pd.read_csv(data_path)
        print(df)
        if df.empty:
            return None
            
        latest_data = df.iloc[-1].to_dict()
        latest_data['Timestamp'] = pd.to_datetime(
            latest_data['Timestamp']
        ).strftime('%Y-%m-%d %H:%M:%S')
        
        return latest_data
    except Exception as e:
        app.logger.error(f"Data retrieval error: {str(e)}")
        return None
@app.route("/get-data",methods=["GET"])
def data_endpoint():

    data = get_latest_data()
    print(data)
    if not data: 
        return jsonify({"error":"No Data Available"}),404
    
    data["clot_risk"]=predict_risk(data)
    
    return jsonify(data)

if __name__=="__main__":
    port=int(os.getenv("PORT",5000))
    debug_mode = os.getenv("FLASK_DEBUG","False").lower()=="true"
    app.run(debug=debug_mode,port=port)