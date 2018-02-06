import json
import csv
import pandas as pd
import pathlib
import glob, os


writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
os.chdir("./intents")
x= 0

for file in glob.glob("*.json"):

    if "usersays" not in file:

                    x+=1
                    print(x)

                    intent_name = os.path.splitext(file)[0]
                    print(intent_name)


                    #x += 1

                    with open(''+ intent_name + '_usersays_en-au.json') as json_data_query , open('' + intent_name + '.json') as json_data_response:
                            #print(intent_name)
                            queries = json.load(json_data_query)
                            response = json.load(json_data_response)
                            value_response = response["responses"][0]["messages"][0]["speech"]
                            value_query = []
                            dataframe_response = []

                            for i in range(0 , len(queries)-1 ):

                                value_query.append(queries[i]['data'][0]["text"])

                                dataframe_response.append(value_response)


                            for query in value_query:


                                df = pd.DataFrame({'query': value_query, "response" : dataframe_response})


                            df.to_excel(writer, sheet_name=intent_name.replace("smalltalk.", ""))

                            # Get the xlsxwriter objects from the dataframe writer object.
                            workbook  = writer.book
                            worksheet = writer.sheets[intent_name.replace("smalltalk.", "")]
