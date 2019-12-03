import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Skryabin_test(unittest.TestCase):

    def test_signup(self):
        browser: WebDriver = webdriver.Chrome(
            '/Users/igorkomarov/Desktop/python/Selenium/browsers/chromedriver')
        browser.get('http://skryabin.com/webdriver/html/sample.html')

        # Name:
        browser.find_element_by_id('name').click()
        browser.find_element_by_xpath('//*[@id="firstName"]').send_keys('F-test')
        browser.find_element_by_xpath('//*[@id="middleName"]').send_keys('M-test')
        browser.find_element_by_xpath('//*[@id="lastName"]').send_keys('L-test')
        browser.find_element_by_xpath(
            '//*[@class="ui-button-text"][contains(text(),"Save")]').click()

        # Country droplist:
        browser.find_element_by_css_selector(
            'select[ng-model="formData.countryOfOrigin"]').click()
        browser.find_element_by_css_selector('option[value="USA"]').click()

        # Address textarea:
        browser.find_element_by_id('address').send_keys('12345 BadCupertino 13')

        # 3rd Party message:
        element = browser.find_element_by_id('thirdPartyButton')
        element.location_once_scrolled_into_view
        element.click()
        browser.switch_to.alert.accept()
        result_value = browser.find_element_by_xpath(
            '//*[@id="thirdPartyResponseMessage"]').get_attribute('innerHTML')
        test_value = 'You accepted third party agreement.'
        self.assertEqual(test_value, result_value)

        # Checkbox Private Policy:
        element = browser.find_element_by_css_selector('input[name="agreedToPrivacyPolicy"]')
        element.location_once_scrolled_into_view
        element.click()

        # Username:
        element = browser.find_element_by_name('username')
        element.location_once_scrolled_into_view
        element.send_keys('TestUser')

        # Email:
        browser.find_element_by_name('email').send_keys('abc@gmail.com')

        # Password:
        browser.find_element_by_id('password').send_keys('test_password123')
        browser.find_element_by_id('confirmPassword').send_keys('test_password123')

        # Phone Number:
        browser.find_element_by_css_selector(
            'input[name="phone"]').send_keys('6501234567')

        # Radio Button Male-Female:
        browser.find_element_by_xpath('//input[@name="gender"][@value="male"]').click()
        browser.find_element_by_xpath('//input[@name="gender"][@value="female"]').click()

        # Checkbox Allowed to contact:
        js = 'scroll(0, 350);'
        browser.execute_script(js)
        browser.find_element_by_xpath('//input[@name="allowedToContact"][@type="checkbox"]').click()

        # Birthday:
        browser.find_element_by_id('dateOfBirth').click()
        browser.find_element_by_css_selector('.ui-datepicker-year').click()
        browser.find_element_by_css_selector('option[value="1971"]').click()
        browser.find_element_by_css_selector('.ui-datepicker-month').click()
        browser.find_element_by_css_selector('option[value="2"]').click()
        browser.find_element_by_css_selector('.ui-state-default')
        browser.find_element_by_link_text('28').click()

        # Car Make listbox:
        browser.find_element_by_css_selector('option[value="Ford"]').click()
        browser.find_element_by_css_selector('option[value="BMW"]').click()

        # Additional Information:
        browser.switch_to.frame('additionalInfo')
        browser.find_element_by_id('contactPersonName').send_keys('Tester Name')
        browser.find_element_by_id('contactPersonPhone').send_keys('6507654321')
        browser.switch_to.parent_frame()

        # Button Related documents:
        main_window = browser.current_window_handle
        browser.find_element_by_xpath(
            '//*[@type="button"][contains(text(),"Related documents")]').click()
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        result_value = browser.find_element_by_css_selector('h4').get_attribute('innerHTML')
        test_value = 'Documents List:'
        self.assertEqual(test_value, result_value)
        browser.switch_to.window(main_window)

        # Button Attach file:
        element = browser.find_element_by_xpath('//input[@id="attachment"]')
        element.location_once_scrolled_into_view
        element.send_keys(os.path.abspath('/Users/igorkomarov/Downloads/testfile.txt'))

        # Button Submit:
        browser.find_element_by_css_selector('button[id="formSubmit"]').click()

        # Check all values:
        result_values = []
        browser.switch_to.active_element
        test_values = ['F-test', 'M-test', 'L-test', 'F-test M-test L-test', 'USA', '12345 BadCupertino 13',
                       'true', 'TestUser', 'abc@gmail.com', '[entered]', '6501234567', 'female', '03/28/1971',
                       'true', 'Ford, BMW', 'Tester Name', '6507654321', 'accepted', 'testfile.txt']
        result_values.append(browser.find_element_by_name('firstName').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('middleName').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('lastName').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('name').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('countryOfOrigin').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('address').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('agreedToPrivacyPolicy').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('username').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('email').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('password').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('phone').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('gender').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('dateOfBirth').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('allowedToContact').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('carMake').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('contactPersonName').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('contactPersonPhone').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('thirdPartyAgreement').get_attribute('innerHTML'))
        result_values.append(browser.find_element_by_name('attachmentName').get_attribute('innerHTML'))
        self.assertEqual(test_values, result_values)
        browser.quit()


if __name__ == '__main__':
    unittest.main()
