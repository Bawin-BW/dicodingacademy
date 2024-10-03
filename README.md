# Geolocation Dashboard

## Overview
This project visualizes the geolocation distribution of sellers and customers in São Paulo using Streamlit.

## Requirements
To run this project, you need to install the following Python packages:

- Babel==2.11.0
- matplotlib==3.8.4
- numpy==1.26.4
- pandas==2.2.2
- seaborn==0.13.2
- streamlit==1.32.0

You can find the required packages listed in the `requirements.txt` file.

## Installation

### Clone the Repository
First, clone the repository:

git clone https://github.com/Bawin-BW/dicodingacademy.git
cd dicodingacademy

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

## Install Dependencies
# Install the required packages:

pip install -r requirements.txt

## Prepare Data
Ensure that you have the following CSV files in the ../data/ directory:

sellers_lat.csv
sellers_lng.csv
customers_lat.csv
customers_lng.csv
Adjust the file paths in dashboard.py if necessary.

## Running the Dashboard
# Run the Streamlit application:

streamlit run dashboard.py
