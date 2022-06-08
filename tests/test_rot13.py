import pytest

from ciphering.rot13 import Rot13


@pytest.fixture
def rot13():
    return Rot13()


def test_should_return_string_when_any_text_is_typed_in(rot13):
    text = 'rand_rext'
    text = rot13.encrypt(text)

    assert type(text) == str


def test_should_return_valid_encoded_value_when_any_text_is_typed_in(rot13):
    text = 'rand_rext'
    encrypted_text = rot13.encrypt(text)
    expected_result = 'C2?50C6IE'

    assert encrypted_text == expected_result