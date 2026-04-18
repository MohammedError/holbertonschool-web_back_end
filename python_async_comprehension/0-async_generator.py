#!/usr/bin/env python3
"""Module for asynchronous generator."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate random float numbers between 0 and 10 asynchronously."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

