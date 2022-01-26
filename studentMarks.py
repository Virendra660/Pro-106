import csv
import numpy as np

def getDataSource(data_path):
    marks_in_percentage=[]
    days_persent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_persent.append(float(row["Days Present"]))
    
    return{"x":marks_in_percentage,"y":days_persent}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between marks in percentage and days present is:  ",correlation[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
setup()