import os
import csv
# stateMapDirectory = '/home/m/PycharmProjects/mapsProject/allPdfs'
# half1 = ['ALABAMA', 'ALABAMA-FLORIDA', 'ALABAMA-GEORGIA', 'ARIZONA', 'ARIZONA-NEW MEXICO', 'ARIZONA-SONORA', 'ARKANSAS', 'ARKANSAS-LOUISIANA', 'ARKANSAS-MISSISSIPPI', 'ARKANSAS-MISSOURI', 'ARKANSAS-OKLAHOMA', 'CALIFORNIA', 'CALIFORNIA-NEVADA', 'CALIFORNIA-OREGON', 'CAROLINA-SOUTH CAROL', 'COLORADO', 'COLORADO-KANSAS', 'COLORADO-UTAH', 'COLORADO-WYOMING', 'FLORIDA', 'FLORIDA-ALABAMA', 'FLORIDA-GEORGIA', 'GEORGIA', 'GEORGIA-FLORIDA', 'GEORGIA-NORTH CAROLI', 'GEORGIA-SOUTH CAROLI', 'GEORGIA-TENNESSEE', 'IDAHO', 'IDAHO-MONTANA', 'IDAHO-NEVADA', 'IDAHO-OREGON', 'IDAHO-UTAH', 'IDAHO-WASHINGTON', 'IDAHO-WYOMING', 'ILLINOIS', 'ILLINOIS-KENTUCKY', 'ILLINOIS-MISSOURI', 'INDIANA', 'INDIANA-KENTUCKY', 'KANSAS', 'KANSAS-OKLAHOMA', 'KENTUCKY', 'KENTUCKY-ILLINOIS', 'KENTUCKY-INDIANA', 'KENTUCKY-OHIO', 'KENTUCKY-TENNESSEE', 'KENTUCKY-VIRGINIA', 'LOUISIANA', 'LOUISIANA-TEXAS', 'MAINE', 'MARYLAND-WEST VIRGIN', 'MASSACHUSETTS-VERMON', 'MICHIGAN', 'MICHIGAN-WISCONSIN', 'MINNESOTA', 'MISSISSIPPI', 'MISSISSIPPI-ARKANSAS', 'MISSISSIPPI-TENNESSE', 'MISSOURI', 'MISSOURI-ILLINOIS', 'MONTANA', 'MONTANA-IDAHO', 'MONTANA-NORTH DAKOTA', 'MONTANA-SOUTH DAKOTA', 'MONTANA-WYOMING', 'NEBRASKA', 'NEBRASKA-COLORADO', 'NEVADA', 'NEVADA-CALIFORNIA', 'NEVADA-IDAHO', 'NEVADA-OREGON', 'NEVADA-UTAH']
# half2 = ['NEW HAMPSHIRE', 'NEW HAMPSHIRE-MAINE', 'NEW HAMPSHIRE-VERMON', 'NEW MEXICO', 'NEW MEXICO-ARIZONA', 'NEW MEXICO-COLORADO', 'NEW MEXICO-OKLAHOMA', 'NEW MEXICO-TEXAS', 'NEW YORK', 'NEW YORK-MASSACHUSET', 'NEW YORK-VERMONT', 'NORTH CAROLINA', 'NORTH CAROLINA-GEORG', 'NORTH CAROLINA-TENNE', 'NORTH CAROLINA-VIRGI', 'NORTH DAKOTA', 'NORTH DAKOTA-MONTANA', 'NORTH DAKOTA-SOUTH D', 'OHIO', 'OHIO-KENTUCKY', 'OHIO-WEST VIRGINIA', 'OKLAHOMA', 'OKLAHOMA-ARKANSAS', 'OKLAHOMA-COLORADO', 'OKLAHOMA-KANSAS', 'OKLAHOMA-NEW MEXICO', 'OKLAHOMA-TEXAS', 'OREGON', 'OREGON-CALIFORNIA', 'OREGON-IDAHO', 'OREGON-WASHINGTON', 'PENNSYLVANIA', 'PENNSYLVANIA-NEW YOR', 'SOUTH CAROLINA', 'SOUTH CAROLINA-GEORG', 'SOUTH DAKOTA', 'SOUTH DAKOTA-NORTH D', 'SOUTH DAKOTA-WYOMING', 'TENNESSEE', 'TENNESSEE-GEORGIA', 'TENNESSEE-KENTUCKY', 'TENNESSEE-NORTH CARO', 'TENNESSEE-VIRGINIA', 'TEXAS', 'TEXAS-LOUISIANA', 'TEXAS-NEW MEXICO', 'TEXAS-OKLAHOMA', 'UTAH', 'UTAH-COLORADO', 'UTAH-IDAHO', 'UTAH-NEVADA', 'UTAH-WYOMING', 'VERMONT', 'VIRGINIA', 'VIRGINIA-KENTUCKY', 'VIRGINIA-WEST VIRGIN', 'WASHINGTON', 'WASHINGTON-IDAHO', 'WASHINGTON-OREGON', 'WEST VIRGINIA', 'WEST VIRGINIA-MARYLA', 'WEST VIRGINIA-OHIO', 'WEST VIRGINIA-VIRGIN', 'WISCONSIN', 'WISCONSIN-MICHIGAN', 'WYOMING', 'WYOMING-COLORADO', 'WYOMING-IDAHO', 'WYOMING-MONTANA', 'WYOMING-NEBRASKA', 'WYOMING-SOUTH DAKOTA', 'YRTH CAROLINA-SOUTH ']
# directory = sorted(os.listdir(stateMapDirectory))
# list =[]
# lessThan150List = []
# for file in directory:
#     lessThan150List.append(file)
#
# print(lessThan150List)

import csv

masterDictionary = {}
dictionaryToAdd = {'key':'value'}
# Python code to merge dict using update() method
# def Merge(masterDictionary, dictionaryToAdd):
#     masterDictionary = masterDictionary.update(dictionaryToAdd)
#     return masterDictionary
#
# masterDictionary = Merge(masterDictionary, dictionaryToAdd)

masterDictionary = masterDictionary.update(dictionaryToAdd)
print(masterDictionary)