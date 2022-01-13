from django.shortcuts import render

# Create your views here.
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(BASE_DIR + '/dashboard/'+'drugsComTrain_raw.csv')
test = pd.read_csv(BASE_DIR + '/dashboard/'+'drugsComTest_raw.csv')
data = pd.concat([df, test])
rating = dict(data.loc[data.rating == 10, "drugName"].value_counts())
drugname = list(rating.keys())[:20]
drug_rating = list(rating.values())[:20]
def index(request):
    context={
        'drugname':drugname,
        'drug_rating':drug_rating,
        
    }
    return render(request, 'dashboard/index.html',context)