#!/bin/python3
# confluence.py
# A python script for finding all of the pdfs on a webpage and combining
# them. The motivation for this is was the webpage for simply scheme,
# which had all of the individual chapter pdfs for the book, but did not
# have a complete pdf of the book, which I wanted to be able to download
# to my tablet.

from bs4 import BeautifulSoup
import requests

