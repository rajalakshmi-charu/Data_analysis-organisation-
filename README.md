# Data_analysis-organisation-
Data Preprocessing and Correlation Heatmap

This project performs data cleaning, preprocessing, and correlation analysis on a dataset of organizations using Python. The main goal is to visualize how different numerical features are related to each other through a heatmap.
Dataset

File: `organizations-100.csv`
Content: Information about 100 organizations, with multiple categorical and numerical features.
 Preprocessing Steps

1. Missing Value Handling  
   - For categorical columns: filled with the most frequent value (mode).
   - For numerical columns: filled with the median.

2. Column Dropping 
   - Drops unnecessary or irrelevant columns: `Name`, `Description`,`Internal ID`, `EAN` (if present).

3. Encoding  
   - Converts categorical variables into numeric using one-hot encoding.

4. Standardization
   - Scales numerical features to have zero mean and unit variance.
 Correlation Analysis
- Identifies top 10 features with the highest variance.
- Generates a **heatmap** to visualize the correlation between these features.
- Helps in feature selection and understanding relationships.

Output

The script produces a heatmap showing pairwise correlations:

- Strong positive/negative correlations are highlighted.
- Useful for data exploration and preprocessing in machine learning workflows.

 ▶️ How to Run

 
 1. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

2. Run the Script

Make sure `organizations-100.csv` is in the same folder, then run:

```bash
python your_script.py
```

Or use Jupyter Notebook for step-by-step execution.

 Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn

