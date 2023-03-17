from django.db import models

# Generated using https://www.p2sdev.com/projects/json-to-orm-converter


# Create your models here.
class MetaData(models.Model):
    data_version = models.CharField(max_length=100)
    match_id = models.CharField(max_length=100)
    participants = models.CharField(max_length=100)


class Participant(models.Model):
    role = models.CharField(max_length=100)
    teamid = models.IntegerField()

    summonername = models.CharField(max_length=100)
    summonerid = models.CharField(max_length=100)
    summonerlevel = models.IntegerField()
    timeplayed = models.IntegerField()

    win = models.BooleanField()
    firstbloodkill = models.BooleanField()
    firsttowerassist = models.BooleanField()

    championid = models.IntegerField()
    championname = models.CharField(max_length=100)
    champlevel = models.CharField(max_length=100)
    champexperience = models.IntegerField()

    lane = models.CharField(max_length=100)
    teamposition = models.CharField(max_length=100)

    assists = models.CharField(max_length=100)
    deaths = models.CharField(max_length=100)
    neutralminionskilled = models.CharField(max_length=100)
    totalminionskilled = models.IntegerField()
    bountylevel = models.CharField(max_length=100)
    longesttimespentliving = models.IntegerField()

    goldearned = models.IntegerField()
    goldspent = models.IntegerField()

    visionscore = models.CharField(max_length=100)
    sightwardsboughtingame = models.CharField(max_length=100)
    visionwardsboughtingame = models.CharField(max_length=100)
    detectorwardsplaced = models.CharField(max_length=100)


    # Damage and Healing
    totalheal = models.IntegerField()
    totalhealsonteammates = models.CharField(max_length=100)
    totalunitshealed = models.CharField(max_length=100)
    totaldamageshieldedonteammates = models.CharField(max_length=100)

    totaldamagetaken = models.IntegerField()
    damageselfmitigated = models.IntegerField()
    magicdamagetaken = models.IntegerField()
    physicaldamagetaken = models.IntegerField()

    magicdamagedealt = models.IntegerField()
    physicaldamagedealt = models.IntegerField()
    physicaldamagedealttochampions = models.IntegerField()
    truedamagedealt = models.IntegerField()
    totaldamagedealttochampions = models.IntegerField()
    truedamagedealttochampions = models.CharField(max_length=100)
    timeccingothers = models.CharField(max_length=100)

    # Objective Stats
    damagedealttoobjectives = models.IntegerField()
    damagedealttoturrets = models.IntegerField()
    firsttowerkill = models.BooleanField()
    objectivesstolen = models.CharField(max_length=100)
    inhibitorkills = models.CharField(max_length=100)
    dragonkills = models.CharField(max_length=100)
    nexuskills = models.CharField(max_length=100)
    nexustakedowns = models.CharField(max_length=100)
    nexuslost = models.CharField(max_length=100)
    turrettakedowns = models.CharField(max_length=100)
    damagedealttobuildings = models.IntegerField()
    inhibitorslost = models.CharField(max_length=100)
    baronkills = models.CharField(max_length=100)

    # Kill Stats
    kills = models.CharField(max_length=100)
    doublekills = models.CharField(max_length=100)
    quadrakills = models.CharField(max_length=100)
    pentakills = models.CharField(max_length=100)
    unrealkills = models.CharField(max_length=100)

    largestmultikill = models.CharField(max_length=100)
    killingsprees = models.CharField(max_length=100)

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

    
    profile_icon = models.IntegerField()
    eligibleforprogression = models.BooleanField()

    championtransform = models.CharField(max_length=100)
    consumablespurchased = models.CharField(max_length=100)
    inhibitortakedowns = models.CharField(max_length=100)
    turretslost = models.CharField(max_length=100)
    gameendedinearlysurrender = models.BooleanField()
    riotidname = models.CharField(max_length=100)

    firstbloodassist = models.BooleanField()
    largestkillingspree = models.CharField(max_length=100)
    totaldamagedealt = models.IntegerField()
    turretkills = models.CharField(max_length=100)
    largestcriticalstrike = models.CharField(max_length=100)
    summoner1casts = models.CharField(max_length=100)
    objectivesstolenassists = models.CharField(max_length=100)
    individualposition = models.CharField(max_length=100)
    truedamagetaken = models.IntegerField()
    magicdamagedealttochampions = models.IntegerField()
    wardskilled = models.CharField(max_length=100)
    teamearlysurrendered = models.BooleanField()
    totaltimeccdealt = models.IntegerField()
    wardsplaced = models.CharField(max_length=100)
    puuid = models.CharField(max_length=100)
    spell3casts = models.IntegerField()
    triplekills = models.CharField(max_length=100)
    riotidtagline = models.CharField(max_length=100)

    totaltimespentdead = models.IntegerField()


    gameendedinsurrender = models.BooleanField()
    participantid = models.CharField(max_length=100)

    # Items
    itemspurchased = models.CharField(max_length=100)
    item0 = models.IntegerField()
    item1 = models.IntegerField()
    item2 = models.IntegerField()
    item3 = models.CharField(max_length=100)
    item4 = models.CharField(max_length=100)
    item5 = models.CharField(max_length=100)
    item6 = models.IntegerField()

    spell1casts = models.IntegerField()
    spell2casts = models.IntegerField()
    spell4casts = models.CharField(max_length=100)

    summoner1id = models.IntegerField()
    summoner2id = models.CharField(max_length=100)
    summoner2casts = models.CharField(max_length=100)


class Match(models.Model):
    game_id = models.CharField(max_length=100)
    game_version = models.CharField(max_length=100)
    map_id = models.IntegerField()

    queue_id = models.IntegerField()
    game_mode = models.CharField(max_length=50)
    game_type = models.CharField(max_length=50)

    game_name = models.CharField(max_length=100)
    platform_id = models.CharField(max_length=100)
    tournament_code = models.CharField(max_length=100)

    game_creation = models.IntegerField()
    game_start_timestamp = models.IntegerField()
    game_end_timestamp = models.IntegerField()
    game_duration = models.IntegerField()

    participants = models.ForeignKey()
    teams = models.ForeignKey()