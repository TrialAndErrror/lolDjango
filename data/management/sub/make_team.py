from data.models import Team, Ban, Objective


def make_team(team_dict, match):
    team = Team.objects.create(
        team_id=team_dict['teamId'],
        win=team_dict['win'],
        match=match
    )

    ban_data = team_dict['bans']
    for ban in ban_data:
        Ban.objects.create(
            champion_id=ban['championId'],
            pick_turn=ban['pickTurn'],
            team=team
        )

    objectives_data = team_dict['objectives']
    for key, value in objectives_data.items():
        Objective.objects.create(
            name=key,
            first=value['first'],
            kills=value['kills'],
            team=team
        )
