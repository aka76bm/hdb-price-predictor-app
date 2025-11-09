import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st

def validate_inputs(input_data):
    """Validate user inputs"""
    errors = []
    
    # Check required fields
    required_fields = ['town', 'flat_type', 'storey_range', 'floor_area_sqm', 
                      'flat_model', 'lease_commence_date']
    
    for field in required_fields:
        if field not in input_data or input_data[field] is None:
            errors.append(f"Missing required field: {field}")
    
    # Validate numerical values
    if 'floor_area_sqm' in input_data:
        if not (30 <= input_data['floor_area_sqm'] <= 200):
            errors.append("Floor area must be between 30 and 200 sqm")
    
    if 'lease_commence_date' in input_data:
        current_year = datetime.now().year
        if not (1966 <= input_data['lease_commence_date'] <= current_year):
            errors.append("Lease commence year must be between 1966 and current year")
    
    return errors

def format_currency(amount):
    """Format currency with commas"""
    return f"${amount:,.2f}"

def calculate_remaining_lease(lease_commence_year):
    """Calculate remaining lease in years"""
    current_year = datetime.now().year
    years_passed = current_year - lease_commence_year
    remaining_lease = 99 - years_passed
    return max(0, remaining_lease)

def get_town_coordinates(town_name, postal_data):
    """Get coordinates for a town from postal data"""
    if town_name in postal_data:
        return postal_data[town_name].get('coordinates', [1.3521, 103.8198])
    return [1.3521, 103.8198]  # Default to Singapore coordinates

 @st.cache_data
def load_sample_data():
    """Load sample data for demonstration"""
    return pd.DataFrame({
        'town': ['ANG MO KIO', 'BEDOK', 'TAMPINES'],
        'flat_type': ['4 ROOM', '5 ROOM', '3 ROOM'],
        'storey_range': ['10 TO 12', '07 TO 09', '04 TO 06'],
        'floor_area_sqm': [105, 125, 85],
        'flat_model': ['Model A', 'Improved', 'New Generation'],
        'lease_commence_date': [1990, 1985, 2000]
    })