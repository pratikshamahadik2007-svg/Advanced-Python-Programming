import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
    
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for row in csvReader:
            jsonArray.append(row)
            
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csvFilePath = r'input.csv'
jsonFilePath = r'output.json'

csv_to_json(csvFilePath, jsonFilePath)