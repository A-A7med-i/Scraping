import requests
from bs4 import BeautifulSoup
import numpy as np
import csv
import os


def scrape(base_url, num_page=2):
    """Scrapes book information from Z-Library for a given number of pages.

    Args:
        base_url (str): The base URL for Z-Library search results.
        num_pages (int, optional): The number of pages to scrape (defaults to 2).

    Returns:
        list: A list containing scraped book information.
    """

    titles_list = []
    authors_list = []
    publishers_list = []
    years_list = []
    languages_list = []
    files_type_list = []
    rate_list = []
    data_book = []

    for i in range(num_page):

        url = f"{base_url}&page={i}"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "lxml")

        divs = soup.find_all("div", class_="resItemBox resItemBoxBooks exactMatch")

        years = soup.find_all("div", class_="bookProperty property_year")

        files_type = soup.find_all("div", class_="bookProperty property__file")

        for div in divs:
            title = div.find("h3", itemprop="name")
            titles_list.append(title.text.strip())

            author = div.find("div", class_="authors")
            authors_list.append(author.text.strip())

            publisher = div.find("a", itemprop="publisher")
            if publisher:
                publishers_list.append(publisher.text.strip())
            else:
                publishers_list.append(np.nan)

            language = div.find("div", class_="property_value text-capitalize")
            languages_list.append(language.text.strip())

            rate = div.find("span", class_="book-rating-interest-score")
            rate_list.append(rate.text.strip())

        for year in years:
            if year.find("div", class_="property_label").text == "Year:":
                years_list.append(
                    year.find("div", class_="property_value").text.strip()
                )

        for file_type in files_type:
            files_type_list.append(
                file_type.find("div", class_="property_value").text.strip()
            )

    for title, author, publisher, year, language, file_type, rate in zip(
        titles_list,
        authors_list,
        publishers_list,
        years_list,
        languages_list,
        files_type_list,
        rate_list,
    ):
        data_book.append((title, author, publisher, year, language, file_type, rate))

    return data_book


def write_book_info_to_csv(data):
    """Writes scraped book information to a CSV file.

    Args:
        data (list): A list of dictionaries containing book information.
        filename (str, optional): The filename for the CSV file (defaults to "book_info.csv").
    """
    folder = "Data"
    file_name = os.path.join(folder, "book_info.csv")

    with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            [
                "Title",
                "Author(s)",
                "Publisher",
                "Year",
                "Language",
                "File Type",
                "Rating",
            ]
        )
        csv_writer.writerows(data)


def main():
    """Main function to scrape book information and write it to CSV."""

    base_url = "https://zlib-official.com/s/Computer%20Science?q=Computer%20Science"
    book_data = scrape(base_url)
    write_book_info_to_csv(book_data)


if __name__ == "__main__":
    main()
