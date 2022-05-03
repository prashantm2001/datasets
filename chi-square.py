import pandas as pd
import scipy.stats as stats

# create sample data according to survey
data = [['likes_reading', 'Male'] for i in range(250)] + \
        [['likes_reading', 'Female'] for i in range(200)] + \
        [['disikes_reading', 'Male'] for i in range(50)] + \
        [['disikes_reading', 'Female'] for i in range(1000)]

df = pd.DataFrame(data, columns = ['Reading Status', 'Gender']) 

# create contingency table
data_crosstab = pd.crosstab(df['Reading Status'],
                            df['Gender'],
                           margins=True, margins_name="Total")

# significance level
alpha = 0.001

# Calcualtion of Chisquare test statistics
chi_square = 0
rows = df['Reading Status'].unique()
columns = df['Gender'].unique()
for i in columns:
    for j in rows:
        O = data_crosstab[i][j]
        E = data_crosstab[i]['Total'] * data_crosstab['Total'][j] / data_crosstab['Total']['Total']
        chi_square += (O-E)**2/E

# The p-value approach
        
# The critical value approach
print("\n--------------------------------------------------------------------------------------")
print("Approach: The critical value approach to hypothesis testing in the decision rule")
critical_value = stats.chi2.ppf(1-alpha, (len(rows)-1)*(len(columns)-1))
conclusion = "Failed to reject the null hypothesis."
if chi_square > critical_value:
    conclusion = "Null Hypothesis is rejected."
        
print("chisquare-score is:", chi_square, " and p value is:", critical_value)
print(conclusion)