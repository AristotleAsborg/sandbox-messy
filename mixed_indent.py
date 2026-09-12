"""Mixed tabs and spaces, on purpose.

This file is the fixture for "the linter will complain and be right".
Some lines are indented with a tab, some with four spaces; Python accepts it as
long as a single block is consistent, which is exactly why it survives review.
"""


def compute(value):
	"""Returns value doubled. Indented with a tab."""
	if value < 0:
		return 0
    return value * 2


def describe():
    """Indented with spaces, in the same file."""
	return "spaces then a tab, because why not"
