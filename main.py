#!/bin/env python
import logging

import automata
import image
import visual

def setup_logger():
    FORMAT = r"[%(asctime)-15s] %(levelname)s - %(message)s"
    DATE_FORMAT = r"%Y-%m-%d %H:%M:%S"
    logging.basicConfig(level = logging.DEBUG, format = FORMAT, datefmt = DATE_FORMAT)

#cool rules: 30, 90, 22, 160

if __name__ == "__main__":
    logger = logging.getLogger()
    setup_logger()

    SCREEN_SIZE = (1600, 900)
    AUTOMATA_SIZE = SCREEN_SIZE[0]
    DELAY = 10
    CHANGE_INTERVAL = 200
    auto = automata.Automata(30, AUTOMATA_SIZE)
    visu = visual.Visualizer(auto, SCREEN_SIZE, DELAY, CHANGE_INTERVAL)
    visu.loop()

