#!/usr/bin/env python3
"""Concurrent coroutines execution."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []

    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
