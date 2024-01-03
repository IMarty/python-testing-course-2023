import pytest
from restaurant_reviews import RestaurantReviews

@pytest.fixture
def restaurant_reviews_with_two_restaurants():
    rr = RestaurantReviews()
    # Ajout des restaurants pour mes scénario
    rr.add_review("Cafe Mocha", "Great Coffe.", 4)
    rr.add_review("Cafe Burger", "Good Burger", 3)
    return rr