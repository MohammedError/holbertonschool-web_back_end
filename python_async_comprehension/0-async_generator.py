#!/usr/bin/env python3
"""Async Generator Module."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times, waits 1 sec, and yields a random float."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
