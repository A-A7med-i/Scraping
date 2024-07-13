# Z-Library Python Scraper

[Z-Library](https://zlib-official.com/)

## Overview

This Python project provides a web scraper for Z-Library, the world's largest collection of free ebooks and articles. The goal is to make it easier to integrate Z-Library content into other applications.

## Features

- Fetch ebook and article data from Z-Library.
- Search for specific titles, authors, or topics.
- Retrieve download URLs for ebooks and articles.

## Customization Options

### Search URL

By default, the scraper targets Z-Library (z-lib.org) for ebook and article data. However, you can easily customize the search URL to focus on specific categories, genres, or topics. Modify the `BASE_URL` variable in your script to point to the desired search page.

### Number of Pages

The scraper retrieves data from multiple pages of search results. You can adjust the number of pages to scrape by changing the `MAX_PAGES` constant. Keep in mind that scraping too many pages too quickly may trigger rate limits or IP blocks, so use this option judiciously.

## Running the Script

1. Ensure you've installed the required libraries (requests, BeautifulSoup, and Selenium).
2. Customize the search URL and set the desired number of pages.
3. Run the scraping script:
```bash
python script.py
```
(Replace `scrape.py` with the actual filename of your script)