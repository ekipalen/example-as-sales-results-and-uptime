"""
AI Action for submitting sales results to company's internal application. 
"""

import time

from robocorp import browser
from robocorp.actions import action


@action
def submit_sales_results(
    firstname: str, lastname: str, salestarget: str, salesresult: str
) -> str:
    """
    Submit sales results to company's internal application.

    Sales target needs to have increments of 5000 between 5-100k.

    Args:
        firstname (str): Sales persons first name in string format. Example: "Jill"
        lastname (str): Sales persons last name in string format. Example: "Jones"
        salestarget (str): Sales target between 5000 and 100000 in increments of 5000, in string format. Example "40000"
        salesresult (str): Sales result in string format. Example "35000"

    Returns:
        str: Result of the automation task, either "Success" or an error message.
    """

    try:
        browser.configure(
            browser_engine="chromium",
            screenshot="only-on-failure",
            headless=False,
        )
        page = browser.goto("https://robotsparebinindustries.com/")
        page.set_default_timeout(4000)
        page.fill("#username", "maria")
        page.fill("#password", "thoushallnotpass")
        page.click("button:text('Log in')")

        page.fill("#firstname", firstname)
        page.fill("#lastname", lastname)
        page.fill("#salesresult", salesresult)
        page.select_option("#salestarget", salestarget)
        page.click("text=Submit")
        time.sleep(5)
        return "Success"
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Looks like the target didn't meet the requirements?"
