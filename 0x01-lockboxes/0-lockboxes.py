#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIds = unseen_boxes.pop()
        if not boxIds or boxIds >= n or boxIds < 0:
            continue
        if boxIds not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIds])
            seen_boxes.add(boxIds)
    return n == len(seen_boxes)
