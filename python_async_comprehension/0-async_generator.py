#!/usr/bin/env python3
"""Module that defines an asynchronous generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This asynchronous generator produces 10 random float numbers between 0 and 10, pausing for one second between each value."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
