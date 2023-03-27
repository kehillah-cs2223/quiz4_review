# An AQI of more than 100 is unhealthy for sensitive groups.
# Write a function that takes a dictionary of AQIs and prints out which places
# have an AQI greater than 100

def check_unhealthy_aqi(aqi_dictionary):
    return ### YOUR CODE HERE

############# Tests below (don't change these!) ############# 
monday_aqi = {
    "Sunnyvale": 105,
    "Los Altos": 90,
    "Palo Alto": 75,
    "San Jose": 120,
    "San Francisco": 110 
}
print(check_unhealthy_aqi(monday_aqi)) #Sunnyvale, San Jose, San Francisco
tuesday_aqi = {
    "Sunnyvale": 45,
    "Los Altos": 119,
    "Palo Alto": 107,
    "San Jose": 101,
    "San Francisco": 100 
}
print(check_unhealthy_aqi(tuesday_aqi)) #Los Altos, Palo Alto, San Jose
wednesday_aqi = {
    "Sunnyvale": 99,
    "Los Altos": 103,
    "Palo Alto": 45,
    "San Jose": 77,
    "San Francisco": 109 
}
print(check_unhealthy_aqi(wednesday_aqi)) #Los Altos, San Francisco

