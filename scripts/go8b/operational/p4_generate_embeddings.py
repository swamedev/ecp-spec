import numpy as np
import yaml
from sentence_transformers import SentenceTransformer

OUT = r"D:\ecp-spec\scripts\go8b\operational\EMBEDDINGS.npy"
META = r"D:\ecp-spec\scripts\go8b\operational\EMBEDDINGS.yaml"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load C3 taxonomy labels
with open(r"D:\ecp-spec\scripts\go8b\operational\C3_TAXONOMY.yaml", encoding="utf-8") as f:
    c3 = yaml.safe_load(f)

# Load C2 mapping (labels are CAT-XX; neutral descriptive text comes from definitions)
with open(r"D:\ecp-spec\scripts\go8b\operational\C2_PERMUTATION.yaml", encoding="utf-8") as f:
    c2 = yaml.safe_load(f)

# ECP canonical labels
ecp_labels = ["Problem", "Goal", "Claim", "Knowledge", "Assumption", "Evidence", "Decision", "State", "Artifact"]

# Text for each label to embed
texts = {}
for lbl in ecp_labels:
    texts[("ECP", lbl)] = lbl

for node in c3["taxonomy"]["nodes"]:
    texts[("SYN", node["label"])] = node["definition"]

# C2: neutral descriptive text of each CAT-XX from the canonical category they map to
c2_o2c = c2["opaque_to_canonical"]
cat_labels = sorted(c2_o2c.keys())
for cat in cat_labels:
    canon_name = c2_o2c[cat]
    texts[("CAT", cat)] = canon_name  # neutral via mapping; analysis-phase only

keys = list(texts.keys())
sentences = [texts[k] for k in keys]
vecs = model.encode(sentences, normalize_embeddings=True, show_progress_bar=False)

data = {
    "keys": [[ns, lbl] for ns, lbl in keys],
    "vectors": np.asarray(vecs, dtype=np.float32),
    "model": "sentence-transformers/all-MiniLM-L6-v2",
    "normalized": True,
}
np.save(OUT, data, allow_pickle=True)

import json
meta = {
    "model": "sentence-transformers/all-MiniLM-L6-v2",
    "dim": int(vecs.shape[1]),
    "normalized_L2": True,
    "count": len(keys),
    "usage": "S_sem only (05 WL-KERNEL SS4.1). S_struct does NOT use embeddings.",
    "hash_status": "PENDING LOCK PROTOCOL",
    "namespaces": list({"ECP", "SYN", "CAT"}),
}
with open(META, "w", encoding="utf-8", newline="\n") as f:
    yaml.safe_dump(meta, f, sort_keys=False)

print("EMBEDDINGS.npy written:", len(keys), "vectors, dim", vecs.shape[1])
print("BIP-VAL note: generated from frozen model; hash pending")