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
    three_dots_button_xpath = "(//td[contains(@class,'MuiTableCell-root MuiTableCell-body')]//button)[1]"  # Botón de "tres puntos"
    add_licenses_option_xpath = "(//li[text()='Ver']/following-sibling::li)[2]"  # Opción "Agregar licencias"
    increase_quantity_button_xpath = "(//div[@class='MuiStack-root mui-bf78pe']//button)[2]"  # Botón "+"
    no_option_xpath = "(//span[contains(@class,'MuiButtonBase-root MuiRadio-root')])[2]"  # Botón "No"
    add_to_cart_button_xpath = "//button[contains(.,'Agregar al Carro')]"  # Botón "Agregar al carrito"
    continue_shopping_button_xpath = "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[2]"
    go_to_cart_button_xpath = "//a[contains(@class,'MuiButtonBase-root MuiIconButton-root')]"
    cart_button_xpath = "//a[contains(@href, '/cart')]"  # Botón para ir al carrito
    cart_product_names_xpath = "(//div[@class='MuiCardHeader-content mui-1aan0jy']//span)[1]"  # Nombres de productos en el carrito
    cart_product_prices_xpath = "//div[@class='MuiBox-root mui-jysr79']/following-sibling::p[1]"  # Precios de productos en el carrito
    cart_total_price_xpath = "//div[@class='MuiBox-root mui-u4ybgy']"  # Precio total en el carrito
