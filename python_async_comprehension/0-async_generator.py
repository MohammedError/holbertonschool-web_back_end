#!/usr/bin/env python3
"""This module provides an asynchronous generator."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This coroutine loops 10 times and yields a random float."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

