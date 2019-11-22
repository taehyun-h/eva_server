from eva.protocol.data import user
import pytest


pytest.mark.default_user_object = \
    pytest.mark.parametrize('obj', [pytest.lazy_fixture('default_user_object')])


@pytest.fixture()
def default_user_object():
    pb_object = user.create_default_user("default_user_object")
    user_object = user.User(pb_object)
    return user_object


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


@pytest.mark.default_user_object
def test_add_newly_studying_words(obj):
    obj.update_today_study()
    obj.add_newly_studying_words()

    orders = obj.studying_word_orders
    words = obj.studying_words

    assert obj.last_studied_word_id == user.NEW_STUDYING_WORDS_COUNT - 1
    assert len(orders) == user.NEW_STUDYING_WORDS_COUNT
    assert len(words) == user.NEW_STUDYING_WORDS_COUNT

    order = orders[1]
    assert order.order == obj.today_study_date


@pytest.mark.default_user_object
def test_study_current_index(obj):
    # todo
    pass


@pytest.mark.default_user_object
def test_i_know_current_test_index(obj):
    # todo
    pass


@pytest.mark.default_user_object
def test_i_dont_know_current_test_index(obj):
    # todo
    pass
