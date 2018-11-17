#!/bin/env python
import logging

import rule30

def setup_logger():
    FORMAT = r"[%(asctime)-15s] %(levelname)s - %(message)s"
    DATE_FORMAT = r"%Y-%m-%d %H:%M:%S"
    logging.basicConfig(level = logging.DEBUG, format = FORMAT, datefmt = DATE_FORMAT)

if __name__ == "__main__":
    logger = logging.getLogger()
    setup_logger()
    IMG_NAME = "img.png"
    HEIGHT = 4096
    SIZE = 8192
    r = rule30.Rule30(SIZE, 0)
    r.create_image(SIZE, IMG_NAME)
