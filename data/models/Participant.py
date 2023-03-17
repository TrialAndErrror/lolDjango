from django.db import models


class Participant(models.Model):
    team_id = models.IntegerField()
    participant_id = models.CharField(max_length=100)

    # Summoner Info
    summoner_name = models.CharField(max_length=100)
    summoner_id = models.CharField(max_length=100)
    summoner_level = models.IntegerField()
    profile_icon = models.IntegerField()
    eligible_for_progression = models.BooleanField()
    riot_id_name = models.CharField(max_length=100)
    riot_id_tagline = models.CharField(max_length=100)

    time_played = models.IntegerField()

    # Champion & Role Info
    champion_id = models.IntegerField()
    champion_name = models.CharField(max_length=100)
    champ_level = models.CharField(max_length=100)
    champ_experience = models.IntegerField()
    role = models.CharField(max_length=100)

    lane = models.CharField(max_length=100)
    team_position = models.CharField(max_length=100)
    individual_position = models.CharField(max_length=100)

    # K/D/A and Kill Stats
    assists = models.IntegerField()
    deaths = models.IntegerField()
    kills = models.IntegerField()

    double_kills = models.IntegerField()
    triple_kills = models.IntegerField()
    quadra_kills = models.IntegerField()
    penta_kills = models.IntegerField()
    unreal_kills = models.IntegerField()

    largest_multikill = models.IntegerField()
    killing_sprees = models.IntegerField()
    largest_killing_spree = models.IntegerField()

    longest_time_spent_living = models.IntegerField()
    total_time_spent_dead = models.IntegerField()

    # Farming & Economy
    gold_earned = models.IntegerField()
    gold_spent = models.IntegerField()

    neutral_minions_killed = models.IntegerField()
    total_minions_killed = models.IntegerField()
    bounty_level = models.IntegerField()

    consumables_purchased = models.IntegerField()

    # Vision
    vision_score = models.IntegerField()
    sight_wards_bought_in_game = models.IntegerField()
    vision_wards_bought_in_game = models.IntegerField()
    detector_wards_placed = models.IntegerField()
    wards_placed = models.IntegerField()
    wards_killed = models.IntegerField()

    # Damage and Healing
    total_heal = models.IntegerField()
    total_heals_on_teammates = models.IntegerField()
    total_units_healed = models.IntegerField()
    total_damage_shielded_on_teammates = models.IntegerField()

    total_damage_taken = models.IntegerField()
    damage_self_mitigated = models.IntegerField()
    magic_damage_taken = models.IntegerField()
    physical_damage_taken = models.IntegerField()
    true_damage_taken = models.IntegerField()

    magic_damage_dealt = models.IntegerField()
    magic_damage_dealt_to_champions = models.IntegerField()

    physical_damage_dealt = models.IntegerField()
    physical_damage_dealt_to_champions = models.IntegerField()

    true_damage_dealt = models.IntegerField()
    true_damage_dealt_to_champions = models.IntegerField()

    total_damage_dealt = models.IntegerField()
    total_damage_dealt_to_champions = models.IntegerField()

    total_time_cc_dealt = models.IntegerField()
    time_ccing_others = models.IntegerField()
    largest_critical_strike = models.IntegerField()

    # Objective Stats
    damage_dealt_to_objectives = models.IntegerField()
    damage_dealt_to_turrets = models.IntegerField()
    objectives_stolen = models.IntegerField()
    dragon_kills = models.IntegerField()

    nexus_kills = models.IntegerField()
    nexus_takedowns = models.IntegerField()
    nexus_lost = models.IntegerField()

    inhibitor_kills = models.IntegerField()
    inhibitor_takedowns = models.IntegerField()
    inhibitors_lost = models.IntegerField()

    turret_kills = models.IntegerField()
    turret_takedowns = models.IntegerField()
    turrets_lost = models.IntegerField()

    damage_dealt_to_buildings = models.IntegerField()
    baron_kills = models.IntegerField()

    objectives_stolen_assists = models.IntegerField()

    # Ping Stats
    all_in_pings = models.IntegerField()
    assist_me_pings = models.IntegerField()
    enemy_missing_pings = models.IntegerField()
    danger_pings = models.IntegerField()
    basic_pings = models.IntegerField()
    enemy_vision_pings = models.IntegerField()
    command_pings = models.IntegerField()
    get_back_pings = models.IntegerField()
    need_vision_pings = models.IntegerField()
    hold_pings = models.IntegerField()
    push_pings = models.IntegerField()
    bait_pings = models.IntegerField()
    on_my_way_pings = models.IntegerField()
    vision_cleared_pings = models.IntegerField()

    champion_transform = models.IntegerField()

    puuid = models.CharField(max_length=150)

    # Items
    items_purchased = models.IntegerField()
    item0 = models.IntegerField()
    item1 = models.IntegerField()
    item2 = models.IntegerField()
    item3 = models.IntegerField()
    item4 = models.IntegerField()
    item5 = models.IntegerField()
    item6 = models.IntegerField()

    # Spells and Abilities
    spell1_casts = models.IntegerField()
    spell2_casts = models.IntegerField()
    spell3_casts = models.IntegerField()
    spell4_casts = models.IntegerField()

    summoner1id = models.IntegerField()
    summoner2id = models.IntegerField()
    summoner1_casts = models.IntegerField()
    summoner2_casts = models.IntegerField()

    # Game Info
    win = models.BooleanField()

    first_blood_kill = models.BooleanField()
    first_blood_assist = models.BooleanField()

    first_tower_kill = models.BooleanField()
    first_tower_assist = models.BooleanField()
    game_ended_in_surrender = models.BooleanField()
    game_ended_in_early_surrender = models.BooleanField()
    team_early_surrendered = models.BooleanField()

    match = models.ForeignKey('data.Match', on_delete=models.CASCADE)
