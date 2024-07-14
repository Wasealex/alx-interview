# Unlock All Boxes

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - 1` and each box may contain keys to the other boxes.

## Method Signature

```python
def canUnlockAll(boxes: List[List[int]]) -> bool:
```

## Parameters

- `boxes`: A list of lists representing the boxes and their corresponding keys. Each inner list represents a box and contains integers representing the keys it holds.

## Return Value

- Returns `True` if all boxes can be opened, else returns `False`.

## Assumptions

- A key with the same number as a box opens that box.
- All keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.

## Example

```python
boxes = [[1], [2], [3], []]
canUnlockAll(boxes)  # Returns True
```

In the above example, we have 4 boxes. Box 0 contains a key to Box 1, Box 1 contains a key to Box 2, Box 2 contains a key to Box 3, and Box 3 does not have any keys. Since all boxes can be opened by following the keys, the method returns `True`.
