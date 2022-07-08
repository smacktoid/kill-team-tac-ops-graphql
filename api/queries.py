from os import kill

from ariadne import convert_kwargs_to_snake_case

from .models import KillTeam


def listKillTeams_resolver(obj, info):
    try:
        kill_teams = [kill_team.to_dict() for kill_team in KillTeam.query.all()]
        print(kill_teams)
        edges = []
        for kill_team in kill_teams:
            edge = dict()
            edge['node'] = kill_team
            edges.append(edge)
        kill_team_connection = dict()
        kill_team_connection['total_count'] = len(edges)
        kill_team_connection['edges'] = edges
        payload = {
            "success": True,
            "kill_teams": kill_team_connection
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    print(payload)
    return payload


@convert_kwargs_to_snake_case
def getKillTeam_resolver(obj, info, id):
    try:
        kill_team = KillTeam.query.get(id)
        payload = {
            "success": True,
            "kill_team": kill_team.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ['Unable to find kill team with this ID']
        }
    return payload