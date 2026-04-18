#!/usr/bin/env python3
"""Module that defines an asynchronous generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate random float numbers asynchronously."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

