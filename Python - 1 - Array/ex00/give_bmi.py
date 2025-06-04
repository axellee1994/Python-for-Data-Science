def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height values must be integers or float")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight values must be integers or float")
    

    bmi = [weight[i] / (height[i] ** 2) for i in range(len(height))]
    return [bmi for bmi in bmi]
    

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI values must be integers or float")
    return [b > limit for b in bmi]