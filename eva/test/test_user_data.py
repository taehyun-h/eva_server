from eva.protocol.data import user
import pytest


@pytest.fixture()
def default_user_object():
    pb_object = user.create_default_user("test_user")
    user_object = user.User(pb_object)
    return user_object


pytest.mark.default_user_object = \
    pytest.mark.parametrize('obj', [pytest.lazy_fixture('default_user_object')])


@pytest.mark.default_user_object
def test_update_today_study(obj):
    current_today_study_date = obj.today_study_date
    obj.update_today_study()

    assert current_today_study_date + 1 == obj.today_study_date


@pytest.mark.default_user_object
def test_update_today_study_multiple(obj):
    current_today_study_date = obj.today_study_date
    obj.update_today_study()
    obj.update_today_study()
    obj.update_today_study()

    assert current_today_study_date + 3 == obj.today_study_date


@pytest.mark.default_user_object
def test_add_studying_word(obj):
    obj.add_studying_word(123)
    obj.add_studying_word(50)

    studying_word = obj.studying_words[123]
    studying_word2 = obj.studying_words[50]

    assert studying_word.id == 123
    assert studying_word.studied_count == 0
    assert studying_word2.id == 50
    assert studying_word2.studied_count == 0
