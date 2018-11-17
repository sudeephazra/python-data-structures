import CreditCard


# Test 1 - Creating an object with default parameters
def test_object_creation_default_parameters():
    card = CreditCard.CreditCard()
    assert card.get_name() == 'John Doe'


def test_object_creation_non_default_position_parameters():
    card = CreditCard.CreditCard(name = 'Sudeep Hazra')
    assert card.get_name() == 'Sudeep Hazra'
    assert card.get_balance() == 0.0
    assert card.get_limit() == 0.0


def test_object_creation_non_default_paremeters():
    card = CreditCard.CreditCard('Jane Doe', 10000, 0.16)
    assert card.get_name() == 'Jane Doe'
    assert card.get_limit() == 10000
    assert card.get_balance() == 0.16


# Test getters and setters

# Test operator overloading


