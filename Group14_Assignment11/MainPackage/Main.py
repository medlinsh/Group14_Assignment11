'''
#Name: Seth Medlin, Bill Tummler
#email: medlinsh@mail.uc.edu, Tummlewm@mail.uc.edu
#Assignment: Assignment 11
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can retrieve data from a JSON source and output meaningful information
#Citations: "https://open.fda.gov/apis/query-syntax/" , "https://api.fda.gov/drug/event.json"
#Anything else thats relevant: N/A
'''
#importing the needed functions
import requests 
import json
import statistics


# Pulls data of patients who experienced Overdoses while taking Oxycontin from the FDA.gov API
response = requests.get('https://api.fda.gov/drug/event.json?api_key=1waaLElvCplx3l7PVdX3DguXN1t8e2Dz4s6QhrgO&search=patient.reaction.reactionmeddrapt:OVERDOSE +AND+patient.drug.medicinalproduct:OXYCONTIN&limit=15') #API Key = 1waaLElvCplx3l7PVdX3DguXN1t8e2Dz4s6QhrgO
json_string = response.content #Saves Response as a variable

#Creating a Python dictionary of the FDA Data pulled
parsed_json = json.loads(json_string) 
    
print(parsed_json)


#Testing Each Result
#print(parsed_json['results'][0]['patient']['patientonsetage'])
#print(parsed_json['results'][1]['patient']['patientonsetage'])
#print(parsed_json['results'][2]['patient']['patientonsetage'])
#print(parsed_json['results'][3]['patient']['patientonsetage'])
#print(parsed_json['results'][4]['patient']['patientonsetage'])
#print(parsed_json['results'][5]['patient']['patientonsetage'])
#print(parsed_json['results'][6]['patient']['patientonsetage'])
#print(parsed_json['results'][7]['patient']['patientonsetage'])
#print(parsed_json['results'][8]['patient']['patientonsetage'])
#print(parsed_json['results'][9]['patient']['patientonsetage'])


#Creating a list of all of the Ages - This is a little cluncky
list_Age = [ 
    int(parsed_json['results'][0]['patient']['patientonsetage']),
    int(parsed_json['results'][2]['patient']['patientonsetage']),
    int(parsed_json['results'][3]['patient']['patientonsetage']),
    int(parsed_json['results'][4]['patient']['patientonsetage']),
    int(parsed_json['results'][5]['patient']['patientonsetage']),
    int(parsed_json['results'][6]['patient']['patientonsetage']),
    int(parsed_json['results'][7]['patient']['patientonsetage']),
    int(parsed_json['results'][8]['patient']['patientonsetage']),
    int(parsed_json['results'][9]['patient']['patientonsetage'])
    ]

print('The ages of patients that died from Oxycotin Overdose are:', list_Age)

#Finding the Average age from the list
avg_Age = statistics.mean(list_Age)


print('The average age of the patients who dies from Oxycotin Overdose in the FDA data is: ', round(avg_Age), "years old")





    

