def convert_land_to_acre(value: float, unit: str) -> float:
    """
    Convert land area units (Guntha, Hectare, Bigha, Acre) to Acre.
    """
    unit_lower = unit.lower().strip()
    if unit_lower == "guntha":
        return round(value / 40.0, 4)
    elif unit_lower == "hectare":
        return round(value * 2.47105, 4)
    elif unit_lower == "bigha":
        return round(value * 0.619, 4)
    else:
        return float(value)

def convert_quintal_to_kg(quintal: float) -> float:
    """
    Convert quintals to kilograms (1 Quintal = 100 kg).
    """
    return float(quintal * 100.0)

def convert_quintal_to_ton(quintal: float) -> float:
    """
    Convert quintals to metric tons (1 Metric Ton = 10 Quintals).
    """
    return float(quintal / 10.0)
