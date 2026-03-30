def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> tuple:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage_spell(damage: int) -> int:
        return damage

    def is_enemy(target: str) -> bool:
        return target == "Dragon"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print("\nTesting power amplifier...")
    original_damage = 10
    mega_fireball = power_amplifier(damage_spell, 3)
    result = mega_fireball(original_damage)
    print(f"Original: {original_damage}, Amplified: {result}")
    # caster = conditional_caster(is_enemy, fireball)
    # print(caster("Dragon"))
    # print(caster("hamza"))
    # sequence = spell_sequence([fireball, heal])
    # print(sequence("Knight"))
