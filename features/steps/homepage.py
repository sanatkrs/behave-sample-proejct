from behave import *

from Logger.LogGen import LogGen
from Pages.HomePage import Homepage
from Config.readProperties import ReadConfig

logger = LogGen.loggen()


@given(u'user input wrong email id "{login_id}" and password "{password}"')
def step_impl(context, login_id, password):
    Homepage(context.driver).open_page(ReadConfig.getWebUrl())
    Homepage(context.driver).enter_username(login_id)
    Homepage(context.driver).enter_password(password)
    # status = False
    # try:
    #     SeleniumHelper(context.driver).open_page(test_data.facebook_login_url)
    #     # SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_login, login_id)
    #     # SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_password, password)
    #     SeleniumHelper(context.driver).click(locators.button_login)
    #     status = True
    # except Exception as e:
    #     LogGen.LogGen.loggen().error(f"Exception occurred: {e}")
    # assert status is True

# @when('check the homepage')
# def step_impl(context):
#     print("Checked the header of the homepage")
#
# @then('header menu items should be present')
# def step_impl(context):
#     print("Menu items are present")
#     assert 3==3;

@when(u'check the homepage')
def step_impl(context):
    logger.info(f"Reached into when step")


@then(u'check the homepage title')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then check the homepage title')


@then(u'header menu items should be present')
def step_impl(context):
    logger.info(f"Reached into then step")

