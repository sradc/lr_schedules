import numpy as np
import pytest

from lr_schedules.interp import interp


def test_interp_basic_cases():
    # Test basic linear interpolation
    assert interp(0, [0, 1], [0, 1]) == 0
    assert interp(0.5, [0, 1], [0, 1]) == 0.5
    assert interp(1, [0, 1], [0, 1]) == 1


def test_interp_with_numpy():
    # Test more complex examples using numpy's interp
    times = np.linspace(0, 1, 10)
    values = np.linspace(0, 1, 10)
    assert np.allclose(interp(0.5, times, values), np.interp(0.5, times, values))


def test_interp_with_random_numbers():
    # Test interpolation with random numbers
    rng = np.random.RandomState(0)
    x = np.linspace(0, 1, 10)
    y = rng.rand(10)
    assert np.allclose(interp(0.5, x, y), np.interp(0.5, x, y))


def test_interp_with_squared_x_values():
    # Test interpolation where x values are squared
    rng = np.random.RandomState(0)
    x = np.linspace(0, 1, 10) ** 2
    y = rng.rand(10)
    for value in np.linspace(0, 1, 10):
        assert np.allclose(interp(value, x, y), np.interp(value, x, y))


def test_interp_with_edge_cases():
    # Test interpolation with edge cases
    rng = np.random.RandomState(0)
    x = np.linspace(0, 1, 10) ** 2
    y = rng.rand(10)
    assert np.allclose(interp(2, x, y), np.interp(2, x, y))  # x value outside range
    assert np.allclose(interp(-1, x, y), np.interp(-1, x, y))  # x value outside range


def test_interp_with_empty_arrays():
    # Allowed to fail if arrays are empty
    with pytest.raises(IndexError):
        interp(0.5, [], [])


def test_interp_with_non_monotonic_x():
    x = [0, 1, 0]
    y = [0, 1, 0]
    assert np.allclose(interp(2, x, y), np.interp(2, x, y))


def test_interp_non_uniform_x():
    # Test interpolation with non-uniform spacing in x
    x = [0, 0.2, 0.5, 0.8, 1]
    y = [0, 0.5, 1, 0.5, 0]
    assert np.allclose(interp(0.3, x, y), np.interp(0.3, x, y))


def test_interp_exact_x_values():
    # Test interpolation at the exact x-values
    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 1, 10)
    for value in x:
        assert np.allclose(interp(value, x, y), np.interp(value, x, y))


def test_interp_non_numeric_values():
    # Test interpolation with non-numeric values
    with pytest.raises(TypeError):
        interp("a", [0, 1], [0, 1])


def test_interp_single_value_arrays():
    # Test interpolation with single-value arrays
    assert interp(0.5, [1], [1]) == 1


def test_interp_different_sizes():
    # We don't raise exceptions here, because checking slower
    # will check in the class init
    interp(0.5, [0, 1], [0, 1, 2])
    interp(0.5, [0, 1, 2, 3], [0, 1, 2])
