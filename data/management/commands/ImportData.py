from django.core.management.base import BaseCommand

from data.management.sub.make_champions import make_champions
from data.management.sub.make_items import make_items
from data.management.sub.make_match import make_match
from data.management.sub.make_participant import make_participant
from data.management.sub.make_runes import make_runes
from data.management.sub.make_team import make_team
from pathlib import Path
import json


def load_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)


class Command(BaseCommand):
    help = 'Import Data'

    def handle(self, *args, **options):
        print("Processing Champions")
        champions = load_data("champions_list.json")['data']
        make_champions(champions)

        print("Processing Items")
        items = load_data("item_data.json")['data']
        make_items(items)

        all_match_files = Path("matches").glob("*.json")

        count = 1
        for file in all_match_files:
            current_data = load_data(file)
            print(f"Processing Match {current_data['metadata']['matchId']} ({count})")

            data_version = current_data['metadata'].get('dataVersion')
            match_id = current_data['metadata'].get('matchId')

            info_dict = current_data['info']
            match = make_match(info_dict, data_version, match_id)

            teams = info_dict['teams']
            for team in teams:
                make_team(team, match)

            participants = info_dict['participants']
            
            for participant in participants:
                make_participant(participant, match)
                make_runes(participant)

            count += 1

