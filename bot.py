# Clone repository
git clone https://github.com/Barindersingh-iit/nifty50-ml-trading-bot.git
cd nifty50-ml-trading-bot

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Step 1: Fetch historical data
python data/fetch_data.py

# Step 2: Preprocess data
python data/preprocessing.py

# Step 3: Engineer features (technical indicators)
python data/feature_engineering.py

# Step 4: Train all models
python models/train.py

# Step 5: Run backtesting
python backtest/backtester.py

# Step 6: Make predictions
python inference/predictor.py

# Step 7: Deploy real-time trading
python inference/realtime_trading.py
