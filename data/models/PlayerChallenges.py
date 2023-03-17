from django.db import models


class PlayerChallenges(models.Model):
    knock_enemy_into_team_and_kill = models.CharField(max_length=100)
    epic_monster_stolen_without_smite = models.CharField(max_length=100)
    kills_near_enemy_turret = models.CharField(max_length=100)
    k_turrets_destroyed_before_plates_fall = models.CharField(max_length=100)
    played_champ_select_position = models.CharField(max_length=100)
    baron_takedowns = models.CharField(max_length=100)
    takedowns_in_enemy_fountain = models.CharField(max_length=100)
    wards_guarded = models.CharField(max_length=100)
    aces_before15minutes = models.CharField(max_length=100)
    deaths_by_enemy_champs = models.CharField(max_length=100)
    max_cs_advantage_on_lane_opponent = models.CharField(max_length=100)
    kill_after_hidden_with_ally = models.CharField(max_length=100)
    took_large_damage_survived = models.CharField(max_length=100)
    stealth_wards_placed = models.CharField(max_length=100)
    control_wards_placed = models.CharField(max_length=100)
    gold_per_minute = models.CharField(max_length=100)
    multi_kills = models.CharField(max_length=100)
    survived_single_digit_hp_count = models.CharField(max_length=100)
    takedowns_in_alcove = models.CharField(max_length=100)
    kda = models.CharField(max_length=100)
    effective_heal_and_shielding = models.CharField(max_length=100)
    lost_an_inhibitor = models.CharField(max_length=100)
    danced_with_rift_herald = models.CharField(max_length=100)
    turret_plates_taken = models.CharField(max_length=100)
    outer_turret_executes_before_10_minutes = models.CharField(max_length=100)
    killed_champ_took_full_team_damage_survived = models.CharField(max_length=100)
    unseen_recalls = models.CharField(max_length=100)
    multi_kills_after_aggressive_flash = models.CharField(max_length=100)
    lane_minions_first_10_minutes = models.CharField(max_length=100)
    ward_takedowns_before_20_m = models.CharField(max_length=100)
    outnumbered_kills = models.CharField(max_length=100)
    max_kill_deficit = models.CharField(max_length=100)
    jungler_kills_early_jungle = models.CharField(max_length=100)
    land_skillshots_early_game = models.CharField(max_length=100)
    team_elder_dragon_kills = models.CharField(max_length=100)
    kill_participation = models.CharField(max_length=100)
    solo_kills = models.CharField(max_length=100)
    takedown_on_first_turret = models.CharField(max_length=100)
    had_afk_teammate = models.CharField(max_length=100)
    game_length = models.CharField(max_length=100)
    immobilize_and_kill_with_ally = models.CharField(max_length=100)
    multiturret_rift_herald_count = models.CharField(max_length=100)
    takedowns = models.CharField(max_length=100)
    solo_baron_kills = models.CharField(max_length=100)
    skillshots_dodged = models.CharField(max_length=100)
    quick_cleanse = models.CharField(max_length=100)
    scuttlecrab_kills = models.CharField(max_length=100)
    early_lan_in_g_phase_gold_exp_advantage = models.CharField(max_length=100)
    elder_dragon_kills_with_oppos_in_g_soul = models.CharField(max_length=100)
    complete_support_quest_in_time = models.CharField(max_length=100)
    twenty_minions_in_3seconds_count = models.CharField(max_length=100)
    dodge_skillshots_small_window = models.CharField(max_length=100)
    pick_kill_with_ally = models.CharField(max_length=100)
    legendary_count = models.CharField(max_length=100)
    more_enemy_jungle_than_opponent = models.CharField(max_length=100)
    blast_cone_opposite_opponent_count = models.CharField(max_length=100)
    kills_on_recently_healed_by_aram_pack = models.CharField(max_length=100)
    outnumbered_nexus_kill = models.CharField(max_length=100)
    takedowns_before_jungle_minion_spawn = models.CharField(max_length=100)
    kills_under_own_turret = models.CharField(max_length=100)
    full_team_takedown = models.CharField(max_length=100)
    kills_with_help_from_epic_monster = models.CharField(max_length=100)
    enemy_champion_immobilizations = models.CharField(max_length=100)
    flawless_aces = models.CharField(max_length=100)
    epic_monster_steals = models.CharField(max_length=100)
    vision_score_per_minute = models.CharField(max_length=100)
    elder_dragon_multi_kills = models.CharField(max_length=100)
    jungler_takedowns_near_damaged_epic_monster = models.CharField(max_length=100)
    turret_takedowns = models.CharField(max_length=100)
    enemy_jungle_monster_kills = models.CharField(max_length=100)
    initial_buff_count = models.CharField(max_length=100)
    team_rift_herald_kills = models.CharField(max_length=100)
    perfect_dragon_souls_taken = models.CharField(max_length=100)
    had_open_nexus = models.CharField(max_length=100)
    kills_on_laners_early_jungle_as_jungler = models.CharField(max_length=100)
    ward_takedowns = models.CharField(max_length=100)
    rift_herald_takedowns = models.CharField(max_length=100)
    damage_taken_on_team_percentage = models.CharField(max_length=100)
    initial_crab_count = models.CharField(max_length=100)
    survived_three_immobilizes_in_fight = models.CharField(max_length=100)
    save_ally_from_death = models.CharField(max_length=100)
    takedowns_after_gaining_level_advantage = models.CharField(max_length=100)
    team_damage_percentage = models.CharField(max_length=100)
    epic_monster_kills_within_30_seconds_of_spawn = models.CharField(max_length=100)
    multikill_one_spell = models.CharField(max_length=100)
    quick_solo_kills = models.CharField(max_length=100)
    poro_explosions = models.CharField(max_length=100)
    epic_monster_kills_near_enemy_jungler = models.CharField(max_length=100)
    quick_first_turret = models.CharField(max_length=100)
    max_level_lead_lane_opponent = models.CharField(max_length=100)
    jungle_cs_before_10_minutes = models.CharField(max_length=100)
    team_baron_kills = models.CharField(max_length=100)
    double_aces = models.CharField(max_length=100)
    allied_jungle_monster_kills = models.CharField(max_length=100)
    takedowns_first_x_minutes = models.CharField(max_length=100)
    dragon_takedowns = models.CharField(max_length=100)
    three_wards_one_sweeper_count = models.CharField(max_length=100)
    snowballs_hit = models.CharField(max_length=100)
    turrets_taken_with_rift_herald = models.CharField(max_length=100)
    ability_uses = models.IntegerField()
    vision_score_advantage_lane_opponent = models.CharField(max_length=100)
    bounty_gold = models.CharField(max_length=100)
    twelve_assist_streak_count = models.CharField(max_length=100)
    perfect_game = models.CharField(max_length=100)
    damage_per_minute = models.CharField(max_length=100)
    skillshots_hit = models.CharField(max_length=100)
    buffs_stolen = models.CharField(max_length=100)

    participant = models.ForeignKey("data.Participant", on_delete=models.CASCADE)
