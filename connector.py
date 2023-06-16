import glob
import pandas as pd
import os
import requests
import json

# getting the pokemon name
response_API = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10&offset=0')
data = response_API.text
parse_json = json.loads(data)
pokemon_ls=[]
for i in range(0,10):
    pokemon_ls.append(parse_json['results'][i]['name'])

# configuring yml file
for pokemon in pokemon_ls:
    cmd = 'meltano config tap-pokeapi set airbyte_config.pokemon_name '+ pokemon
    os.system(cmd)
    cmd = 'meltano config target-csv set file_naming_scheme {stream_name}_'+pokemon+'.csv'
    os.system(cmd)
    cmd = 'meltano run tap-pokeapi target-csv'
    os.system(cmd)
    print("requested pokemon is: "+pokemon)

# merging the csv files
files=[]
df = pd.DataFrame()
for csv in glob.glob("pokemon_*.csv"):
    files.append(csv)
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df,data],axis=0)
df.to_csv('pokemon.csv', index = False)
os.system('ls')
