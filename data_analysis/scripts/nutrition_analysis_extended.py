# Comprehensive School Nutrition Analysis Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Create directories for output
os.makedirs('visualizations', exist_ok=True)
os.makedirs('reports', exist_ok=True)
output_dir = 'visualizations'
reports_dir = 'reports'

# Set plotting style
sns.set_theme()
plt.rcParams.update({'font.size': 12})

print("Starting comprehensive nutrition data analysis...")

# Load data
try:
    file_path = 'data/Nutrition and Eating Habits Survey Responses.csv'
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully. Shape: {df.shape}")
    
    # Create a copy for cleaning and transformations
    df_clean = df.copy()
    
    # Standardize diet types
    diet_mapping = {
        'Vegeterian': 'Vegetarian',
        'vegetarian with chicken seafood and occasional mutton': 'Semi-Vegetarian',
        'vegetarian with the exception of chicken': 'Semi-Vegetarian',
        'Vegeterian with chicken seafood and occasional mutton': 'Semi-Vegetarian',
        'Non-vegeterian': 'Non-Vegetarian',
        'im a regular meat eater!!!! im very big back and obese and i love food so i eat everything but like beef and dogs yk': 'Non-Vegetarian',
        'Everything, all meats': 'Non-Vegetarian',
        'No specific diet': 'No specific diet',
        'no specific diet': 'No specific diet',
        'none': 'No specific diet',
        'n/a': 'No specific diet'
    }
    
    df_clean['Diet Type'] = df_clean["Do you follow a specific diet, and if so which one?"].map(lambda x: diet_mapping.get(x, x))
    
    # Create age groups
    df_clean['Age Group'] = pd.cut(df_clean['How old are you?'], 
                                 bins=[0, 14, 16, 18, 100], 
                                 labels=['13-14', '15-16', '17-18', '19+'])
    
    # Convert physical activity levels to numerical scale
    activity_mapping = {
        'Inactive': 0,
        'A little bit': 1,
        'Decent': 2,
        'Good': 3,
        'Amazing': 4
    }
    
    df_clean['Activity Level Score'] = df_clean['Rate your level of physical activity.'].map(activity_mapping)
    
    # Convert water consumption to estimated liters
    water_mapping = {
        'Less than 1 Liter': 0.5,
        '1-2 Liters': 1.5,
        '2-3 Liters': 2.5,
        '3-4 Liters': 3.5,
        '4+ Liters': 4.5
    }
    
    df_clean['Water Consumption (Liters)'] = df_clean['How much water do you drink in a day? (One Liter is about 2 water bottles)'].map(water_mapping)
    
    # Create a healthiness score
    df_clean['Healthy Diet Score'] = 0
    
    # High fruit/vegetable consumption (25+ days/month)
    df_clean.loc[df_clean['In a month, how many days do you eat fruits and vegetables?'] >= 25, 'Healthy Diet Score'] += 1
    
    # Low junk food consumption (10 or fewer days/month)
    df_clean.loc[df_clean['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?'] <= 10, 'Healthy Diet Score'] += 1
    
    # Low sugary beverage consumption (5 or fewer days/month)
    df_clean.loc[df_clean['In a month, how many days do you consume sugary beverages (soda, energy drinks, sweetened coffee/tea)?'] <= 5, 'Healthy Diet Score'] += 1
    
    # Low fast food consumption (3 or fewer days/month)
    df_clean.loc[df_clean['In a month, how many days do you eat fast food?'] <= 3, 'Healthy Diet Score'] += 1
    
    # High water consumption (2+ liters/day)
    df_clean.loc[df_clean['Water Consumption (Liters)'] >= 2, 'Healthy Diet Score'] += 1
    
    print("\n--- GENERATING VISUALIZATIONS ---")
    
    # 1. Age distribution
    plt.figure(figsize=(10, 6))
    df_clean['How old are you?'].value_counts().sort_index().plot(kind='bar')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/1_age_distribution.png')
    print("✓ Age distribution plot")
    
    # 2. Gender distribution
    plt.figure(figsize=(10, 6))
    gender_counts = df_clean['What is your gender?'].value_counts()
    gender_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Gender Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/2_gender_distribution.png')
    print("✓ Gender distribution plot")
    
    # 3. Diet type distribution
    plt.figure(figsize=(12, 6))
    diet_counts = df_clean['Diet Type'].value_counts()
    diet_counts.plot(kind='bar')
    plt.title('Diet Type Distribution')
    plt.xlabel('Diet Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/3_diet_type_distribution.png')
    print("✓ Diet type distribution plot")
    
    # 4. Water consumption
    plt.figure(figsize=(10, 6))
    water_counts = df_clean['How much water do you drink in a day? (One Liter is about 2 water bottles)'].value_counts()
    water_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Water Consumption Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/4_water_consumption.png')
    print("✓ Water consumption plot")
    
    # 5. Fruit and vegetable consumption
    plt.figure(figsize=(10, 6))
    veg_fruit_dist = df_clean['In a month, how many days do you eat fruits and vegetables?'].value_counts().sort_index()
    plt.bar(veg_fruit_dist.index.astype(str), veg_fruit_dist.values)
    plt.title('Fruit and Vegetable Consumption (Days per Month)')
    plt.xlabel('Days per Month')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/5_fruit_veg_consumption.png')
    print("✓ Fruit and vegetable consumption plot")
    
    # 6. Junk food consumption
    plt.figure(figsize=(10, 6))
    junk_food_dist = df_clean['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?'].value_counts().sort_index()
    plt.bar(junk_food_dist.index.astype(str), junk_food_dist.values)
    plt.title('Junk Food Consumption (Days per Month)')
    plt.xlabel('Days per Month')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/6_junk_food_consumption.png')
    print("✓ Junk food consumption plot")
    
    # 7. Self-rated health
    plt.figure(figsize=(10, 6))
    health_counts = df_clean['Self-rate how healthy your diet is.'].value_counts()
    health_counts.plot(kind='bar')
    plt.title('Self-Rated Health Distribution')
    plt.xlabel('Self-Rating')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/7_self_rated_health.png')
    print("✓ Self-rated health plot")
    
    # 8. Healthy Diet Score distribution
    plt.figure(figsize=(10, 6))
    df_clean['Healthy Diet Score'].value_counts().sort_index().plot(kind='bar')
    plt.title('Healthy Diet Score Distribution')
    plt.xlabel('Score (0-5, higher is healthier)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/8_healthy_diet_score.png')
    print("✓ Healthy diet score plot")
    
    # 9. Comparison: Self-rated vs Objective health
    health_mapping = {
        'Extremely unhealthy': 0,
        'Unhealthy': 1,
        'Healthy': 2,
        'Extremely healthy': 3
    }
    
    df_clean['Health Self-Rating Score'] = df_clean['Self-rate how healthy your diet is.'].map(health_mapping)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df_clean['Health Self-Rating Score'], df_clean['Healthy Diet Score'])
    plt.title('Self-Rated vs Objective Health Score')
    plt.xlabel('Self-Rated Health (0-3)')
    plt.ylabel('Objective Health Score (0-5)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/9_self_vs_objective_health.png')
    print("✓ Self-rated vs objective health plot")
    
    # 10. Comparison by age group
    plt.figure(figsize=(12, 6))
    age_health = df_clean.groupby('Age Group')['Healthy Diet Score'].mean()
    age_health.plot(kind='bar')
    plt.title('Average Healthy Diet Score by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Health Score')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/10_health_by_age.png')
    print("✓ Health by age group plot")
    
    # 11. Comparison by gender
    plt.figure(figsize=(10, 6))
    gender_health = df_clean.groupby('What is your gender?')['Healthy Diet Score'].mean()
    gender_health.plot(kind='bar')
    plt.title('Average Healthy Diet Score by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Average Health Score')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/11_health_by_gender.png')
    print("✓ Health by gender plot")
    
    # 12. Correlation heatmap
    plt.figure(figsize=(14, 10))
    correlation_vars = [
        'How old are you?',
        'Activity Level Score',
        'In a month, how many days do you eat fruits and vegetables?',
        'In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?',
        'In a month, how many days do you consume sugary beverages (soda, energy drinks, sweetened coffee/tea)?',
        'In a month, how many days do you eat a dessert after a meal?',
        'In a month, how many days do you eat fast food?',
        'In a month, how many days do you eat out?',
        'Water Consumption (Liters)',
        'Health Self-Rating Score',
        'Healthy Diet Score'
    ]
    
    corr_matrix = df_clean[correlation_vars].corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', 
                square=True, linewidths=.5)
    plt.title('Correlation Matrix of Key Variables')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/12_correlation_heatmap.png')
    print("✓ Correlation heatmap")
    
    # Generate summary report
    with open(f'{reports_dir}/nutrition_summary_report.txt', 'w') as f:
        f.write("=== SCHOOL NUTRITION HABITS ANALYSIS SUMMARY ===\n\n")
        
        f.write("BASIC STATISTICS:\n")
        f.write(f"Total participants: {len(df_clean)}\n")
        f.write(f"Age range: {df_clean['How old are you?'].min()} - {df_clean['How old are you?'].max()} (Average: {df_clean['How old are you?'].mean():.1f})\n")
        f.write(f"Gender distribution: {df_clean['What is your gender?'].value_counts().to_dict()}\n\n")
        
        f.write("KEY FINDINGS:\n")
        f.write(f"1. Water consumption: {(df_clean['Water Consumption (Liters)'] < 2).mean()*100:.1f}% of students drink less than 2 liters of water daily\n")
        f.write(f"2. Fruit & vegetable consumption: {(df_clean['In a month, how many days do you eat fruits and vegetables?'] >= 25).mean()*100:.1f}% of students eat fruits/vegetables almost daily\n")
        f.write(f"3. Junk food: {(df_clean['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?'] >= 15).mean()*100:.1f}% of students consume junk food 15+ days per month\n")
        f.write(f"4. Fast food: {(df_clean['In a month, how many days do you eat fast food?'] >= 5).mean()*100:.1f}% of students eat fast food 5+ days per month\n")
        f.write(f"5. Sugary beverages: {(df_clean['In a month, how many days do you consume sugary beverages (soda, energy drinks, sweetened coffee/tea)?'] >= 10).mean()*100:.1f}% of students consume sugary beverages 10+ days per month\n\n")
        
        f.write("DIET TYPES:\n")
        for diet, count in df_clean['Diet Type'].value_counts().items():
            f.write(f"- {diet}: {count} students ({count/len(df_clean)*100:.1f}%)\n")
        f.write("\n")
        
        f.write("SELF-PERCEPTION VS REALITY:\n")
        f.write("Average objective health score (0-5) by self-rated category:\n")
        for category, score in df_clean.groupby('Self-rate how healthy your diet is.')['Healthy Diet Score'].mean().items():
            f.write(f"- {category}: {score:.2f}\n")
        f.write("\n")
        
        f.write("CORRELATIONS OF INTEREST:\n")
        f.write(f"- Activity level vs Fruit/veg consumption: {df_clean['Activity Level Score'].corr(df_clean['In a month, how many days do you eat fruits and vegetables?']):.2f}\n")
        f.write(f"- Activity level vs Junk food consumption: {df_clean['Activity Level Score'].corr(df_clean['In a month, how many days do you eat junk food (ultra-processed foods like chips, soda, cereal, candy, etc)?']):.2f}\n")
        f.write(f"- Water consumption vs Overall health score: {df_clean['Water Consumption (Liters)'].corr(df_clean['Healthy Diet Score']):.2f}\n")
        f.write(f"- Self-rated health vs Objective health score: {df_clean['Health Self-Rating Score'].corr(df_clean['Healthy Diet Score']):.2f}\n\n")
        
        f.write("RECOMMENDATIONS:\n")
        f.write("1. Water consumption: Implement campaigns to increase water consumption among students\n")
        f.write("2. Junk food reduction: Educational initiatives about the impact of excessive junk food consumption\n")
        f.write("3. Nutrition education: Develop programs to address the gap between perceived and actual dietary healthiness\n")
        f.write("4. Physical activity promotion: Encourage more physical activity, which correlates with healthier eating habits\n\n")
        
        f.write("This analysis was performed using the survey data collected from students. For more details, see the visualizations in the 'visualizations' folder.\n")
    
    print("\n✅ Analysis complete! Results saved to the organized directory structure.")
    print(f"📄 Summary report: {reports_dir}/nutrition_summary_report.txt")
    print(f"📊 Visualizations: 12 PNG files in the {output_dir} directory")
    
except Exception as e:
    print(f"Error during analysis: {e}") 