import pytest
from password import validate_password

# Happy path 
def test_validate_password_valid():
    assert validate_password("Password123") is True

# Edge case
def test_validate_password_boundary():
    assert validate_password("Pass1234") is True
    assert validate_password("Pass123") is False

# Exception case
def test_validate_password_non_string():
    with pytest.raises(TypeError):
        validate_password(12345678)