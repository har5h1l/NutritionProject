# School Nutrition Analysis Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Create folders for outputs if they don't exist
os.makedirs('visualizations', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# Set plotting style - using a properly named style
sns.set_theme()

print("Loading and analyzing nutrition data...")

# Load data
try:
    file_path = 'data/Nutrition and Eating Habits Survey Responses.csv'
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully. Shape: {df.shape}")
    
    # Quick data summary
    print("\nBasic statistics for age:")
    print(df['How old are you?'].describe())
    
    # Age distribution
    plt.figure(figsize=(10, 6))
    df['How old are you?'].value_counts().sort_index().plot(kind='bar')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.savefig('visualizations/age_distribution.png')
    print("\nAge distribution plot saved as 'visualizations/age_distribution.png'")
    
    # Water consumption
    plt.figure(figsize=(10, 6))
    water_counts = df['How much water do you drink in a day? (One Liter is about 2 water bottles)'].value_counts()
    water_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Water Consumption Distribution')
    plt.ylabel('')
    plt.savefig('visualizations/water_consumption.png')
    print("Water consumption plot saved as 'visualizations/water_consumption.png'")
    
    # Fruit and vegetable consumption
    plt.figure(figsize=(10, 6))
    veg_fruit_dist = df['In a month, how many days do you eat fruits and vegetables?'].value_counts().sort_index()
    plt.bar(veg_fruit_dist.index.astype(str), veg_fruit_dist.values)
    plt.title('Fruit and Vegetable Consumption (Days per Month)')
    plt.xlabel('Days per Month')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/fruit_veg_consumption.png')
    print("Fruit and vegetable consumption plot saved as 'visualizations/fruit_veg_consumption.png'")
    
    # Self-rated health
    plt.figure(figsize=(10, 6))
    health_counts = df['Self-rate how healthy your diet is.'].value_counts()
    health_counts.plot(kind='bar')
    plt.title('Self-Rated Health Distribution')
    plt.xlabel('Self-Rating')
    plt.ylabel('Count')
    plt.savefig('visualizations/self_rated_health.png')
    print("Self-rated health plot saved as 'visualizations/self_rated_health.png'")
    
    # Gender comparison of junk food consumption
    plt.figure(figsize=(10, 6))
    gender_junk = df.groupby('What is your gender?')['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?'].mean()
    gender_junk.plot(kind='bar')
    plt.title('Average Junk Food Consumption by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Average Days per Month')
    plt.savefig('visualizations/gender_junk_food.png')
    print("Gender comparison plot saved as 'visualizations/gender_junk_food.png'")
    
    # Create a summary table
    print("\nSummary of Key Nutritional Habits:")
    summary = pd.DataFrame({
        'Metric': [
            'Average age', 
            'Students eating fruits/vegetables 25+ days per month (%)',
            'Students consuming junk food 15+ days per month (%)',
            'Students drinking less than 2L water per day (%)'
        ],
        'Value': [
            df['How old are you?'].mean(),
            (df['In a month, how many days do you eat fruits and vegetables?'] >= 25).mean() * 100,
            (df['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?'] >= 15).mean() * 100,
            (df['How much water do you drink in a day? (One Liter is about 2 water bottles)'].isin(['Less than 1 Liter', '1-2 Liters'])).mean() * 100
        ]
    })
    print(summary)
    
    # Save summary to reports directory
    with open('reports/basic_nutrition_summary.txt', 'w') as f:
        f.write("=== BASIC NUTRITION ANALYSIS SUMMARY ===\n\n")
        f.write(f"Total participants: {len(df)}\n")
        f.write(f"Average age: {df['How old are you?'].mean():.1f} years\n\n")
        f.write("KEY METRICS:\n")
        f.write(f"- Students eating fruits/vegetables 25+ days per month: {(df['In a month, how many days do you eat fruits and vegetables?'] >= 25).mean() * 100:.1f}%\n")
        f.write(f"- Students consuming junk food 15+ days per month: {(df['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?'] >= 15).mean() * 100:.1f}%\n")
        f.write(f"- Students drinking less than 2L water per day: {(df['How much water do you drink in a day? (One Liter is about 2 water bottles)'].isin(['Less than 1 Liter', '1-2 Liters'])).mean() * 100:.1f}%\n")
    
    print("\nAnalysis complete! Basic summary saved to 'reports/basic_nutrition_summary.txt'")
    print("Check the 'visualizations' directory for generated visualizations.")
    
except Exception as e:
    print(f"Error during analysis: {e}")
