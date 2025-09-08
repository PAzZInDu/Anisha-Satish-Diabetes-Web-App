def bmi_calculator(weight_kg, height_cm):
    height_m = float(height_cm) / 100  # convert cm → meters
    bmi = float(weight_kg) / (height_m ** 2)
    return round(bmi, 2)