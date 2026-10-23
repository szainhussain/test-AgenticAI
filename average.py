def average(numbers):
    """Return the arithmetic mean of a sequence of numbers.

    Args:
        numbers: An iterable of ints/floats.

    Returns:
        The arithmetic mean as a float.

    Raises:
        ValueError: If `numbers` is empty.
    """
    numbers = list(numbers)
    if not numbers:
        raise ValueError("average() arg is an empty sequence")
    return sum(numbers) / len(numbers)
