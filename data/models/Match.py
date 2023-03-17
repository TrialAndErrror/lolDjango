from django.db import models


class MetaData(models.Model):
    data_version = models.CharField(max_length=100)
    match_id = models.CharField(max_length=100)
    participants = models.CharField(max_length=100)

    match = models.ForeignKey("data.Match", on_delete=models.CASCADE)


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
