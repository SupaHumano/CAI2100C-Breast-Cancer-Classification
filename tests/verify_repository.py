from pathlib import Path
import json, hashlib
import pandas as pd
import nbformat

root=Path(__file__).resolve().parents[1]
csv=root/'data'/'[Dataset]_BreastCancer.csv'
assert hashlib.sha256(csv.read_bytes()).hexdigest()=='ce1eb276766fa19f93eda0d63b3cdb3afbb07618ff1ab7f33f4135ef9075c664'
df=pd.read_csv(csv)
assert df.shape==(569,32)
assert int(df.isna().sum().sum())==28
assert int(df.isna().any(axis=1).sum())==26
assert len(df.dropna())==543
for name,code_count in [('academic/Project_1_Course_Submission.ipynb',20),('notebooks/Project_1_Research_Validation.ipynb',24)]:
    nb=nbformat.read(root/name,as_version=4)
    cells=[c for c in nb.cells if c.cell_type=='code']
    assert len(cells)==code_count
    assert all(c.execution_count is not None for c in cells)
    assert all(not any(o.output_type=='error' for o in c.get('outputs',[])) for c in cells)
metrics=json.loads((root/'assets'/'metrics.json').read_text())
assert len(metrics['classroom'])==3
assert [m['name'] for m in metrics['classroom']]==['KNN','SVM','Decision Tree']
for model in metrics['classroom']:
    cm=model['confusion_matrix']
    assert sum(map(sum,cm))==109
    assert model['false_negatives']==cm[1][0]
    assert model['false_positives']==cm[0][1]
    assert abs((cm[0][0]+cm[1][1])/109-model['holdout_accuracy'])<1e-12
assert [round(100*m['accuracy'],2) for m in metrics['nested']]==[95.4,97.93,95.86]
print('Repository integrity, notebooks, model matrices and validation metrics: PASS')
