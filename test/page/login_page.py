from utils.verifyCode import verifyCode


def login(driver, username, password):
    old_url = driver.current_url()
    while True:
        driver.clear('id', 'shortAccount')
        driver.input('id', 'shortAccount', username)
        driver.clear('id', 'password')
        driver.input('id', 'password', password)
        code = verifyCode(driver, 'id', 'imgcode')
        driver.input('id', 'code0', code)
        driver.click('css', '[value="登 录"]')
        new_url = driver.current_url()
        if old_url != new_url:
            break
        else:
            driver.refresh()











