import pandas as pd
import os
from datetime import time

import warnings
warnings.filterwarnings("ignore")

def get_unique_values(df_file, columns):
    
    unique_df = df_file[columns].drop_duplicates()



    return unique_df

def change_column_name(df, header_map):
    df = df.rename(columns=header_map)
    return df

def format_fields(df, datatype_map):
    default_int_value = 0
    default_float_value = 0
    for col in list(datatype_map.keys()):
        if datatype_map[col] == 'date2' :
            df[col] = pd.to_datetime(df[col], format='%m/%d/%Y')
            df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')
            df[col] = df[col].fillna("")
        elif datatype_map[col] == 'date1' :
            df[col] = pd.to_datetime(df[col], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')

            #df[col] = df[col].astype(str)
            #df[col] = df[col].fillna("", inplace=True)
        elif datatype_map[col] == 'time' :
            df[col] = pd.to_datetime(df[col]).dt.time
            df[col] = df[col].fillna("")
        elif datatype_map[col] == 'float' :
            df[col] = df[col].astype(datatype_map[col], errors='ignore').round(1)
            df[col] = df[col].fillna(default_float_value)
        elif datatype_map[col] == 'int':
            df[col] = pd.to_numeric(df[col], errors='ignore').fillna(default_int_value)
            df[col] = df[col].astype(int, errors='ignore')
        elif datatype_map[col] == 'interval':
            df[col] = df[col].astype(str)
            df[col] = df[col].fillna("")
        else:
            df[col] = df[col].astype(datatype_map[col])
            df[col] = df[col].fillna("")

    return df

def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

csv_attributes_dict1 = { 
                         "drivers": ['driverId', 'givenName', 'familyName', 'dateOfBirth', 'nationality'],
                         "constructors": ['constructorId', 'name', 'nationality.1'],
                         "results": ['season', 'round', 'driverId',  'results.grid', 'results.laps', 'results.status'],
                         "driver_standings": ['season', 'round', 'driverId', 'position', 'points', 'positionText'],
                         "driver_teams": ['season', 'driverId', 'constructorId']
                        }

csv_attributes_dict1_rename_map = { 
    "drivers": {'driverId' : 'driverId', 'givenName' : "givenName", 'familyName' : "familyName", 'dateOfBirth' : "dateOfBirth", 'nationality' : "nationality"},
    "constructors": {'constructorId' : 'constructorId', 'name' : 'constructorName', 'nationality.1' : 'nationality'},
    "results": {'season' : 'season', 'round' : 'round', 'driverId' : 'driverId', 'results.grid' : 'resultGrid', 'results.laps' : 'resultLap', 'results.status' : 'resultStatus'},
    "driver_standings": {'season' : 'season', 'round' : 'round', 'driverId' : 'driverId', 'position' : "position", 'points' : 'points', 'positionText' : 'positionText'},
    "driver_teams": {'season' : 'season', 'driverId' : 'driverId', 'constructorId' : 'constructorId'}
}

csv_attributes_dict1_datatype_map = { 
    "drivers": {'driverId' : 'str', "givenName" : 'str',"familyName" : 'str', "dateOfBirth" : 'date1', 'nationality' : "str"},
    "constructors": {'constructorId' : 'str', 'constructorName' : 'str', 'nationality': 'str'},
    "results": {'season' : 'int', 'round' : 'int', 'driverId' : 'str','resultGrid' : 'int','resultLap' : 'int', 'resultStatus': 'str'},
    "driver_standings": {'season' : 'int', 'round' : 'int', 'driverId' : 'str', 'position' : "int", 'points' : 'int', 'positionText' : 'str'},
    "driver_teams": {'season' : 'int', 'driverId' : 'str', 'constructorId' : 'str'}
}

csv_attributes_dict2 = { "pitstops": ['year', 'round', 'driverId', 'lap', 'stop', 'time', 'duration']
                        }

csv_attributes_dict2_rename_map = {
    "pitstops": {'year' : 'season', 'round' : 'round', 'driverId' : 'driverId', 'lap' : 'lap', 'stop' : 'stop', 'time' : 'time', 'duration' : 'duration'}
}

csv_attributes_dict2_datatype_map = {
    "pitstops": {'season' : 'int', 'round' : 'int', 'driverId' : 'str', 'lap' : 'int', 'stop' : 'int', 'time' : 'time', 'duration' : 'float'}
}

csv_attributes_dict3 =  { "raceinfo": ['season', 'round', 'raceName', 'date', 'raceTime', 'circuitID'],
                          "laptime": ['season', 'round', 'lap', 'driverID', 'position', 'time'],
                          "circuits": ['circuitID', 'circuitName', 'country'] 
                        }

csv_attributes_dict3_rename_map = {
    "raceinfo": {'season' : 'season', 'round' : "round", 'raceName' : 'raceName', 'date' : 'date', 'raceTime' : 'raceTime', 'circuitID' : 'circuitId'},
    "laptime": {'season' : 'season', 'round' : 'round', 'lap' : 'lap', 'driverID' : 'driverId', 'position' : 'position', 'time' : 'laptime'},
    "circuits" : {'circuitID' : 'circuitId', 'circuitName' : 'circuitName', 'country' : 'country'}  
}

csv_attributes_dict3_datatype_map = {
    "raceinfo": {'season' : 'int', 'round' : "int", 'raceName' : 'str', 'date' : 'date1', 'raceTime' : 'time', 'circuitId' : 'str'},
    "laptime": {'season' : 'int', 'round' : 'int', 'lap' : 'int', 'driverId' : 'str', 'position' : 'int', 'laptime' : 'interval'},
    "circuits" : {'circuitId' : 'str', 'circuitName' : 'str', 'country': 'str'}   
}

raw_data = os.path.join(os.path.dirname(os.path.realpath(__file__)) , 'raw_data')
allracecsv = os.path.join(raw_data , "All_F1_Races.xlsx")
pitstopcsv = os.path.join(raw_data , "pitstops_scraped.csv")
laptime = raw_data

result_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)) , 'final')

df_1 = pd.read_excel(allracecsv)
df_1['circuitId'] = df_1['circuitId'].replace('BAK', 'baku')
df_1 = df_1[df_1['season'] >= 1996]
for table in list(csv_attributes_dict1.keys()):
    columns = csv_attributes_dict1[table]
    unique_df = get_unique_values(df_1, columns)
    
    if table in ["results", "driver_standings"]:
        unique_df.drop_duplicates(subset=["season", "round", "driverId"], keep='first', inplace=True)
    elif table == "driver_teams":
        unique_df.drop_duplicates(subset=["season", "driverId"], keep='first', inplace=True)
    sql_relation_table = change_column_name(unique_df, csv_attributes_dict1_rename_map[table])
    formatted_table = format_fields(sql_relation_table, csv_attributes_dict1_datatype_map[table])
    
    output_file = os.path.join(result_folder, table+".csv") 

    save_to_csv(formatted_table, output_file)


df_2 = pd.read_csv(pitstopcsv)
for table in list(csv_attributes_dict2.keys()):
    columns = csv_attributes_dict2[table]
    unique_df = get_unique_values(df_2, columns)
    filtered_table1 = unique_df[unique_df['year'] >= 1996]
    filtered_table = unique_df[unique_df['year'] < 2020]
    sql_relation_table = change_column_name(filtered_table, csv_attributes_dict2_rename_map[table])
    formatted_table = format_fields(sql_relation_table, csv_attributes_dict2_datatype_map[table])
    output_file = os.path.join(result_folder, table+".csv") 

    save_to_csv(formatted_table, output_file)

laptime_path = os.path.join(laptime, 'laptimedata')
laptime_files = os.listdir(laptime_path)

laptime_dfs = []

for file in laptime_files:
    lfp = os.path.join(laptime_path, file)
    df = pd.read_csv(lfp)
    laptime_dfs.append(df)

df_3 = pd.concat(laptime_dfs, ignore_index=True)

for table in list(csv_attributes_dict3.keys()):
    columns = csv_attributes_dict3[table]
    unique_df = get_unique_values(df_3, columns)
    #if table == "laptime":
    sql_relation_table = change_column_name(unique_df, csv_attributes_dict3_rename_map[table])
    formatted_table = format_fields(sql_relation_table, csv_attributes_dict3_datatype_map[table])
    output_file = os.path.join(result_folder, table+".csv") 

    save_to_csv(formatted_table, output_file)

print("Done")
