*** Settings ***
Library    CSVLibrary

*** Keywords ***
Read CSV File
    [Arguments]    ${file_path}
    ${data}=    Read CSV    ${file_path}
    RETURN    ${data}


Update Profile Name
    [Documentation]    Test updating profile name on shopist.io
    [Tags]    ECommerce
    ${names}=    Read CSV File        Data/names.csv
    ${first_name}=    Set Variable    ${names[0][0]}
    ${second_name}=    Set Variable    ${names[0][1]}
    Browser.Open Browser    ${URL}   browser=chromium    headless=False    pause_on_failure=True
    Browser.Click    ${MY_PROFILE_BUTTON_SELECTOR}
    Browser.Click    ${EDIT_PROFILE_BUTTON_SELECTOR}
    Browser.Fill Text    ${FIRST_NAME_SELECTOR}    ${first_name}
    Browser.Fill Text    ${SECOND_NAME_SELECTOR}    ${second_name}
    Browser.Click    ${SAVE_PROFILE_BUTTON_SELECTOR}
    Browser.Close Browser

Create Shopist Keywords
    RETURN      ShopistKeywords