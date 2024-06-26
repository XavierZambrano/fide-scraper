# FIDE Scraper
[FIDE Top 100 players](https://ratings.fide.com/) scraper

## Installation

### Setup
1. Clone the repository 
```
git clone https://github.com/XavierZambrano/fide-scraper.git
```
2. Create a virtual environment and activate it
3. Install the requirements
```bash
pip install -r requirements.txt
```

## Usage
```
scrapy crawl top_players -O results.csv
```
For more information about scrapy crawl arguments, check the [Scrapy documentation](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl).

Example result: [results.csv](assets/results.csv)