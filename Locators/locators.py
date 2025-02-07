class Locators():

    #Login page objects
    username_textbox_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[1]"
    password_textbox_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]"
    login_button_xpath = "(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[1]"
    login_page_xpath = "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')]/following-sibling::a[1]"

    #Search
    opcion_page_xpath ="//span[normalize-space(text())='Google']"

    #Product
    opcion_product_xpath ="//a[normalize-space(text())='Comprar']"
    opcion_buy_xpath ="(//button[contains(@class,'MuiButtonBase-root MuiButton-root')])[2]"