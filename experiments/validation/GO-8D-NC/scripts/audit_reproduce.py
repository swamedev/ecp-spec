import pandas as pd
import numpy as np
import json
from scipy import stats
import hashlib

# Load frozen data
df = pd.read_csv(r'D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\pilot_results_newcycle.csv')
matrix = np.load(r'D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\dv3_matrix_newcycle.npy')

print('=== DATA INTEGRITY ===')
print('CSV shape:', df.shape)
print('Matrix shape:', matrix.shape)
print('Unique BIPs:', df['bip_id'].nunique())
print('Conditions:', sorted(df['condition'].unique()))
print('Status counts:', df['status'].value_counts().to_dict())

# Verify matrix matches CSV
pivot = df.pivot_table(index='bip_id', columns='condition', values='dv3', aggfunc='first')
matrix_from_csv = pivot[['A', 'B', 'C']].values
print('Matrix matches CSV:', np.allclose(matrix, matrix_from_csv))

# Descriptives
print('\n=== DESCRIPTIVE ===')
for cond in ['A', 'B', 'C']:
    vals = df[df['condition'] == cond]['dv3'].values
    print(f'{cond}: median={np.median(vals):.4f}, IQR=[{np.percentile(vals,25):.4f},{np.percentile(vals,75):.4f}], min={vals.min():.4f}, max={vals.max():.4f}')

# Friedman test
from scipy.stats import friedmanchisquare, wilcoxon
stat, p = friedmanchisquare(
    df[df['condition']=='A']['dv3'].values,
    df[df['condition']=='B']['dv3'].values,
    df[df['condition']=='C']['dv3'].values
)
print(f'\nFriedman: chi2={stat:.4f}, p={p:.2e}')

# Wilcoxon tests
for c1, c2 in [('B','A'), ('A','C'), ('B','C')]:
    stat, p = wilcoxon(df[df['condition']==c1]['dv3'].values, df[df['condition']==c2]['dv3'].values, alternative='less')
    print(f'Wilcoxon {c1} < {c2}: stat={stat}, p={p:.2e}')

# Effect sizes
def cliffs_delta(x, y):
    n1, n2 = len(x), len(y)
    diff = np.subtract.outer(x, y)
    return (np.sum(diff > 0) - np.sum(diff < 0)) / (n1 * n2)

for c1, c2 in [('B','A'), ('A','C'), ('B','C')]:
    cd = cliffs_delta(df[df['condition']==c1]['dv3'].values, df[df['condition']==c2]['dv3'].values)
    print(f'Cliff delta {c1} vs {c2}: {cd:.3f}')

# TOST A-C
from scipy.stats import ttest_1samp
diff = df[df['condition']=='A']['dv3'].values - df[df['condition']=='C']['dv3'].values
delta = 0.05
t_stat, p = ttest_1samp(diff, popmean=delta)
print(f'\nTOST A-C (delta=0.05): mean_diff={np.mean(diff):.4f}, t={t_stat:.4f}, p={p:.4f}')

# Hash of CSV
with open(r'D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\pilot_results_newcycle.csv', 'rb') as f:
    csv_hash = hashlib.sha256(f.read()).hexdigest()
print(f'\nCSV SHA-256: {csv_hash}')

# Hash of matrix
matrix_hash = hashlib.sha256(matrix.tobytes()).hexdigest()
print(f'Matrix SHA-256: {matrix_hash}')

print('\n=== AUDIT COMPLETE ===')