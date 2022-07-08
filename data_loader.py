import csv
from app import db
from api.models import KillTeam, Archetype

# print("creating db tables")
# db.create_all()

print(f'Create Archetypes')
archetypes = dict()
with open('data/archetypes.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        name = row["name"]
        print(f'\t{name}')
        archetype = Archetype(name=name)
        archetypes[name] = archetype
        db.session.add(archetype)
        line_count += 1


with open('data/kill_teams.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]}')
        archetype_column = row["archetypes"]
        archetype_names = archetype_column.split("||")
        kill_team_archetypes = []
        for arch in archetype_names:
            kill_team_archetypes.append(archetypes.get(arch))

        kill_team = KillTeam(name=row['name'], archetypes=kill_team_archetypes)
        db.session.add(kill_team)
        line_count += 1



    db.session.commit()