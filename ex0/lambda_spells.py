def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda art: art['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda power: power["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(
            sum(map(lambda x: x['power'], mages)) / len(mages), 2
            )
    }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Shadow Blade', 'power': 70, 'type': 'weapon'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)

    print("\nTesting artifact sorter...")
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before "
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)

    print("\nTesting spell transformer...")
    print(" ".join(transformed))


if __name__ == "__main__":
    main()
