import json
import pandas as pd
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--json", type=str)
args = parser.parse_args()

try:
    json_data = json.load(open(args.json))
except:
    print(args.json)
    raise
dict_data = []
for k, v in json_data['nuc'].items():
    datum = dict()
    datum['id'] = k
    datum['x'] = v['centroid'][0]
    datum['y'] = v['centroid'][1]
    datum['type'] = v['type']
    dict_data.append(datum)
pd.DataFrame(dict_data).to_csv(args.json.replace('.json', '.csv'), index=False)
