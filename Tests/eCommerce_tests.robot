*** Settings ***
Resource    ../Resources/Settings.resource

*** Test Cases ***
Update Profile Name
    [Documentation]    Test updating profile name on shopist.io
    Update Profile Name

Scrape Shopist Sofas
    [Documentation]    Scrape sofa names and prices on shopist.io
    Scrape Shopist Sofas    ${URL}    ${OUTPUT_FILE}
    ShopistKeywords.Close Browser