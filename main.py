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

    SCREEN_SIZE = (1024, 768)
    AUTOMATA_SIZE = SCREEN_SIZE[0]
    DELAY = 10
    CHANGE_INTERVAL = 0
    auto = automata.Automata(160, AUTOMATA_SIZE)
    visu = visual.Visualizer(auto, SCREEN_SIZE, DELAY, CHANGE_INTERVAL)
    visu.loop()

