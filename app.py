import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib
import json
from datetime import datetime
import requests

# Page configuration
st.set_page_config(
    page_title="HDB Resale Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .map-container {
        height: 600px;
        border-radius: 10px;
        overflow: hidden;
        margin: 1rem 0;
    }
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

class HDBPricePredictor:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.postal_data = None
        self.load_resources()
    
    def load_resources(self):
        """Load model, scaler, and postal data"""
        try:
            self.model = xgb.Booster()
            self.model.load_model('model.bst')
            self.scaler = joblib.load('scaler.joblib')
            with open('postal_data.json', 'r') as f:
                self.postal_data = json.load(f)
        except Exception as e:
            st.error(f"Error loading resources: {str(e)}")
    
    def preprocess_features(self, input_data):
        """Preprocess input features for prediction"""
        try:
            # Convert input to DataFrame
            features = pd.DataFrame([input_data])
            
            # Feature engineering (mirror training process)
            features['remaining_lease'] = 99 - (datetime.now().year - features['lease_commence_date'])
            features['floor_area_sqft'] = features['floor_area_sqm'] * 10.764
            
            # Scale features
            scaled_features = self.scaler.transform(features)
            
            return xgb.DMatrix(scaled_features)
        except Exception as e:
            st.error(f"Error in feature preprocessing: {str(e)}")
            return None

 @st.cache_resource
def load_predictor():
    return HDBPricePredictor()

def main():
    # Initialize predictor
    predictor = load_predictor()
    
    # Header
    st.markdown('<h1 class="main-header">🏠 HDB Resale Price Predictor</h1>', 
                unsafe_allow_html=True)
    
    # Sidebar for user inputs
    with st.sidebar:
        st.header("📋 Property Details")
        
        # Town selection
        towns = [
            "ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH",
            "BUKIT PANJANG", "BUKIT TIMAH", "CENTRAL AREA", "CHOA CHU KANG",
            "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST",
            "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL",
            "QUEENSTOWN", "SEMBAWANG", "SENGKANG", "SERANGOON", "TAMPINES",
            "TOA PAYOH", "WOODLANDS", "YISHUN"
        ]
        town = st.selectbox("Town", towns)
        
        # Flat type
        flat_types = ["2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE", "MULTI-GENERATION"]
        flat_type = st.selectbox("Flat Type", flat_types)
        
        # Storey range
        storey_ranges = [
            "01 TO 03", "04 TO 06", "07 TO 09", "10 TO 12", "13 TO 15",
            "16 TO 18", "19 TO 21", "22 TO 24", "25 TO 27", "28 TO 30",
            "31 TO 33", "34 TO 36", "37 TO 39", "40 TO 42", "43 TO 45",
            "46 TO 48", "49 TO 51"
        ]
        storey_range = st.selectbox("Storey Range", storey_ranges)
        
        # Floor area
        floor_area_sqm = st.slider("Floor Area (sqm)", 30, 200, 100)
        
        # Flat model
        flat_models = [
            "Improved", "New Generation", "Model A", "Standard", "Simplified",
            "Premium Apartment", "Maisonette", "Apartment", "Model A2",
            "DBSS", "Terrace", "Adjoined flat", "Model A-Maisonette",
            "Type S1", "Type S2", "Improved-Maisonette", "Multi Generation",
            "Premium Maisonette", "2-room", "3Gen"
        ]
        flat_model = st.selectbox("Flat Model", flat_models)
        
        # Lease commence date
        current_year = datetime.now().year
        lease_commence_date = st.slider("Lease Commence Year", 1966, current_year, 1990)
        
        # Prediction button
        predict_btn = st.button("🎯 Predict Resale Price", type="primary", use_container_width=True)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("💰 Price Prediction")
        
        if predict_btn and predictor.model is not None:
            # Prepare input data
            input_data = {
                'town': town,
                'flat_type': flat_type,
                'storey_range': storey_range,
                'floor_area_sqm': floor_area_sqm,
                'flat_model': flat_model,
                'lease_commence_date': lease_commence_date
            }
            
            # Make prediction
            try:
                dmatrix = predictor.preprocess_features(input_data)
                if dmatrix is not None:
                    prediction = predictor.model.predict(dmatrix)[0]
                    
                    # Display prediction
                    st.markdown(f"""
                    <div class="prediction-box">
                        <h3>Estimated Resale Price</h3>
                        <h2>${prediction:,.2f}</h2>
                        <p>Based on current market trends and similar properties</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Additional insights
                    st.subheader("📊 Market Insights")
                    st.info(f"""
                    - **Town**: {town}
                    - **Flat Type**: {flat_type}
                    - **Floor Area**: {floor_area_sqm} sqm
                    - **Lease Commenced**: {lease_commence_date}
                    """)
                    
            except Exception as e:
                st.error(f"Prediction error: {str(e)}")
        else:
            st.info("👈 Please fill in the property details and click 'Predict Resale Price'")
    
    with col2:
        st.header("🗺️ Transaction Map")
        st.markdown('<div class="map-container">', unsafe_allow_html=True)
        
        # External map URL - replace with your actual hosted map URL
        map_url = "https://your-username.github.io/hdb-resale-map/hdb_resale_price_map_clickable.html"
        
        try:
            # Embed external map
            st.components.v1.iframe(map_url, height=600, scrolling=True)
        except Exception as e:
            st.warning("Map is currently unavailable. Please try again later.")
            st.info("""
            The interactive map shows recent HDB resale transactions with:
            - Clickable markers for transaction details
            - Price information by location
            - Property characteristics
            """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <p>Data Source: Housing & Development Board (HDB) | Last Updated: 30-06-2025</p>
        <p>⚠️ Disclaimer: Predictions are estimates based on historical data and may not reflect actual transaction prices.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()