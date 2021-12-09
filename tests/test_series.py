import pytest

from math_series.series import fibonacci, lucas

def test_fibonacci_zero():
  """
  This will test what the zero number of the fibonacci sequence is
  """
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_one():
  """
  This will test what the one number of the fibonacci sequence is
  """
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_two():
  """
  This will test what the two number of the fibonacci sequence is
  """
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_fibonacci_eight():
  """
  This will test what the two number of the fibonacci sequence is
  """
  actual = fibonacci(8)
  expected = 21
  assert actual == expected

def test_lucas_zero():
  """
  This will test what the two number of the fibonacci sequence is
  """
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test_lucas_one():
  """
  This will test what the two number of the fibonacci sequence is
  """
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test_lucas_two():
  """
  This will test what the two number of the fibonacci sequence is
  """
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test_lucas_eight():
  """
  This will test what the two number of the fibonacci sequence is
  """
  actual = lucas(8)
  expected = 47
  assert actual == expected

