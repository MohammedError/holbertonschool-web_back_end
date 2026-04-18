#!/usr/bin/env python3
"""Async generator module."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generates 10 random numbers asynchronously."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
