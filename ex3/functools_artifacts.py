import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'),
        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'),
        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning')
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatch(value):
        return f"Unknown spell type: {type(value)}"

    @dispatch.register(int)
    def _(value):
        return f"{value} damage dealt"

    @dispatch.register(str)
    def _(value):
        return f"{value} played"

    @dispatch.register(list)
    def _(value):
        return (f"Multi-cast: {len(value)} "
                f"spells cast: {', '.join(v for v in value)}")

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} with power {power}"


def main() -> None:
    nembs = [10, 20, 30, 40]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(nembs, 'add')}")
    print(f"Product: {spell_reducer(nembs, 'multiply')}")
    print(f"Max: {spell_reducer(nembs, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(10): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
