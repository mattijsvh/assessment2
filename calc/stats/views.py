from django.shortcuts import render
from .forms import UploadFileForm
import os
import pandas as pd
import numpy as np
import plotly as py
import plotly.figure_factory as ff
from calc.settings import MEDIA_ROOT


def file_upload(request):
    '''
    Voordat file opgeslagen wordt, verwijder contents in MEDIA_ROOT.
    Sla daarna file op in directory.
    '''
    csv_data = []
    distplot = []
    outliers = []
    corr = []

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            remove_dir(MEDIA_ROOT)
            document = form.save(commit = False)
            document.save()
    else:
        form = UploadFileForm()

    if os.listdir(MEDIA_ROOT):
        csv_path = os.path.join(MEDIA_ROOT, os.listdir(MEDIA_ROOT)[0]) #Verkrijg eerste file in MEDIA_ROOT directory
        csv_data = read_csv(csv_path)
        csv_data = get_Int(csv_data)
        corr = get_corr(csv_data)
        corr = corr.to_html()
        outliers = get_outliers(csv_data)
        outliers = outliers.to_html()
        distplot = normal_dist(csv_data)
        csv_data = csv_data.to_html()
    else:
        csv_data = []
        distplot = []
        outliers = []
        corr = []

    return render(request, 'stats/file_upload.html', {
        'form': form,
        'csv_data': csv_data,
        'outliers': outliers,
        'corr': corr,
        'distplot': distplot
    })

def remove_dir(path):
    '''
    Verwijdert inhoud van path
    '''
    for root, dirs, files in os.walk(path): #Kijkt in directory
        for file in files:
            os.remove(os.path.join(root, file)) #Verwijder iedere file


def read_csv(csv_path):
    '''
    Leest ingevoerde csv-bestand
    '''
    csv_file = pd.read_csv(csv_path, nrows = 5000)
    return csv_file

def get_Int(csv_data):
    '''
    Gebruik alleen numerieke kolommen
    '''
    csv_data = csv_data.select_dtypes(include = [np.number])
    csv_data.dropna(inplace=True)
    return csv_data

def normal_dist(csv_data):
    '''
    Plot normaaldistributie
    '''

    y = py.offline.plot(ff.create_distplot([csv_data[c] for c in csv_data.columns], csv_data.columns, bin_size = 1),
                        auto_open = False,
                        output_type = 'div',
                        include_plotlyjs = False)


    return y

def get_outliers(csv_data):
    '''
    Zoek alleen waardes waar standaarddeviatie hoger dan 3 is.
    '''
    outliers = csv_data[np.abs(csv_data-csv_data.mean()) > (3*csv_data.std())]
    outliers.dropna(axis = 1, how = 'all', inplace = True)
    outliers.dropna(how = 'all', inplace = True)

    return outliers

def get_corr(csv_data):
    y = csv_data.corr().abs()

    return y

