*** Settings ***
Library           OperatingSystem
Library           CSVLibrary
Library           SeleniumLibrary
Library           Browser
Library           ../Library/csv_reader.py
Library           ../Library/ShopistKeywords.py
Library           ../Library/EmailNotificationLibrary.py

Resource    Variables.resource
Resource    eCommerce_keywords.resource