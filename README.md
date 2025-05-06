# Seoul PM2.5 Analysis Based on Day Types and Months

This project analyzes and visualizes PM2.5 fine dust levels in Seoul using 2023 data. It focuses on how air quality varies by holidays, weekends, and weekdays across each month.

## 📌 Project Objective

To understand:
- How PM2.5 levels change on holidays, weekends, and weekdays
- Seasonal patterns and the interaction between lifestyle routines and air pollution

## 📂 Data Sources

Collected from monthly Excel files containing:
- Region
- Measurement date
- PM2.5 levels

## ⚙️ Preprocessing

- Combined 12 monthly datasets
- Added columns: month, day of week, holiday/weekend/weekday flags
- Removed missing values and outliers (PM2.5 < 0 or > 500)

## 📊 Visualization

- Box plots comparing PM2.5 distributions per month for holidays, weekends, and weekdays
- Holiday effect analyzed including the day before, during, and after

## 📈 Results

- PM2.5 is generally lower on holidays and weekends
- Winter months (Jan–Mar) showed higher PM2.5 due to heating and air stagnation
- Summer months (Jun–Aug) showed lower levels due to active atmospheric circulation

## 📎 Files Included

- `bigdata_bisong2.ipynb`: Main Jupyter notebook (translated to English)
- `bigdata_bisong2.html`: HTML-exported notebook for easy viewing
- `bigdata_bisong2.py`: Python version of the notebook
- `2023_01.xlsx ~ 2023_12.xlsx`: Monthly PM2.5 datasets (not included here for privacy, use sample if needed)
- `PM25_visualization.png`: Resulting plot image (optional)

## 🧠 Author

- Bisong Kwak
