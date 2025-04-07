"""How Much It Cost to host a tea party"""

__author__: str = "730665624"


def main_planner(guests: int) -> None:
    """What it takes to host a tea party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(guests * 2, guests * 3)))


def tea_bags(people: int) -> int:
    """Calculates total amount of tea bags for party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculates total amount of treats needed to go with tea for party"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
