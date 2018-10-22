import sys
import time

def main():
    interval = 3
    if len(sys.argv) > 1:
        interval = int(sys.argv[1])
    time.sleep(interval)

if __name__ == '__main__':
    main()
