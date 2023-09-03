# scrapping-99freelas

## Description
This repository contains a Python script designed to scrape projects related to "Automação Python" from the `99freelas.com.br` website. The fetched projects are stored in an Excel file, ensuring that no duplicate entries are added.

## Features
- Uses BeautifulSoup and Requests to efficiently scrape the 99freelas website.
- Stores scraped data in an Excel file (`projects.xlsx`).
- Avoids adding duplicate entries by checking existing data in the Excel file.
- Lightweight and easy to run.

## Prerequisites
Ensure you have the following installed:
- Python 3
- Virtual Environment (`venv`)

To install the required Python libraries, activate your virtual environment and run:
```bash
pip install -r requirements.txt
```

## Usage
Once you've activated your virtual environment and installed the prerequisites:
```bash
python scraper_99freelas.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
**Igor Medeiros**
- Email: igor.medeiros+github@gmail.com
- WhatsApp: +5511950016111

## License
This project is open source and available under the [MIT License](LICENSE).
