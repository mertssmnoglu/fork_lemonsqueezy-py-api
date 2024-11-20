from random import random

import pytest

from lemonsqueezy.api.customer import list_customers
from lemonsqueezy.api.product import list_products
from lemonsqueezy.api.store import list_stores


@pytest.fixture
def store_id():
    stores = list_stores()
    assert stores != [], "No stores available."
    return stores[int(random() * len(stores))].id_


@pytest.fixture
def customer_id():
    customers = list_customers()
    assert customers != [], "No customers available."
    return customers[int(random() * len(customers))].id_


@pytest.fixture
def product_id():
    products = list_products()
    assert products != [], "No products available."
    return products[int(random() * len(products))].id_
