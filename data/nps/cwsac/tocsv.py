""" Convert cwsac.json to csv files """
import json
import csv

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

battle_fields = (#'cwsac_reference',
    'battle',
    'battle_name',
    'other_names',
    'operation',
    'assoc_battles',
    'location',
    'campaign',
    'start_date',
    'end_date',
    'forces_text',
    'strength',
    'casualties_text',
    'casualties',
    'description',
    'state',
    'results_text',
    'result',
    'preservation',
    'significance',
    'url'
)

# keys = set()
# for battle, battle_data in data.items():
#     for k in battle_data:
#         keys.add(k)
# print(keys)

def battle_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, battle_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            row = dict_subset(battle_data, battle_fields)
            row['operation'] = int(row['operation'])
            writer.writerow(row)

belligerent_fields = [
 'battle',
 'belligerent',

 'description',
 'strength_min',
 'strength_max',
 'armies',
 'corps',
 'divisions',
 'brigades',
 'regiments',
 'companies',

 'cavalry_regiments',
 'cavalry_brigades',
 'cavalry_corps',
 'cavalry_divisions',

 'artillery_batteries',
 'ships',
 'ironclads',
 'gunboats',
 'wooden_ships',
 'rams',

 'casualties',
 'killed',
 'wounded',
 'missing',
 'captured',

]

def forces_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, belligerent_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for belligerent, x in sorted(battle_data['belligerents'].items()):
                row = dict_subset(x, belligerent_fields)
                row['battle'] = battle
                row['belligerent'] = belligerent
                writer.writerow(row)

commanders_fields = (
    'battle', 
    'belligerent',
    'fullname',
    'rank',
    'first_name',
    'last_name',
    'middle_name',
    'suffix'
)

def commanders_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, commanders_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            for belligerent, x in sorted(battle_data['belligerents'].items()):
                for commander in x['commanders']:
                    row = commander.copy()
                    row['battle'] = battle
                    row['belligerent'] = belligerent
                    writer.writerow(row)

SRC = "cwsac.json"
with open(SRC, 'r') as f:
    data = json.load(f)

battle_csv(data, 'cwsac_battles.csv')
forces_csv(data, 'cwsac_forces.csv')
commanders_csv(data, 'cwsac_commanders.csv')
