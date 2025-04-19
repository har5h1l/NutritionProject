# School Nutrition Habits Analysis

## Project Overview
This project analyzes nutrition and eating habits of the general population based on survey responses. The analysis examines various aspects of individuals' diets, including water consumption, fruit and vegetable intake, junk food consumption, and self-perceived healthiness compared to objective measures.

## Project Structure
```
data_analysis/
├── data/                      # Raw data files
│   └── Nutrition and Eating Habits Survey Responses.csv
│
├── scripts/                   # Analysis scripts
│   ├── nutrition_analysis.py              # Basic analysis script
│   └── nutrition_analysis_extended.py     # Comprehensive analysis script
│
├── visualizations/            # Generated charts and graphs
│   ├── age_distribution.png
│   ├── water_consumption.png
│   ├── fruit_veg_consumption.png
│   └── ... (other visualization files)
│
├── reports/                   # Summary reports
│   └── nutrition_summary_report.txt
│
└── README.md                  # This file
```

## Data Description
The analysis is based on survey responses from 81 individuals containing information about:
- Basic demographics (age, gender)
- Diet types (vegetarian, non-vegetarian, etc.)
- Consumption frequencies for different food categories
- Water intake
- Physical activity levels
- Self-rated diet healthiness

## Analysis Scripts

### Basic Analysis (`nutrition_analysis.py`)
This script performs:
- Basic data loading and cleaning
- Generation of key visualizations
- Summary statistics calculation

Usage:
```bash
cd data_analysis
python scripts/nutrition_analysis.py
```

### Comprehensive Analysis (`nutrition_analysis_extended.py`)
This script provides a more in-depth analysis with:
- Extensive data cleaning and transformation
- Creation of a health score based on multiple factors
- 12 different visualizations covering various aspects
- Detailed correlations between different factors
- Generation of a comprehensive summary report

Usage:
```bash
cd data_analysis
python scripts/nutrition_analysis_extended.py
```

Note: You may need to update the file paths in the scripts if running from different directories.

## Key Findings
From the analysis, we discovered:

1. Water Consumption
   - 69.1% of individuals drink less than recommended 2 liters of water daily
   - Strong correlation (0.52) between water consumption and overall diet health

2. Fruit and Vegetable Consumption
   - 91.4% of individuals eat fruits/vegetables almost daily (25+ days/month)
   - Moderate correlation with physical activity levels

3. Junk Food Consumption
   - 74.1% of individuals consume junk food frequently (15+ days per month)
   - Gender-based differences exist in junk food consumption patterns

4. Self-Perception vs. Reality
   - Only a moderate correlation (0.24) between how individuals rate their diet health and objective measures
   - Some individuals overestimate their dietary healthiness

## Recommendations
Based on the analysis:

1. Water Consumption
   - Implement campaigns to increase water consumption among individuals
   - Provide better access to water fountains/bottle filling stations

2. Junk Food Reduction
   - Educational initiatives about the impact of excessive junk food consumption
   - Consider policies to limit availability of these items in various settings

3. Nutrition Education
   - Develop targeted nutrition education programs
   - Address the discrepancy between perceived and actual dietary healthiness

4. Physical Activity Promotion
   - Encourage more physical activity, which correlates with healthier eating habits

## Dependencies
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scipy

## Future Work
- Longitudinal analysis tracking changes over time
- More detailed dietary assessment
- Include academic performance correlation analysis
- Expand sample size and demographic diversity