""" These are the tests for Advent of Code 2023, Day 1"""
# mypy: disable-error-code=no-untyped-def
from d1.puzzle import answer_p1, answer_p2, determine_line_calibration, determine_advanced_line_calibration


def test_answer_p1():
    """12, 38, 15, and 77. Adding these together produces 142.
    Test that our answer matches the example given by AOC for part 1
    """
    assert determine_line_calibration("1abc2") == 12
    assert determine_line_calibration("pqr3stu8vwx") == 38
    assert determine_line_calibration("a1b2c3d4e5f") == 15
    assert determine_line_calibration("treb7uchet") == 77
    assert answer_p1("test_input1") == 142


def test_answer_p2():
    """
    Test that our answer matches the example given by AOC for part 2
    """
    assert determine_advanced_line_calibration("two1nine") == 29
    assert determine_advanced_line_calibration("eightwothree") == 83
    assert determine_advanced_line_calibration("abcone2threexyz") == 13
    assert determine_advanced_line_calibration("xtwone3four") == 24
    assert determine_advanced_line_calibration("4nineeightseven2") == 42
    assert determine_advanced_line_calibration("zoneight234") == 14
    assert determine_advanced_line_calibration("7pqrstsixteen") == 76

    assert answer_p2("test_input2") == 281

    assert determine_advanced_line_calibration("eightwo") == 82  # SON OF A
    assert determine_advanced_line_calibration("eighthree") == 83  # SON OF A
    assert determine_advanced_line_calibration("twone") == 21  # SON OF A
    assert determine_advanced_line_calibration("nineight") == 98  # SON OF A
    assert determine_advanced_line_calibration("oneight") == 18  # SON OF A
    assert determine_advanced_line_calibration("fiveight") == 58  # SON OF A

    assert determine_advanced_line_calibration("one") == determine_advanced_line_calibration("1") == 11
    assert determine_advanced_line_calibration("two") == determine_advanced_line_calibration("2") == 22
    assert determine_advanced_line_calibration("three") == determine_advanced_line_calibration("3") == 33
    assert determine_advanced_line_calibration("four") == determine_advanced_line_calibration("4") == 44
    assert determine_advanced_line_calibration("five") == determine_advanced_line_calibration("5") == 55
    assert determine_advanced_line_calibration("six") == determine_advanced_line_calibration("6") == 66
    assert determine_advanced_line_calibration("seven") == determine_advanced_line_calibration("7") == 77
    assert determine_advanced_line_calibration("eight") == determine_advanced_line_calibration("8") == 88
    assert determine_advanced_line_calibration("nine") == determine_advanced_line_calibration("9") == 99

    assert determine_advanced_line_calibration("mpfjlf1twofbzzhl3ljpfc41") == 11
    assert determine_advanced_line_calibration("5pfzht") == 55
