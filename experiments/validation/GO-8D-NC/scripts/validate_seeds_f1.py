import hashlib, ast, sys

with open(r'D:\ecp-spec\experiments\validation\GO-8D-NC\scripts\seeds_nc.py', 'rb') as f:
    content = f.read()

artifact_hash = hashlib.sha256(content).hexdigest()
print('Seeds artifact SHA-256:', artifact_hash)

tree = ast.parse(content.decode('utf-8'))
seeds_dict = None
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == 'seeds':
                seeds_dict = ast.literal_eval(node.value)
                break

if seeds_dict is None:
    print('ERROR: Could not parse seeds dict')
    sys.exit(1)

bip_count = len(seeds_dict)
expected_bips = [f'BIP-{i:03d}' for i in range(1, 31)]
missing_bips = set(expected_bips) - set(seeds_dict.keys())
extra_bips = set(seeds_dict.keys()) - set(expected_bips)

total_seeds = 0
all_seeds = []
for bip, conditions in seeds_dict.items():
    if set(conditions.keys()) != {'A', 'B', 'C'}:
        print('ERROR:', bip, 'wrong conditions:', set(conditions.keys()))
    for cond in ['A', 'B', 'C']:
        seeds = conditions[cond]
        if set(seeds.keys()) != {'seed1', 'seed2', 'seed3'}:
            print('ERROR:', bip, '/', cond, 'wrong seed keys:', set(seeds.keys()))
        for s_name, s_val in seeds.items():
            if not isinstance(s_val, int):
                print('ERROR:', bip, '/', cond, '/', s_name, 'not int')
            if s_val < 0 or s_val >= 2**64:
                print('ERROR:', bip, '/', cond, '/', s_name, 'out of uint64 range:', s_val)
            total_seeds += 1
            all_seeds.append(s_val)

print('BIP count:', bip_count)
print('Total seeds:', total_seeds)
print('Unique seeds:', len(set(all_seeds)))
if len(set(all_seeds)) == total_seeds:
    print('All seeds UNIQUE')
else:
    print('DUPLICATES FOUND')

if 'SEED_MASTER = 20260816' in content.decode('utf-8'):
    print('SEED_MASTER = 20260816 confirmed')
else:
    print('SEED_MASTER missing')

if bip_count == 30 and total_seeds == 270 and len(set(all_seeds)) == 270 and not missing_bips and not extra_bips:
    print()
    print('F1 VALIDATION: PASS')
else:
    print()
    print('F1 VALIDATION: FAIL')