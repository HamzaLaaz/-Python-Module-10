def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    ...


def mage_stats(mages: list[dict]) -> dict:
    ...


def main():
    artifacte = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 70, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 100, 'type': 'weapon'},
        {'name': 'Fire Staff', 'power': 85, 'type': 'weapon'}
    ]
    hala = artifact_sorter(artifacte)
    print(hala)


main()
