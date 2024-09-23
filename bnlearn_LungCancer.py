#############################################################################
# bnlearn_PlayTennis.py
#
# Implements the Naive Bayes classifier for simple probabilistic inference.
# It makes use of the bnlearn library for parameter estimation and inference.
# This implementation data-dependend and works for only one dataset.
#
# Version: 1.0, Date: 10 September 2024
# Contact: hcuayahuitl@lincoln.ac.uk
#############################################################################

import bnlearn as bn
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

VISUALISE_STRUCTURE = True

# data loading using pandas
data = pd.read_csv('data/lung_cancer-train.csv')
print("DATA:\n", data)

# definition of directed acyclic graph (predefined structure)
# From csv:
# Smoking,Yellow_Fingers,Anxiety,Peer_Pressure,Genetics,Attention_Disorder,Born_an_Even_Day,Car_Accident,Fatigue,Allergy,Coughing
edges=[
    ('Lung_cancer', 'Smoking'),
    ('Lung_cancer', 'Yellow_Fingers'),
    ('Lung_cancer', 'Anxiety'),
    ('Lung_cancer', 'Peer_Pressure'),
    ('Lung_cancer', 'Genetics'),
    ('Lung_cancer', 'Attention_Disorder'),
    ('Lung_cancer', 'Born_an_Even_Day'),
    ('Lung_cancer', 'Car_Accident'),
    ('Lung_cancer', 'Fatigue'),
    ('Lung_cancer', 'Allergy'),
    ('Lung_cancer', 'Coughing'),
]
DAG = bn.make_DAG(edges)
print("DAG:\n", DAG)

# visualise the structure above
if VISUALISE_STRUCTURE:
    G = nx.DiGraph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold', arrows=True)
    plt.title('Directed Acyclic Graph (DAG)')
    plt.show()

# parameter learning using Maximum Likelihood Estimation
model = bn.parameter_learning.fit(DAG, data, methodtype="maximumlikelihood")
print("model=",model)

# probabilistic inference for the example covered in one of the last lecture slides of week 1
_evidence = {'O':'sunny', 'T':'cool', 'H':'high', 'W':'strong'}
inference_result = bn.inference.fit(model, variables=['PT'], evidence=_evidence)
print(inference_result)
