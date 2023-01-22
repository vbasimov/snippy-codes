# propety getter and setter example in User class
import pytest

MAX_RATING = 100

class User:
    name: str
    _rating: int

    def __init__(self, name) -> None:
        self.name = name
        self._rating = 0

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            self._rating = 0
        else:
            self._rating = min(value, MAX_RATING)


@pytest.mark.parametrize("new_value, expected_rating", [
    (0, 0), (10, 10), (-10, 0), (1000, 100)
])
def test_rating(new_value, expected_rating):
    user = User('Mike')

    user.rating = new_value

    assert user.rating == expected_rating


if __name__ == '__main__':
    pytest.main(["-v", "rating_property_limit.py"])
