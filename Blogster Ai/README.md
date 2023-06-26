# Development

## Dependencies

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [Pymongo](https://pymongo.readthedocs.io/en/stable/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

## Installation

```bash
make install # Install dependencies
```

## Run

```bash
make run # Run the application (If not working, try `make run3`)
**Note:** If facing errors, do `make clean` and then `make run` [`make clean` removes the `__pycache__` files]
```

# Usage

## Endpoints

### POST /api/v1/scrape

Scrape a website and return the scraped data.
```Python
@app.route('/api/v1/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return 'URL is required', 400
```

#### Request

```bash
curl --location --request POST 'http://localhost:5000/api/v1/scrape' \
--form 'url="https://www.google.com"'
```

#### Response [Example]

```json
{
    "data": {
        "title": "Google",
        "description": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for.",
        "image": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"
    }
}
```

**Note:** For running the endpoints, it is recommended to use [Postman](https://www.postman.com/downloads/) or if not, you can use [cURL](https://curl.haxx.se/download.html) as shown above.