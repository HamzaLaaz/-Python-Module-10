def mage_counter() -> callable:
    count = 0

    def calling() -> int:
        nonlocal count
        count += 1
        return count
    return calling


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def add_to_total(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return add_to_total


def enchantment_factory(enchantment_type: str) -> callable:
    def inner_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner_enchantment


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return memory.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    calls = [1, 2, 3]
    enchantment_type = ['Flaming', 'Frozen']
    item_name = ['Sword', 'Shield']
    i = 0

    print("\nTesting mage counter...")
    call = mage_counter()
    for x in calls:
        print(f"Call {x}: {call()}")

    print("\nTesting enchantment factory...")
    for enchantment in enchantment_type:
        enchant = enchantment_factory(enchantment)
        print(enchant(item_name[i]))
        i += 1


if __name__ == "__main__":
    main()
