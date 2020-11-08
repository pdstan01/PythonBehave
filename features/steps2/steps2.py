from selenium.webdriver.common.keys import Keys

@when('we visit "{url}"')
def step(context, url):
   context.browser.get(url)


@then('it should have a title "{title}"')
def step(context, title):
   assert context.browser.title == title


@given('we are on the home page')
def step(context):
    context.browser.get('https://redshelf.com/')


@when('we search for "{title}"')
def step(context, title):
    search_box = context.browser.find_element_by_id("search-catalog-home")
    search_box.clear()
    search_box.send_keys(title)
    search_box.send_keys(Keys.RETURN)


@then('"{text}" should be displayed')
def step(context, text):
    assert text in context.browser.page_source