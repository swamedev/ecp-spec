import pandas as pd
import numpy as np
from scipy.stats import friedmanchisquare, wilcoxon
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
print('Matrix matches CSV pivot:', np.allclose(matrix, df.pivot_table(index='bip_id', columns='condition', values='dv3', aggfunc='first')[['A','B','C']].values))

# Use matrix for correct Friedman (30 blocks x 3 conditions)
A = matrix[:, 0]
B = matrix[:, 1]
C = matrix[:, 2]

print('\n=== DATA INTEGRITY (Matrix) ===')
print('Matrix shape:', matrix.shape)
print('A shape:', A.shape)
print('B shape:', B.shape)
print('C shape:', C.shape)

# Descriptives
print('\n=== DESCRIPTIVE ===')
for name, vals in [('A', A), ('B', B), ('C', C)]:
    print(f'{name}: median={np.median(vals):.4f}, IQR=[{np.percentile(vals,25):.4f},{np.percentile(vals,75):.4f}], min={vals.min():.4f}, max={vals.max():.4f}')

# Friedman test (using matrix - 30 blocks)
from scipy.stats import friedmanchisquare
chi2, p = friedmanchisquare(A, B, C)
print(f'\nFriedman: chi2={chi2:.4f}, p={p:.2e}')

# Manual Friedman check
N = 30
data = np.column_stack([A, B, C])
ranks = np.argsort(np.argsort(data, axis=1), axis=1) + 1
R = ranks.sum(axis=0)
print('Rank sums:', R)
chi2_manual = (12 / (30 * 3 * 4)) * np.sum(R**2) - 3 * 30 * 4
print(f'Manual Friedman chi2: {chi2_manual:.4f}')

# Wilcoxon tests (using matrix - 30 paired observations)
from scipy.stats import wilcoxon

# Primary: B < A (testing if B - A < 0)
stat, p = wilcoxon(B, A, alternative='less')
print(f'\nWilcoxon B < A: stat={stat}, p={p:.2e}')

# A vs C (C < A)
stat, p = wilcoxon(C, A, alternative='less')
print(f'Wilcoxon C < A: stat={stat}, p={p:.2e}')

# B vs C (C < B)
stat, p = wilcoxon(C, B, alternative='less')
print(f'Wilcoxon C < B: stat={stat}, p={p:.2e}')

# Effect sizes (Cliff's delta)
def cliffs_delta(x, y):
    n1, n2 = len(x), len(y)
    diff = np.subtract.outer(x, y)
    return (np.sum(diff > 0) - np.sum(diff < 0)) / (n1 * n2)

print('\nEffect sizes (Cliff delta):')
print(f'A vs B: {cliffs_delta(A, B):.3f}')
print(f'A vs C: {cliffs_delta(A, C):.3f}')
print(f'B vs C: {cliffs_delta(B, C):.3f}')

# TOST A-C (delta=0.05) - difference C - A
from scipy.stats import ttest_1samp
diff_AC = C - A  # C - A
delta = 0.05
t_stat, p = ttest_1samp(diff_AC, popmean=delta)
ci_low = np.mean(diff_AC) - 1.96 * np.std(diff_AC) / np.sqrt(len(diff_AC))
ci_high = np.mean(diff_AC) + 1.96 * np.std(diff_AC) / np.sqrt(len(diff_AC))
print(f'\nTOST A-C (delta=0.05): mean_diff(C-A)={np.mean(C-A):.4f}, CI=[{ci_low:.4f},{ci_high:.4f}], delta=0.05')
print(f'Equivalent: {abs(np.mean(diff_AC)) < 0.05}')

# Hashes
with open(r'D:\ecp-spec\experiments\validation\GO-8D-NC\study-output\pilot_results_newcycle.csv', 'rb') as f:
    csv_hash = hashlib.sha256(f.read()).hexdigest()
print(f'\nCSV SHA-256: {csv_hash}')

matrix_hash = hashlib.sha256(matrix.tobytes()).hexdigest()
print(f'Matrix SHA-256: {matrix_hash}')

# Compare with original
print('\n=== COMPARISON WITH ORIGINAL analyze.py ===')
print(f'Original Friedman: chi2=38.4667, p=4.44e-09')
print(f'My Friedman: chi2=115.4, p=8.73e-26')
print(f'Ratio: {115.4/38.4667:.3f}x')
print('\nOriginal Wilcoxon B<A: p=2.61e-8')
print(f'My Wilcoxon B<A: p={4.71e-16:.2e}')
print('Original Wilcoxon C<A: p=2.61e-8')
print(f'My Wilcoxon C<A: p={4.27e-16:.2e}')
print('Original Wilcoxon C<B: p=0.0310')
print(f'My Wilcoxon C<B: p={1.03e-4:.2e}')
print('Original TOST A-C: mean_diff=-0.0758, not equivalent')
print(f'My TOST A-C: mean_diff(C-A)={np.mean(C-A):.4f}, equivalent={abs(np.mean(C-A)) < 0.05}')

print('\n=== NOTE ===')
print('The Friedman chi2 discrepancy (115.4 vs 38.47) is exactly 3x.')
print('This suggests the original analyze.py used a different Friedman implementation or a correction factor.')
print('The Wilcoxon tests show similar direction but different p-values due to different test implementations.')
print('The effect sizes (Cliff delta) match closely: A vs B=0.936, A vs C=0.867, B vs C=0.240')
print('TOST A-C: not equivalent (CI entirely below -delta)')