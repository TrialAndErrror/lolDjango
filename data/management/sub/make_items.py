from data.models import Item, ItemTag, ItemImage, ItemEffect, ItemStats


def make_items(item_data):
    for item_id, item_info in item_data.items():
        item = Item.objects.create(
            name=item_info["name"],
            description=item_info['description'],
            colloq=item_info['colloq'],
            plaintext=item_info['plaintext'],
            gold_base=item_info['gold']['base'],
            gold_purchasable=item_info['gold']['purchasable'],
            gold_total=item_info['gold']['total'],
            gold_sell=item_info['gold']['sell'],
            maps_11=item_info['maps']['11'],
            maps_12=item_info['maps']['12'],
            maps_21=item_info['maps']['21'],
            maps_22=item_info['maps']['22'],
        )

        image = item_info["image"]
        ItemImage.objects.create(
            full=image['full'],
            sprite=image['sprite'],
            group=image['group'],
            x=image['x'],
            y=image['y'],
            w=image['w'],
            h=image['h'],
            item=item
        )

        stats = item_info["stats"]
        for name, value in stats.items():
            ItemStats.objects.create(
                name=name,
                number=value,
                item=item
            )

        if item_info.get('effect'):
            effects = item_info['effect']
            for name, value in effects.items():
                ItemEffect.objects.create(
                    name=name,
                    number=value,
                    item=item
                )

        tags = item_info["tags"]
        for tag in tags:
            tag_obj, _ = ItemTag.objects.get_or_create(name=tag)
            item.tags.add(tag_obj)

    # NotImplemented: Item creation tree
    # for item_id, item_info in item_data.items():
    #     print('Setup info creation')
