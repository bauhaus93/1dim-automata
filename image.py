import logging
import time

import numpy as np
import cv2

logger = logging.getLogger()

def create_image(automata, height, img_name):
    start_time = time.perf_counter()
    img = np.empty((height, automata.size))
    f = lambda e: 0xFF if e else 0
    for i in range(height):
        img[i, :] = np.array([f(e) for e in automata.cells])
        automata.tick()
        if i % int(height / 10) == 0:
            logger.info("Progress: {}%".format(round(100 * i / height)))
    cv2.imwrite(img_name, img)
    logger.info("Image generated in {:.2f}s".format(time.perf_counter() - start_time))