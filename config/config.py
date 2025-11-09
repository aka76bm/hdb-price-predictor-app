import os
from datetime import datetime

# App Configuration
APP_CONFIG = {
    "APP_NAME": "HDB Resale Price Predictor",
    "VERSION": "1.0.0",
    "DESCRIPTION": "Predict HDB resale prices using machine learning",
    "AUTHOR": "Your Name",
    "LAST_UPDATED": "2024-12-19"
}

# Model Configuration
MODEL_CONFIG = {
    "MODEL_PATH": "model.bst",
    "SCALER_PATH": "scaler.joblib",
    "POSTAL_DATA_PATH": "postal_data.json",
    "FEATURE_NAMES": [
        'town', 'flat_type', 'storey_range', 'floor_area_sqm', 
        'flat_model', 'lease_commence_date'
    ]
}

# Map Configuration
MAP_CONFIG = {
    "MAP_URL": "https://your-username.github.io/hdb-resale-map/hdb_resale_price_map_clickable.html",
    "MAP_HEIGHT": 600,
    "DEFAULT_LOCATION": [1.3521, 103.8198],  # Singapore coordinates
    "DEFAULT_ZOOM": 11
}

# UI Configuration
UI_CONFIG = {
    "THEME": {
        "PRIMARY_COLOR": "#1f77b4",
        "BACKGROUND_COLOR": "#f0f2f6",
        "SECONDARY_COLOR": "#ff4b4b"
    },
    "LAYOUT": "wide",
    "INITIAL_SIDEBAR_STATE": "expanded"
}

def get_config():
    """Get configuration based on environment"""
    return {
        "app": APP_CONFIG,
        "model": MODEL_CONFIG,
        "map": MAP_CONFIG,
        "ui": UI_CONFIG
    }