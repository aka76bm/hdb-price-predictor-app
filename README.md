# 🏠 HDB Resale Price Predictor App

A Streamlit web application that predicts Singapore HDB resale flat prices using machine learning. This app loads an XGBoost model and necessary data files directly from its local directory and displays an interactive transaction map.

![HDB Price Predictor](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-3776AB?style=for-the-badge&logo=xgboost&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

## ✨ Features

- **Interactive UI**: User-friendly input for property details via Streamlit
- **Local Model & Data**: Pre-trained XGBoost model with scaler and postal code data
- **Interactive Map**: Displays HDB resale transactions on an interactive map
- **Responsive Design**: Optimized for both desktop and mobile devices
- **Theme Toggle**: Light and Dark mode options
- **Dockerized**: Ready for containerization and deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- Git

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hdb-price-predictor-app.git
   cd hdb-price-predictor-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

### Docker Installation

1. **Build the Docker image**
   ```bash
   docker build -t hdb-predictor-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 hdb-predictor-app
   ```

## 📁 Project Structure

```
hdb-price-predictor-app/
├── app.py                 # Main Streamlit application
├── model.bst             # Pre-trained XGBoost model
├── scaler.joblib         # Feature scaler
├── postal_data.json      # Postal code data
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Docker ignore rules
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

## 🛠️ Configuration

The app uses the following configuration:

- **Model**: XGBoost Regressor
- **Features**: Town, Flat Type, Storey, Floor Area, Lease Commencement, etc.
- **Map**: Interactive Folium map hosted externally

## 📊 Model Details

- **Algorithm**: XGBoost Regressor
- **Training Data**: Historical HDB Resale Flat Prices
- **Data Last Updated**: 30-06-2025
- **Features**: 15+ property and location features

## 🎯 Usage

1. Select your desired HDB parameters using the sidebar controls
2. Click the "Predict Resale Price" button
3. View the predicted price and explore similar transactions on the map
4. Toggle between light and dark themes as preferred

## 🐳 Docker Deployment

### Build and Run
```bash
docker build -t hdb-predictor-app .
docker run -p 8501:8501 hdb-predictor-app
```

### Docker Compose
```yaml
version: '3.8'
services:
  hdb-app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## 🌐 API Access

The application provides a REST API endpoint for programmatic access:

```python
import requests

data = {
    "town": "ANG MO KIO",
    "flat_type": "4 ROOM",
    "storey_range": "10 TO 12",
    "floor_area_sqm": 105,
    "flat_model": "Model A",
    "lease_commence_date": 1985
}

response = requests.post("http://localhost:8501/api/predict", json=data)
prediction = response.json()
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Housing & Development Board (HDB) for public data
- Streamlit team for the amazing framework
- XGBoost developers for the machine learning library

## 📞 Support

If you have any questions or run into issues, please:

1. Check the [existing issues](https://github.com/yourusername/hdb-price-predictor-app/issues)
2. Create a new issue with detailed information

## 📊 Related Projects

- [HDB Data Analysis Notebook](https://github.com/yourusername/hdb-data-analysis)
- [Singapore Property API](https://github.com/yourusername/sg-property-api)

---

<div align="center">

Made with ❤️ in Singapore

</div>