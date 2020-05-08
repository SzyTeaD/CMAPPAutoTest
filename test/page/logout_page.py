import time

class Logout():
    def logout(self,driver):
        old_url = driver.current_url()
        while True:
            driver.move_to('id', 'commission')
            driver.click('class', 'logout_icon')
            time.sleep(1)
            driver.click('xpath', '//*[@id="cancellation"]')
            new_url = driver.current_url()
            if old_url != new_url:
                break
            else:
                driver.refresh()

