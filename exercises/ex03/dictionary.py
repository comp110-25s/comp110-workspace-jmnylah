"""Dictionary Functions"""

__author__: str = "730665624"


def invert(inp: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in inp:
        value = inp[key]
        if value in inverted:
            raise KeyError("duplicate key")
        inverted[value] = key
    return inverted


def count(items: list[str]) -> dict[str, int]:
    counted: dict[str, int] = {}
    for item in items:
        if item in counted:
            counted[item] += 1
        else:
            counted[item] = 1
    return counted


def favorite_color(colors: dict[str, str]) -> str:
    color: str = ""
    max = 0
    fav = count(list(colors.values()))
    for key in fav:
        if fav[key] > max:
            max = fav[key]
            color = key
    return color


def bin_len(objects: list[str]) -> dict[int, set[str]]:
    groups: dict[int, set[str]] = {}
    for element in objects:
        if len(element) in groups:
            groups[len(element)].add(element)
        else:
            groups[len(element)] = {element}
    return groups
