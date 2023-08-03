# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

def get_promotion(food_category):
    # Replace the code below with your implementation.
    promotion = "No Promotion"
    if food_category == "vegetable" or food_category == "vegetables":
        promotion = "5%"
    elif food_category == "fruit" or food_category == "fruits":
        promotion = "7.5%"
    elif food_category == "seasoning" or food_category == "seasonings":
        promotion = "3%"
    elif food_category == "flour" or food_category == "flours":
        promotion = "10%"
    else:
        promotion = "No Promotion"
    return promotion