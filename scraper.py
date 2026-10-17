#!/usr/bin/env python3
"""
Product Price Scraper
Scrapes product name, price, rating and availability from a paginated
catalogue and exports the result to CSV, JSON and Excel.

Demo target: https://books.toscrape.com (a sandbox site made for practice).
To adapt it to a client's site, only parse_product() and the CSS selectors
need to change.

Usage:
    python scraper.py --max-pages 5 --out books
"""
import argparse
import csv
import json
import logging
import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; PriceScraper/1.0)"}
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

log = logging.getLogger("scraper")


def fetch(session, url, retries=3, delay=2.0):
    """GET a page with simple retry/backoff. Returns HTML text or None.""
