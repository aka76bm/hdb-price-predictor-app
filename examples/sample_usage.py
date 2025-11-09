"""
Example usage of the HDB Price Predictor
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.helpers import validate_inputs, format_currency, calculate_remaining_lease

def main():
    """Example usage of helper functions"""
    
    # Sample input data
    sample_input = {
        'town': 'ANG MO KIO',
        'flat_type': '4 ROOM',
        'storey_range': '10 TO 12',
        'floor_area_sqm': 105,
        'flat_model': 'Model A',
        'lease_commence_date': 1990
    }
    
    # Validate inputs
    errors = validate_inputs(sample_input)
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("✅ Input validation passed!")
    
    # Calculate remaining lease
    remaining_lease = calculate_remaining_lease(sample_input['lease_commence_date'])
    print(f"Remaining lease: {remaining_lease} years")
    
    # Format currency
    sample_price = 450000.50
    print(f"Formatted price: {format_currency(sample_price)}")

if __name__ == "__main__":
    main()