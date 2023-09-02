"""
Web Scraper for 99freelas.com.br
-----------------------------------------
Author: Igor Medeiros
Email: igor.medeiros@gmail.com
WhatsApp: +5511950016111
GitHub: [Your GitHub URL here, if you have one]
Date: [Current date, e.g., '01/09/2023']

Description:
This script fetches projects related to 'Automação Python' from 99freelas.com.br
and stores them in an Excel file. It ensures no duplicate entries are added.

Prerequisites:
- Python 3
- Requests
- BeautifulSoup
- pandas

Usage:
$ python scraper_99freelas.py
"""

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Constants
URL_BASE = 'https://www.99freelas.com.br'
SEARCH_QUERY = 'Automação Python'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def fetch_projects():
    """
    Fetch the projects from 99freelas using the search query.

    Returns:
    List of projects with each project being a list of [title, link, description, proposals]
    """
    url = f'{URL_BASE}/projects?q={SEARCH_QUERY}'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    result_list = soup.find('ul', class_='result-list')

    projects = []

    for item in result_list.find_all('li', class_='result-item'):
        title = item.find('h1', class_='title').a.text.strip()
        link = URL_BASE + item.find('h1', class_='title').a['href']
        proposals_text = item.find('p', class_='item-text information').text
        start_index = proposals_text.find('Propostas:') + 10
        end_index = proposals_text.find('|', start_index)

        proposals_description = item.find(
            'div', class_='item-text description formatted-text').text.strip()
        proposals = int(proposals_text[start_index:end_index].strip())
        projects.append([title, link, proposals_description, proposals])

    return projects


def main():
    projects = fetch_projects()

    existing_links = set()
    initial_rows = 0  # Initial number of rows in the Excel file

    if os.path.exists('projects.xlsx'):
        df_old = pd.read_excel('projects.xlsx')
        existing_links = set(df_old['Link'])
        initial_rows = len(df_old)

    # Filtering out the projects already in the Excel file
    projects = [proj for proj in projects if proj[1] not in existing_links]

    if os.path.exists('projects.xlsx'):
        df_new = pd.DataFrame(
            projects, columns=['Title', 'Link', 'Description', 'Proposals'])
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = pd.DataFrame(projects, columns=[
                          'Title', 'Link', 'Description', 'Proposals'])

    df.to_excel('projects.xlsx', index=False)

    added_rows = len(df) - initial_rows
    if added_rows == 0:
        print("No rows were added.")
    else:
        print(f"{added_rows} rows were added.")


if __name__ == "__main__":
    main()
