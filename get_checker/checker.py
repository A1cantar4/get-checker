import requests

def check_website(url: str, logger) -> None:
    # Check if a website is online and log the result.
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            logger.info(f"Site {url} is online!")
        else:
            logger.warning(f"Site {url} returned status code: {response.status_code}")
    except requests.ConnectionError:
        logger.error(f"Site {url} is offline (connection error).")
    except requests.Timeout:
        logger.error(f"Site {url} took too long to respond.")
    except Exception as exc:
        logger.exception(f"Unexpected error with {url}: {exc}")