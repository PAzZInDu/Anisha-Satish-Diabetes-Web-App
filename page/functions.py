def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # convert cm → meters
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)