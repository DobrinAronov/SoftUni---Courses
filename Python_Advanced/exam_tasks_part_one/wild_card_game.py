def draw_cards(*args, **kwargs):
    input_dict = dict(args)
    input_dict.update(kwargs)

    monster_cards = {}
    spell_cards = {}

    for card_name, card_type in input_dict.items():
        if card_type == "monster":
            if card_type not in monster_cards:
                monster_cards[card_type] = []
            monster_cards[card_type].append(card_name)
        elif card_type == "spell":
            if card_type not in spell_cards:
                spell_cards[card_type] = []
            spell_cards[card_type].append(card_name)

    output = []
    if monster_cards:
        output.append("Monster cards:")
        for card_names in monster_cards.values():
            for name in sorted(card_names, reverse=True):
                output.append(f"  ***{name}")
    if spell_cards.values():
        output.append("Spell cards:")
        for card_names in spell_cards.values():
            for name in sorted(card_names):
                output.append(f"  $$${name}")

    return '\n'.join(output)


print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell",
                 destroy="spell", ))
