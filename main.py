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
    HEIGHT = 128
    WIDTH = 128
    SIZE = 64
    r = rule30.Rule30(SIZE, 1000)
    logger.info("Automata size: " + str(r.get_size()))
    r.create_image(HEIGHT, WIDTH, IMG_NAME)
