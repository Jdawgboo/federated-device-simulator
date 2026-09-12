"""Simulate deterministic weighted aggregation across devices."""
from __future__ import annotations

from typing import Mapping


def aggregate(updates: list[Mapping[str, float]], weights: list[float]) -> dict[str, float]:
    """Compute weighted coordinate averages for compatible device updates."""
    if not updates or len(updates) != len(weights) or sum(weights) <= 0:
        raise ValueError("updates and positive weights are required")
    keys = set(updates[0])
    if any(set(update) != keys for update in updates):
        raise ValueError("all updates must share keys")
    total = sum(weights)
    return {key: round(sum(update[key] * weight for update, weight in zip(updates, weights)) / total, 10) for key in sorted(keys)}
