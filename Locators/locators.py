class Locators():

    #Login page objects
    username_textbox_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[1]"
    password_textbox_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]"
    login_button_xpath = "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[1]"
    login_page_xpath = "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')]/following-sibling::a[1]"
    login_success_element_xpath = "//a[normalize-space(text())='Mi Cuenta']"

    #Search
    opcion_page_xpath ="//span[normalize-space(text())='Google']"

    # Search elements
    search_box_xpath = "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]"
    product_name_xpath = "//span[contains(@class,'MuiTypography-root MuiTypography-body1')]"
    product_price_xpath = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')])[3]"

    #Products to the cart
    three_dots_button_xpath = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')]//button)[1]"
    add_licenses_option_xpath = "(//li[text()='Ver']/following-sibling::li)[2]"
    increase_quantity_button_xpath = "(//div[@class='MuiStack-root mui-bf78pe']//button)[2]"
    no_option_xpath = "(//span[contains(@class,'MuiButtonBase-root MuiRadio-root')])[2]"
    add_to_cart_button_xpath = "//button[contains(.,'Agregar al Carro')]"
    continue_shopping_button_xpath = "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[2]"
    go_to_cart_button_xpath = "//a[contains(@class,'MuiButtonBase-root MuiIconButton-root')]"
    cart_button_xpath = "//a[contains(@href, '/cart')]"
    cart_product_names_xpath = "(//span[contains(@class,'MuiTypography-root MuiTypography-h6')])[1]"
    cart_product_prices_xpath = "(//p[contains(@class,'MuiTypography-root MuiTypography-body1')]//span)[1]"
    cart_product_names_two_xpath = "(//span[contains(@class,'MuiTypography-root MuiTypography-h6')])[2]"
    cart_product_prices_two_xpath = "(//p[contains(@class,'MuiTypography-root MuiTypography-body1')]//span)[2]"
    cart_total_price_xpath = "//div[@class='MuiBox-root mui-u4ybgy']"

    # Finish compra
    cart_button_xpath_two = "//a[contains(@class,'MuiButtonBase-root MuiIconButton-root')]"
    contact_dropdown_xpath = "//button[@aria-label='Open']"
    contact_option_xpath = "//input[@aria-activedescendant='autocomplete-contacts-option-0']"
    next_button_1_xpath = "//button[contains(.,'Siguiente')]"
    billing_dropdown_xpath = "(//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')])[3]"
    billing_option_fernando_xpath = "//input[@aria-activedescendant='autocomplete-legalEntity-option-0']"
