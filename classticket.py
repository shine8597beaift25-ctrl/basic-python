#q5 Train Ticket Fare Calculator
# Create class Ticket storing:
# passenger name
# distance (in km)
# Task:
# Fare Rules:
# First 5 km → ₹20/km
# After 5 km → ₹15/km
# Write a method that calculates total fare based on distance
# class Ticket:
#     def __init__(self,name,distance):
#         self.name = name
#         self.distance = distance
#     def calculate_fare(self):
#         if self.distance <=5:
#             fare = self.distance *20
#         else:
#             fare = (5+20) + ((self.distance-5)*15)
#             return fare
# fare=Ticket("Rayna",50)
# fare=Ticket("maanya",30)
# print(fare.name,fare.calculate_fare())

