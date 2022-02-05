# coding=utf-8
"""Async_func function test module."""
import hashlib
import time
from random import SystemRandom
from string import ascii_letters, digits

import pytest

import main


def generate_random_string(length: int = 40) -> str:
    """Return random string."""
    symbols = ascii_letters + digits
    random_symbol = SystemRandom().choice
    random_text = ''.join(random_symbol(symbols) for _ in range(length))
    return '{0}'.format(random_text)


def test_print_hash(capfd: pytest.CaptureFixture):
    """Check output hash."""
    some_data = generate_random_string()
    main.create_hash_output(some_data)
    captured_hash = capfd.readouterr()
    some_data_hash = hashlib.sha256(some_data.encode('utf-8')).hexdigest()
    assert captured_hash.out == some_data_hash


@pytest.mark.asyncio()
async def test_print_delay():
    """Check print delay."""
    random_text = generate_random_string()
    start = time.monotonic()
    await main.print_trainee_data(random_text)
    elapsed = time.monotonic() - start
    assert 1 <= float('{0:.1f}'.format(elapsed)) <= 5


@pytest.mark.asyncio()
async def test_print_data(capfd: pytest.CaptureFixture):
    """Check output data."""
    random_text = generate_random_string()
    await main.print_trainee_data(random_text)
    captured_text = capfd.readouterr()
    assert captured_text.out.rstrip() == random_text


@pytest.mark.asyncio()
async def test_main(capfd: pytest.CaptureFixture):
    """Check output list data."""
    await main.main_async(main.trainee_data)
    captured_text = capfd.readouterr()
    list_captured_text = sorted(captured_text.out.rstrip().split('\n'))
    assert list_captured_text == sorted(main.trainee_data)
