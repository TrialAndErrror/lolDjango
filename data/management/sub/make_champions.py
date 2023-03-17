from data.models import Champion, ChampionImage, ChampionStats, ChampionTag, ChampionInfo


def make_champions(champ_data):
    for champ_name, champ_info in champ_data.items():
        champion = Champion.objects.create(
            version=champ_info["version"],
            champion_id=champ_info["id"],
            key=champ_info["key"],
            name=champ_info["name"],
            title=champ_info["title"],
            blurb=champ_info["blurb"],
            par_type=champ_info["partype"],
        )

        info = champ_info["info"]
        ChampionInfo.objects.create(
            attack=info['attack'],
            defense=info['defense'],
            magic=info['magic'],
            difficulty=info['difficulty'],
            champion=champion
        )

        image = champ_info["image"]
        ChampionImage.objects.create(
            full=image['full'],
            sprite=image['sprite'],
            group=image['group'],
            x=image['x'],
            y=image['y'],
            w=image['w'],
            h=image['h'],
            champion=champion
        )

        stats = champ_info["stats"]
        ChampionStats.objects.create(
            hp=stats["hp"],
            hp_per_level=stats["hpperlevel"],
            mp=stats["mp"],
            mp_per_level=stats["mpperlevel"],
            move_speed=stats["movespeed"],
            armor=stats["armor"],
            armor_per_level=stats["armorperlevel"],
            spell_block=stats["spellblock"],
            spell_block_per_level=stats["spellblockperlevel"],
            attack_range=stats["attackrange"],
            hp_regen=stats["hpregen"],
            hp_regen_per_level=stats["hpregenperlevel"],
            mp_regen=stats["mpregen"],
            mp_regen_per_level=stats["mpregenperlevel"],
            crit=stats["crit"],
            crit_per_level=stats["critperlevel"],
            attack_damage=stats["attackdamage"],
            attack_damage_per_level=stats["attackdamageperlevel"],
            attack_speed_per_level=stats["attackspeedperlevel"],
            attack_speed=stats["attackspeed"],
            champion=champion
        )

        tags = champ_info["tags"]
        for tag in tags:
            tag_obj, _ = ChampionTag.objects.get_or_create(name=tag)
            champion.tags.add(tag_obj)
