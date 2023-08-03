"""
To create a new python script called taxi_fare.py that helps a user calculate the taxi fare of a journey. 

1) Total taxi fare = Meter fare + Surcharges

1.1) Meter fare = Flag-down fare + Fare based on distance

1.1.1) Flag-down fare = fixed first 1km or less
1.1.2) Fare based on distance = Within 9.8km fare + Beyond 9.8km fare

1.1.2.1) Within 9.8km fare = (9.8km - 1km) // 400m * 400m rate. If quotient > 0, + 400m rate
1.1.2.1) Beyond 9.8km fare = (distance - 9.8km) // 350m * 350m rate. If quotient > 0, + 350m rate

1.2) Surcharges = Time-based surcharge + Location surcharge
1.2.1) Time-based surcharge = Meter fare * Time-based rate

Note: Peak period surcharge cannot coincide with late night surcharge
"""

PEAK_HOUR_RATE = 0.25
LATE_NIGHT_RATE = 0.5

# Second attempt
def calculate_meter_fare(distance, flag_down_rate, rate_400m, rate_350m):

    # When distance <= 1km
    meter_fare = flag_down_rate
    if distance <= 1000:
        return meter_fare
    
    # When distance > 9.8km
    if distance > 9800:
        meter_fare += (9800 - 1000) / 400 * rate_400m + (distance - 9800) // 350 * rate_350m
        if (distance - 9800) % 350 > 0:
            meter_fare += rate_350m
        return meter_fare
    
    # When 1km < distance <= 9.8km
    meter_fare += (distance - 1000) // 400 * rate_400m
    if (distance - 1000) % 350 > 0:
        meter_fare += rate_350m
    return meter_fare

'''
# First attempt
def calculate_meter_fare_alternate(distance, flag_down_rate, rate_400m, rate_350m):
    
    if distance <= 1000:                                # When distance <= 1km,
        return flag_down_rate                           # return meter fare
        
    else:                                               # When distance > 1km,
        total_fare = flag_down_rate                     # Add 1km rates into meter fare
        distance -= 1000
        
        if distance - 8800 <= 0:                        # When distance is within 9.8km, (distance <= 9.8km)
            total_fare += distance // 400 * rate_400m   # Next 8.8km, add into meter fare
            if distance % 400 > 0:                      # Checks for quotient, then add into meter fare, if any
                total_fare += rate_400m                 # return meter fare
            return total_fare
        
        else:                                           # When distance is beyond 9.8km, (distance > 9.8km)
            distance -= 8800                            # Next x km beyond 9.8km,
            total_fare += distance // 350 * rate_350m   # Add into meter fare
            if distance % 400 > 0:                      # Checks for quotient, then add into meter fare, if any
                total_fare += rate_350m                 # return meter fare
            return total_fare
'''       

def calculate_surcharge(meter_fare, is_peak_hour, is_midnight):
    if is_peak_hour == "yes":
        return meter_fare * PEAK_HOUR_RATE
    else:
        if is_midnight == "yes":
            return meter_fare * LATE_NIGHT_RATE
        return 0

# (1.1) Calculate meter fare
flag_down_fare = float(input("What's the flag-down fare: $"))
rate_400m_within = float(input("What's the rate per 400 meters within 9.8km? $"))
rate_350m_beyond = float(input("What's the rate per 350 meters beyond 9.8km? $"))
distance = int(input("What's the distance travelled (in meters)? "))
total_fare = calculate_meter_fare(distance, flag_down_fare, rate_400m_within, rate_350m_beyond)

# (1.2.1) Calculate surcharges (Time-based)
is_peak_hour = input("Is the ride during a peak period? [yes/no] ")
is_midnight = input("Is the ride between midnight and 6am? [yes/no] ") if is_peak_hour == "no" else "no"
total_fare += round(calculate_surcharge(total_fare, is_peak_hour, is_midnight), 2)

# (1.2.2) Add surcharges (Location-based), if any
have_location_surcharge = input("Is there any location surcharge? [yes/no] ")
if have_location_surcharge == "yes":
    total_fare += float(input("What's the amount of location surcharge? $"))

print("The total fare is $" + str(total_fare))




'''
# For fun
flag_rate = float(input("What's the flag down fare: $"))
rates_below_10 = float(input("What's the rate per 400 meters within 9.8km: $"))
rates_above_10 = float(input("What's the rate per 350 meters beyong 9.8km: $"))
distance = int(input("What's the distance traveled (in meters)? "))
is_peak = True if input("Is the ride during a peak period? [yes/no] ").upper() == 'YES' else False
is_midnight = True if (input("Is the ride between midnight and 6am? [yes/no] ") if is_peak == False else "no").upper() == 'YES' else False
location_charge = float(input("What's the amount of location surcharge: $")) if input("Is there any location surcharge? [yes/no] ").upper() == 'YES' else 0
print('The total fare is $' + str(round((flag_rate + ((rates_below_10 * (distance - 1000)/400 if distance % 400 == 0 else rates_below_10 * (((distance -1000)//400) + 1)) if distance > 1000 and distance <=  9800 else (rates_below_10 * (8800)/400 + rates_above_10 * ((distance - 9800)/350) if (distance - 9800) % 350 == 0 else rates_below_10 * (8800)/400 + rates_above_10 * (((distance - 9800)//350) + 1)))) * (1.25 if is_peak == True else 1.00) * (1.5 if is_midnight == True else 1.00) + location_charge ,2)))
'''




    