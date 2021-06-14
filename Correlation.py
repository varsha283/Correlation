import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    coffee_in_ml=[]
    sleep_in_hours=[]
    with open(data_path) as csv_files:
        df=csv.DictReader(csv_files)
        for row in df:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
        
    return {"x":coffee_in_ml,"y":sleep_in_hours}
def find_correlation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Coffee in ml and sleep in hours:\n--->",correlation)
def setup():
    data_path="coffee.csv"
    dataSource=getDataSource(data_path)
    find_correlation(dataSource)
    plotFig(data_path)
def plotFig(data_path):
    with open(data_path) as csv_files:
        df=csv.DictReader(csv_files)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()
setup()