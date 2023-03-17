from data.models import Match


def make_match(info_dict, data_version, match_id):
    return Match.objects.create(
        match_id=match_id,
        data_version=data_version,
        game_creation=info_dict["gameCreation"],
        game_duration=info_dict["gameDuration"],
        game_end_timestamp=info_dict["gameEndTimestamp"],
        game_id=info_dict["gameId"],
        game_mode=info_dict["gameMode"],
        game_name=info_dict["gameName"],
        game_start_timestamp=info_dict["gameStartTimestamp"],
        game_type=info_dict["gameType"],
        game_version=info_dict["gameVersion"],
        map_id=info_dict["mapId"],
        platform_id=info_dict["platformId"],
        queue_id=info_dict["queueId"],
        tournament_code=info_dict["tournamentCode"],
    )


