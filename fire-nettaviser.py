from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


def open_and_arrange_news_sites_as_strips(urls, refresh_interval=300):
    """
    Opens each URL in a Firefox window, arranges them as vertical strips side by side to fill the screen,
    and refreshes the pages at the specified interval.

    Args:
    - urls: A list of URLs to open.
    - refresh_interval: Time in seconds between each page refresh.
    """
    screen_width = 1920
    screen_height = 1080
    window_width = screen_width // 4
    window_height = screen_height

    options = Options()

    drivers = []
    for i, url in enumerate(urls):
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(window_width, window_height)
        driver.set_window_position(
            window_width * i, 0
        )  # Position windows next to each other horizontally
        driver.get(url)
        drivers.append(driver)

    try:
        while True:
            for driver in drivers:
                driver.refresh()
            time.sleep(refresh_interval)
    except KeyboardInterrupt:
        for driver in drivers:
            driver.quit()


urls = [
    "https://www.nrk.no",
    "https://www.adressa.no",
    "https://www.nidaros.no",
    "https://www.underdusken.no",
]

open_and_arrange_news_sites_as_strips(urls)
