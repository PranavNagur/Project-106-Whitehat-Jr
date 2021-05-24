import csv
import numpy as np
import plotly.express as px

def plotfigure(datapath):
    with open(datapath) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Days Present',y='Marks In Percentage')
        fig.show()

def getdatasource(datapath):
    marksinpercentage=[]
    dayspresent=[]
    with open(datapath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marksinpercentage.append(float(row['Marks In Percentage']))
            dayspresent.append(float(row['Days Present']))
    return {'x':marksinpercentage,'y':dayspresent}

def findcorelation(datasource):
    corelation=np.corrcoef(datasource['x'],datasource['y'])
    print('Corelation between marks in percentage and days present',corelation[0,1])

def setup():
    datapath='Dataset106.csv'
    datasource=getdatasource(datapath)
    plotfigure(datapath)
setup()