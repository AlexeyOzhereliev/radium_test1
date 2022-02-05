# coding=utf-8
"""Test script radium."""
import asyncio
import hashlib
import sys
from random import SystemRandom

trainee_name = 'Алексей'
vacancy_title = 'Стажер-программист Python / Python Developer Trainee'
expected_salary = '70000 рублей'

trainee_data = [trainee_name, vacancy_title, expected_salary]


def create_hash_output(some_data: str) -> None:
    """Create data hash and print it out."""
    some_data_encode = some_data.encode('utf-8')
    some_data_hash = hashlib.sha256(some_data_encode).hexdigest()
    sys.stdout.write(some_data_hash)


def get_random_num() -> int:
    """Return a random number in the range from 1 to 5."""
    sys_random_obj = SystemRandom()
    return sys_random_obj.randint(1, 5)


async def print_trainee_data(single_data: str) -> None:
    """Print trainee data with a delay."""
    random_num = get_random_num()
    await asyncio.sleep(random_num)
    sys.stdout.write('{0}\n'.format(single_data))


async def main_async(data_list: list[str]) -> None:
    """Print all trainee data with a delay."""
    coroutines_gen = (
        print_trainee_data(single_data) for single_data in data_list
    )
    await asyncio.gather(*coroutines_gen)


if __name__ == '__main__':
    asyncio.run(main_async(trainee_data))
    some_data = sys.stdin.readline().rstrip()
    create_hash_output(some_data)
