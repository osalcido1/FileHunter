from fiinder_1 import startSearch, search
from time import sleep

if __name__ == "__main__":
    startSearch()
    sleep(10)
    items = search('trademark')
    print('TOTAL LIST: ', items)
