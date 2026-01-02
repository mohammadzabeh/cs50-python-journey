# =========================
# APIs
# =========================
# API (Application Programming Interface):
# An API allows one program to communicate with another program or service
# over the internet using structured requests and responses.
# In this file, we use a public music API to search for songs by artist name.


# =========================
# Requests
# =========================
# requests is a popular third-party Python library used to send HTTP requests.
# It allows us to easily communicate with web APIs using GET, POST, etc.
# It is NOT part of the Python standard library.
#
# Installation (once):
# pip install requests
#
# If pip is not recognized on Windows, use:
# python -m pip install requests


# =========================
# JSON
# =========================
# JSON (JavaScript Object Notation):
# A lightweight text format used to exchange structured data.
# APIs usually return data in JSON format.
#
# In Python:
# - json.dumps() → converts Python data → JSON string
# - json.loads() → converts JSON string → Python data
#
# IMPORTANT:
# json.dump() is used to write JSON to a FILE
# json.dumps() is used to print or format JSON as a STRING


# =========================
# HTTP methods
# =========================
# requests.get():
# Sends an HTTP GET request to a URL.
# Used to retrieve data from an API (read-only operation).


import json
import requests
import sys


# =========================
# Version 1 — basic API request
# =========================
def v1():
    # Ensure exactly one command-line argument is provided
    # sys.argv is a list of command-line arguments
    # sys.argv[0] → script name
    # sys.argv[1] → artist or band name provided by the user
    if len(sys.argv) != 2:
        sys.exit("Usage: python file.py <artist_or_band_name>")

    # sys.argv[1] contains the band or singer name typed in the terminal
    # We are making a simple command-line search using the Deezer API
    #
    # URL explanation:
    # https://api.deezer.com/search?q=
    # q → query string (artist name)
    response = requests.get(
        "https://api.deezer.com/search?q=" + sys.argv[1] + "&limit=1"
    )

    # response.json():
    # Converts the HTTP response body (JSON text)
    # into a Python dictionary
    print(response.json())


# =========================
# Version 2 — formatted JSON output
# =========================
def v2():
    if len(sys.argv) != 2:
        sys.exit("Usage: python file.py <artist_or_band_name>")

    response = requests.get(
        "https://api.deezer.com/search?q=" + sys.argv[1] + "&limit=1"
    )

    # json.dumps():
    # Converts Python data into a nicely formatted JSON string
    #
    # indent=2:
    # Adds indentation for readability
    #
    # NOTE:
    # json.dump() writes to a file
    # json.dumps() returns a string (what we want here)
    print(json.dumps(response.json(), indent=2))


# =========================
# Version 3 — extracting useful data
# =========================
def v3():
    if len(sys.argv) != 2:
        sys.exit("Usage: python file.py <artist_or_band_name>")

    # This request retrieves multiple results instead of just one
    response = requests.get(
        "https://api.deezer.com/search?q=" + sys.argv[1] + "&limit=1"
    )

    # Convert the JSON response into a Python dictionary
    o = response.json()

    # The Deezer API returns a dictionary with a key called "data"
    # "data" is a list of song objects
    for result in o["data"]:
        # Each result contains metadata about a track
        # title → song name
        print(result["title"])


# Run version 3 by default
v3()
