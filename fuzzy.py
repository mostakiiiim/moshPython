import numpy as np
import matplotlib.pyplot as plt

def speed_slow(x):
    return max(0, min((30 - x) / 30, 1))

def speed_medium(x):
    return max(0, min((abs(x - 50)) / 20, 1))

def speed_fast(x):
    return max(0, min((x - 70) / 30, 1))

def weight_light(x):
    return max(0, min((60 - x) / 60, 1))

def weight_medium(x):
    return max(0, min((abs(x - 80)) / 20, 1))

def weight_heavy(x):
    return max(0, min((x - 100) / 40, 1))

def distance_very_low(x):
    return max(0, min((1.5 - x) / 1.5, 1))

def distance_low(x):
    return max(0, min((2 - x) / 1.5, 1))

def distance_medium(x):
    return max(0, min((2.5 - x) / 1.5, 1))

def distance_high(x):
    return max(0, min((x - 2.5) / 1.5, 1))

def distance_very_high(x):
    return max(0, min((x - 3) / 1.5, 1))

def fuzzy_inference(speed, weight):
    # Fuzzification
    speed_mf = {'slow': speed_slow(speed), 'medium': speed_medium(speed), 'fast': speed_fast(speed)}
    weight_mf = {'light': weight_light(weight), 'medium': weight_medium(weight), 'heavy': weight_heavy(weight)}
    
    # Inference
    distances = {'very_low': min(speed_mf['slow'], weight_mf['light']),
                 'low': min(speed_mf['slow'], weight_mf['medium']),
                 'medium': min(speed_mf['slow'], weight_mf['heavy']),
                 'low_2': min(speed_mf['medium'], weight_mf['light']),
                 'medium_2': min(speed_mf['medium'], weight_mf['medium']),
                 'high': min(speed_mf['medium'], weight_mf['heavy']),
                 'medium_3': min(speed_mf['fast'], weight_mf['light']),
                 'high_2': min(speed_mf['fast'], weight_mf['medium']),
                 'very_high': min(speed_mf['fast'], weight_mf['heavy'])}
    
    # Defuzzification (Center of Gravity)
    distances_sum = 0
    membership_sum = 0
    for term, value in distances.items():
        if term == 'very_low':
            distances_sum += value * 0.75
            membership_sum += value
        elif term == 'low':
            distances_sum += value * 1.25
            membership_sum += value
        elif term == 'medium':
            distances_sum += value * 1.75
            membership_sum += value
        elif term == 'low_2':
            distances_sum += value * 1.25
            membership_sum += value
        elif term == 'medium_2':
            distances_sum += value * 1.75
            membership_sum += value
        elif term == 'high':
            distances_sum += value * 2.25
            membership_sum += value
        elif term == 'medium_3':
            distances_sum += value * 1.75
            membership_sum += value
        elif term == 'high_2':
            distances_sum += value * 2.25
            membership_sum += value
        elif term == 'very_high':
            distances_sum += value * 2.75
            membership_sum += value
            
    result = distances_sum / membership_sum if membership_sum != 0 else 0
    return result

# Calculate distance for Speed = 30, Car weight = 60
distance = fuzzy_inference(30, 60)
print("Distance to full stop:", distance, "tens of meters")
