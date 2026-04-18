#!/usr/bin/env python3
"""Module that contains an asynchronous generator coroutine."""
import asyncio
import random
import typing


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """Loops 10 times, waits 1 second, and yields a random number."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
