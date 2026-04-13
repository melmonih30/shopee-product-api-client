# Shopee Product Detail API Client

This project demonstrates how to retrieve Shopee product data using an asynchronous API workflow.

## Overview

The Shopee Product Detail Task API works in three steps:

1. Submit a product detail request
2. Poll the API until processing is complete
3. Retrieve the raw product data

## Features

- Submit product detail tasks
- Poll task status automatically
- Retrieve raw Shopee product data
- Clean and simple Python implementation

## Tech Stack

- Python
- Requests library
- REST API

## How to Use

1. Add your API credentials:

```python
TOKEN = "YOUR_API_TOKEN"
SECRET = "YOUR_API_SECRET"
