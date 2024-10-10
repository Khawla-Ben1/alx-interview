#!/usr/bin/python3
"""
Each box of n number is numbered
sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""


def canUnlockAll(box):
    """
    Determine if all the boxes can be opened.

    :param box: A list of lists representing boxes with keys to other boxes.
    :return: True if all boxes can be opened, otherwise False.
    """
    if not box or type(box) is not list:
        return False
    unlocked_boxes = [0]
    for current_box in unlocked_boxes:
        for key in box[current_box]:
            if key not in unlocked_boxes and key < len(box):
                unlocked_boxes.append(key)
    if len(unlocked_boxes) == len(box):
        return True
    else:
        return False
