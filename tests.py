#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2022
month = 9
day = 17

def test_code():
    assert main.wordSmash("Cat", "Dog") == "CatDog", "Cat + Dog == CatDog failed"
    assert main.wordSmash("Red", "blue") == "Redblue", "Red + blue == Redblue failed"
    assert main.wordSmash("qqqqq", "wwwww") == "qqqqqwwwww", "qqqqq + wwwww == qqqqqwwwww failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
