#!/usr/bin/env python3

"""
Answer of lockboxes problem
"""

def can_unlock_all(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """

    if not isinstance(boxes, list):
        return False
    if not boxes:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx, box in enumerate(boxes):
            boxes_checked = k in box and k != idx
            if boxes_checked:
                break
        if not boxes_checked:
            return False
    return True
