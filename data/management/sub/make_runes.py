from data.models import RuneCategory, RuneSelection, StatPerks


def make_runes(participant):
    styles = participant.get('styles')
    if styles:
        primary_rune_data = styles[0]
        secondary_rune_data = styles[1]

        category = RuneCategory.objects.create(
            description="1",
            style=primary_rune_data['style']
        )

        primary_selections = primary_rune_data['selections']
        for selection in primary_selections:
            RuneSelection.objects.create(
                perk=selection['perk'],
                var1=selection['var1'],
                var2=selection['var2'],
                var3=selection['var3'],
                category=category
            )

        secondary_selections = secondary_rune_data['selections']
        for selection in secondary_selections:
            RuneSelection.objects.create(
                perk=selection['perk'],
                var1=selection['var1'],
                var2=selection['var2'],
                var3=selection['var3'],
                category=category
            )

        stat_perks_data = participant['statPerks']

        StatPerks.objects.create(
            defense=stat_perks_data['defense'],
            flex=stat_perks_data['flex'],
            offense=stat_perks_data['offense']
        )
