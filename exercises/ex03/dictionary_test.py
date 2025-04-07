"""Dictionary Functions Unit Tests"""

__author__: str = "730665624"


from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use() -> None:
    """Test use case for the invert function."""
    assert invert({"Jimmy": "Jey"}) == {"Jey": "Jimmy"}


def test_invert_use_continued() -> None:
    """Test use case again for the invert function."""
    assert invert({"Jonathan": "Joshua"}) == {"Joshua": "Jonathan"}


def test_invert_edge_empty() -> None:
    """Test empty string in invert function."""
    assert invert({"Usos": ""}) == {"": "Usos"}


def test_count_use() -> None:
    """Test use case for the count function."""
    assert count(["red", "red", "green"]) == {"red": 2, "green": 1}


def test_count_same() -> None:
    """Test to see if the same thing in the count function will produce one output."""
    assert count(["tag", "tag", "tag"]) == {"tag": 3}


def test_county_empty() -> None:
    """Test to see if empty list will work in count function."""
    assert count([""]) == {"": 1}


def test_favorite_color_use() -> None:
    """Test use case for favorite_color function"""
    assert favorite_color({"Nylah": "Blue", "Jey": "Red", "Jimmy": "Red"}) == "Red"


def test_favorite_color_same() -> None:
    """Test to see if same color will work for the favorite_color function"""
    assert favorite_color({"Ny": "Blue", "Jey": "Blue", "Jimmy": "Blue"}) == "Blue"


def test_favorite_color_different() -> None:
    """Test to see if all different colors will have a fav in the favorite_color fn"""
    assert favorite_color({"Nylah": "Blue", "Jey": "Red", "Jimmy": "Gold"}) == "Blue"


def test_bin_len_use() -> None:
    """Test use case for bin length function."""
    assert bin_len(["Jey", "Jim", "Naomi"]) == {3: {"Jey", "Jim"}, 5: {"Naomi"}}


def test_bin_len_different() -> None:
    """Test to see if all different lengths are added to set for bin length fn."""
    assert bin_len(["BigJim", "Nylah", "Jey"]) == {
        6: {"BigJim"},
        5: {"Nylah"},
        3: {"Jey"},
    }


def test_bin_len_empty() -> None:
    """Test to see if empty strings will give me 0 for bin_length function"""
    assert bin_len([""]) == {0: ""}
