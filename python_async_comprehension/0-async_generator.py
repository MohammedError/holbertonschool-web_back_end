#!/usr/bin/env python3
"""This module provides an asynchronous generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """This asynchronous generator yields random float values between 0 and 10."""
    for index in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

