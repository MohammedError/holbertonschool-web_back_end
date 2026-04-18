#!/usr/bin/env python3
"""This module defines an asynchronous generator that yields random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This asynchronous generator yields 10 random float numbers between 0 and 10, waiting 1 second between each yield."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

