from checker import check_website
from logger import setup_logger
import time

def main():
    logger = setup_logger()
    url = input("Paste here the link: ").strip()
    interval = 6

    while True: # Press 'CTRL + C' to break the loop
        check_website(url, logger)
        time.sleep(interval)
        
if __name__ == "__main__":
    main()