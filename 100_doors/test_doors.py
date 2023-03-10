import pytest
from doors import Door, Row, Passer, doors_to_string

def test_door():
    door = Door(number=1, is_open=False)
    assert not door.is_open
    door.toggle()
    assert door.is_open

def test_row_has_correct_number_of_doors():
    row = Row(doors=100)
    assert row.number_of_doors == 100

def test_opened_and_closed():
    row = Row(doors=5)
    row.toggle(door=2)
    assert row.opened == [2]
    assert row.closed == [1, 3, 4, 5]

def test_first_pass():
    row = Row(doors=100)
    passer = Passer(row)
    passer.pass_by(toggle_each=1)
    assert row.closed == []

@pytest.mark.parametrize("doors,toggle_each,opened",
                         [
                             (100, 1, list(range(1, 101))),
                             (10, 2, [2, 4, 6, 8, 10]),
                             (11, 2, [2, 4, 6, 8, 10]),
                             (10, 3, [3, 6, 9]),
                             (11, 3, [3, 6, 9]),
                             (100, 50, [50, 100]),
                             (100, 99, [99]),
                             (100, 100, [100])
                         ])
def test_pass(doors, toggle_each, opened):
    row = Row(doors=doors)
    passer = Passer(row)
    passer.pass_by(toggle_each=toggle_each)
    assert row.opened == opened

def test_make_3_passes():
    row = Row(doors=5)
    passer = Passer(row)
    passer.make_n_passes(3)

    assert row.opened == [1, 5]

def test_format_door_numbers():
    row = Row(doors=5)
    row.toggle(door=2)
    row.toggle(door=4)
    door_string = doors_to_string(row.opened)
    assert door_string == "2, 4"
