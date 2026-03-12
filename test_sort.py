import pytest
from sort import sort


# --- STANDARD packages (not bulky, not heavy) ---

def test_standard_small_light():
    assert sort(10, 10, 10, 5) == "STANDARD"

def test_standard_just_under_thresholds():
    # Volume = 999,999, dimension < 150, mass < 20
    assert sort(99, 100, 101, 19.9) == "STANDARD"

def test_standard_minimal():
    assert sort(1, 1, 1, 1) == "STANDARD"


# --- SPECIAL packages (bulky only) ---

def test_special_bulky_by_volume():
    # Volume = 1,000,000 exactly
    assert sort(100, 100, 100, 10) == "SPECIAL"

def test_special_bulky_by_volume_over():
    assert sort(200, 200, 200, 10) == "SPECIAL"

def test_special_bulky_by_single_dimension():
    # One dimension = 150, volume well under threshold
    assert sort(150, 1, 1, 1) == "SPECIAL"

def test_special_bulky_by_dimension_height():
    assert sort(1, 150, 1, 5) == "SPECIAL"

def test_special_bulky_by_dimension_length():
    assert sort(1, 1, 150, 5) == "SPECIAL"

def test_special_bulky_dimension_over_150():
    assert sort(200, 10, 10, 5) == "SPECIAL"


# --- SPECIAL packages (heavy only) ---

def test_special_heavy_exactly_20():
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_special_heavy_over_20():
    assert sort(10, 10, 10, 50) == "SPECIAL"


# --- REJECTED packages (both bulky and heavy) ---

def test_rejected_bulky_volume_and_heavy():
    assert sort(100, 100, 100, 20) == "REJECTED"

def test_rejected_bulky_dimension_and_heavy():
    assert sort(150, 1, 1, 20) == "REJECTED"

def test_rejected_all_large():
    assert sort(200, 200, 200, 100) == "REJECTED"


# --- Edge cases ---

def test_zero_dimensions():
    assert sort(0, 0, 0, 0) == "STANDARD"

def test_zero_mass_bulky():
    assert sort(150, 150, 150, 0) == "SPECIAL"

def test_float_inputs():
    # 99.5 * 100.5 * 100.0 = 999,975 < 1M, no dim >= 150, mass < 20
    assert sort(99.5, 100.5, 100.0, 19.99) == "STANDARD"

def test_very_heavy_tiny_package():
    assert sort(1, 1, 1, 1000) == "SPECIAL"

def test_boundary_volume_exactly_1m():
    # 100 * 100 * 100 = 1,000,000
    assert sort(100, 100, 100, 19) == "SPECIAL"

def test_boundary_volume_just_under_1m():
    assert sort(99, 100, 100, 19) == "STANDARD"  # 990,000 < 1M


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
