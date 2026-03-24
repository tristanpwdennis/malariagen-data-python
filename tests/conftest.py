import random
import numpy as np
import pytest


@pytest.fixture(autouse=True, scope="session")
def seed_random():
    random.seed(42)
    np.random.seed(42)
