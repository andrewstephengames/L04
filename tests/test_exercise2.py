import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing_at_5():
    assert is_passing(5) == True


# bug report 2
def test_r2_is_valid_password_eight_chars_with_digit():
    assert is_valid_password("abcdefgh1") == True


# bug report 3
def test_r3_clamp_out_of_low_range():
    assert clamp(10, 5, 15) == 10
