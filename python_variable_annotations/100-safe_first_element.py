#!/usr/bin/env python3
"""Task 10"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Safe first element"""
    if lst:
        return lst[0]
    else:
        return None
