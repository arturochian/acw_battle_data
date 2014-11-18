""" Convert cwsac.json to csv files """
import json
import csv

def dict_remove(x, exclude = []):
    return dict((k, v) for k, v in x.items() if k not in exclude)

def dict_subset(x, include = []):
    return dict((k, v) for k, v in x.items() if k in include)

battle_fields = (#'combatants',
     'battle',
     'battle_name',
     'campaign',
     'url',
     'state',
     # 'locations',
     'strength',
     #'dates',
     'results_text',
     'results',
     'forces_text',
     'study_area',
     'core_area',
     'potnr_boundary')

def battle_csv(data, filename):
    # keys = set()
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, battle_fields)
        writer.writeheader()
        for battle, battle_data in sorted(data.items()):
            # for k in battle_data:
            #     keys.add(k)
            row = dict_subset(battle_data, battle_fields)
            writer.writerow(row)

combatant_fields = ('battle',
 'combatant',
 'description',
<<<<<<< HEAD
 'strength',
 'ships',
 'guns',
 'commanders',
 'cavalry_regiments',
 'strength_other',
 'brigades',
 'regiments',
 'cavalry_brigades',
 'companies',
 'corps',
 'divisions',
 'armies',
 'artillery_batteries',
 'cavalry_divisions',
 'cavalry_corps',
 'artillery_regiments',
 'artillery_sections',
 'cavalry_companies',
 'artillery_companies',
 'infantry_regiments'
=======
 'commanders',
 'strength',
 'regiments',
 'companies',
 'brigades',
 'divisions',
 'corps',
 'armies',
 'cavalry_regiments',
 'cavalry_brigades',
 'cavalry_divisions',
 'cavalry_corps',
 'cavalry_companies',
 'artillery_batteries',
 'artillery_companies',
 'artillery_regiments',
 'artillery_sections',
 'infantry_regiments'
 'strength_other',
 'ships',
 'guns',
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025
)

def combatants_csv(data, filename):
    # fields = set()
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, combatant_fields)
        writer.writeheader()
<<<<<<< HEAD
        for battle, battle_data in data.items():
            for combatant, x in battle_data['combatants'].items():
                # for k in x:
                #     fields.add(k)
                row = dict_subset(battle_data, combatant_fields)
=======
        for battle, battle_data in sorted(data.items()):
            for combatant, force_data in sorted(battle_data['combatants'].items()):
                row = dict_subset(force_data, combatant_fields)
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025
                row['battle'] = battle
                row['combatant'] = combatant
                writer.writerow(row)
    # print(fields)

<<<<<<< HEAD
commanders_fields = ('battle', 'combatant', 'fullname', 'rank')
=======
commanders_fields = ('battle', 'combatant', 'fullname', 'rank',
                     'last_name', 'first_name', 'middle_name', 'suffix')
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025

def commanders_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, commanders_fields)
        writer.writeheader()
<<<<<<< HEAD
        for battle, battle_data in data.items():
            for combatant, x in battle_data['combatants'].items():
=======
        for battle, battle_data in sorted(data.items()):
            for combatant, x in sorted(battle_data['combatants'].items()):
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025
                for commander in x['commanders']:
                    row = commander.copy()
                    row['battle'] = battle
                    row['combatant'] = combatant
                    writer.writerow(row)

def dates_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, ('battle', 'spell', 'start_date', 'end_date'))
        writer.writeheader()
<<<<<<< HEAD
        for battle, battle_data in data.items():
=======
        for battle, battle_data in sorted(data.items()):
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025
            for spell in battle_data['dates']:
                row = spell.copy()
                row['battle'] = battle
                writer.writerow(row)

def locations_csv(data, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, ('battle', 'state', 'location'))
        writer.writeheader()
<<<<<<< HEAD
        for battle, battle_data in data.items():
=======
        for battle, battle_data in sorted(data.items()):
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025
            for spell in battle_data['locations']:
                row = spell.copy()
                row['battle'] = battle
                writer.writerow(row)

SRC = "cwsac2.json"
with open(SRC, 'r') as f:
    data = json.load(f)

battle_csv(data, 'cwsac2_battles.csv')
<<<<<<< HEAD
combatants_csv(data, 'cwsac2_combatants.csv')
=======
combatants_csv(data, 'cwsac2_forces.csv')
>>>>>>> 379f5c05b3ae34481969a30e523e3c0b689bd025
commanders_csv(data, 'cwsac2_commanders.csv')
dates_csv(data, 'cwsac2_dates.csv')
locations_csv(data, 'cwsac2_locations.csv')
