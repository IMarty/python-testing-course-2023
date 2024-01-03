import pytest
from restaurant_reviews import RestaurantReviews

# @pytest.fixture.... -> conftest.py

@pytest.mark.parametrize("restaurant_title, review_text, review_rating, expected_output",[
    ("Cafe Mocha","Great coffee and pastries.", 4, "Review delete for Cafe Mocha."),
    ("Cafe Bürger","Great coffee and Bürger.", 2, "Review delete for Cafe Bürger."),
    ("Cafe Pizza","Great coffee and Pizza.", 3, "Review delete for Cafe Pizza."),
    ("Cafe Sushi","Great coffee and Sushi.", 5, "Review delete for Cafe Sushi."),
    ("Cafe Tacos","Great coffee and Tacos.", 1, "Review delete for Cafe Tacos."),
])

def test_remove_valid_review(restaurant_title, review_text, review_rating, expected_output):
    rr = RestaurantReviews()
    rr.add_review(restaurant_title, review_text, review_rating)
    result = rr.delete_review(restaurant_title)
    assert (result == expected_output)
    result2 = rr.get_review(restaurant_title) 
    assert(result2 == "Review not found.")


@pytest.mark.parametrize("non_existing_restaurant",[
    ("Cafe Mocha"),
    ("Cafe Bürger"),
    ("Cafe Pizza"),
    ("Cafe Sushi"),
    ("Cafe Tacos"),
])
# TODO: Check issue with parametrize and Exception here
def test_delete_non_existing(non_existing_restaurant):
    rr = RestaurantReviews()
    with pytest.raises(ValueError) as e:
        rr.delete_review(non_existing_restaurant)
    assert str(e.value) == "Review not found to delete."