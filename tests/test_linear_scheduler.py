import pytest

from lr_schedules.linear_scheduler import LinearScheduler


def test_init():
    # Test correct initialization
    times = [0, 1]
    values = [0, 100]
    total_training_steps = 200
    scheduler = LinearScheduler(times, values, total_training_steps)
    assert scheduler.times == times
    assert scheduler.values == values
    assert scheduler.total_training_steps == total_training_steps

    # Test AssertionError when times and values lengths do not match
    with pytest.raises(AssertionError):
        LinearScheduler([0, 1], [0], total_training_steps)

    # Test AssertionError when times are not in ascending order
    with pytest.raises(AssertionError):
        LinearScheduler([1, 0], values, total_training_steps)

    # Test AssertionError when times are fractions and total_training_steps is not provided
    with pytest.raises(AssertionError):
        LinearScheduler([0, 0.5, 1], values)


def test_call():
    times = [0, 1]
    values = [0, 100]
    total_training_steps = 200
    scheduler = LinearScheduler(times, values, total_training_steps)

    # Test interpolation at step 0
    assert scheduler(0) == 0

    # Test interpolation at step 100 (middle point)
    assert scheduler(100) == 50

    # Test interpolation at step 200 (end point)
    assert scheduler(200) == 100

    # Test interpolation beyond total_training_steps
    assert scheduler(300) == 100
