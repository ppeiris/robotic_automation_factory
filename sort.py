def sort(width: float, height: float, length: float, mass: float) -> str:
    """Dispatch a package to the correct stack based on its dimensions and mass.

    Args:
        width:  Package width in cm.
        height: Package height in cm.
        length: Package length in cm.
        mass:   Package mass in kg.

    Returns:
        "STANDARD", "SPECIAL", or "REJECTED".
    """
    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
