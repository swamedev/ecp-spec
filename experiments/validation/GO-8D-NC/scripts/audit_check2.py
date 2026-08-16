import pandas as pd
import numpy as np
from scipy.stats import friedmanchisquare, wilcoxon

df = pd.read_csv(r'D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\pilot_results_newcycle.csv')
A = df[df['condition']=='A']['dv3'].values
B = df[df['condition']=='B']['dv3'].values
C = df[df['condition']=='C']['dv3'].values

print('A shape:', A.shape)
print('B shape:', B.shape)
print('C shape:', C.shape)

# Friedman
chi2, p = friedmanchisquare(A, B, C)
print(f'Friedman: chi2={chi2:.4f}, p={p:.2e}')

# Manual Friedman check
N = len(A)
k = 3
data = np.column_stack([A, B, C])
ranks = np.argsort(np.argsort(data, axis=1), axis=1) + 1
R = ranks.sum(axis=0)
print('Rank sums:', R)
chi2_manual = (12 / (N * 3 * 4)) * np.sum(R**2) - 3 * N * 4
print(f'Manual Friedman chi2: {chi2_manual:.4f}')

# scipy friedman
from scipy.stats import friedmanchisquare
chi2, p = friedmanchisquare(A, B, C)
print(f'Scipy friedman: chi2={chi2:.4f}, p={p:.2e}')

# Wilcoxon tests
for c1, c2, label in [('B','A','B<A'), ('C','A','C<A'), ('C','B','C<B')]:
    x = df[df['condition']==c1]['dv3'].values
    y = df[df['condition']==c2]['dv3'].values
    stat, p = wilcoxon(x, y, alternative='less')
    print(f'Wilcoxon {label}: stat={stat}, p={p:.2e}')

# TOST A-C
from scipy.stats import ttest_1samp
diff = df[df['condition']=='A']['dv3'].values - df[df['condition']=='C']['dv3'].values
delta = 0.05
t_stat, p = ttest_1samp(diff, popmean=delta)
print(f'TOST A-C (delta=0.05): mean_diff={np.mean(diff):.4f}, t={t_stat:.4f}, p={p:.4f}')

# Effect sizes
def cliffs_delta(x, y):
    n1, n2 = len(x), len(y)
    diff = np.subtract.outer(x, y)
    return (np.sum(diff > 0) - np.sum(diff < 0)) / (n1 * n2)

for c1, c2 in [('A','B'), ('A','C'), ('B','C')]:
    cd = cliffs_delta(df[df['condition']==c1]['dv3'].values, df[df['condition']==c2]['dv3'].values)
    print(f'Cliff delta {c1} vs {c2}: {cd:.3f}')

print('\n=== ORIGINAL STATS COMPARISON ===')
print('Original Friedman: chi2=38.4667, p=4.44e-09')
print('Original Wilcoxon B<A: p=2.61e-8')
print('Original Wilcoxon A<C: p=2.61e-8')
print('Original Wilcoxon B<C: p=0.0310')
print('Original TOST A-C: mean_diff=-0.0758, not equivalent')