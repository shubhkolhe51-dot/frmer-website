def format_inr(amount: float | int) -> str:
    """
    Format a number into Indian Rupee representation (e.g., ₹1,50,000).
    """
    if amount is None:
        return "₹0"
    num_int = int(round(amount))
    is_neg = num_int < 0
    num_str = str(abs(num_int))

    if len(num_str) <= 3:
        res = num_str
    else:
        last3 = num_str[-3:]
        remaining = num_str[:-3]
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        res = ",".join(groups) + "," + last3

    prefix = "-₹" if is_neg else "₹"
    return f"{prefix}{res}"
