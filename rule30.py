import logging
import time
import numpy as np
import cv2

logger = logging.getLogger()

class Rule30:

    def __init__(self, size, dry_runs = 0):
        self.size = size
        self.cells = np.full(size, False)
        self.cells[round(self.size / 2)] = True
        self.run(dry_runs)

    def run(self, count):
        for _ in range(count):
            self.tick()

    def tick(self):
        next_cells = np.empty(len(self.cells), dtype = bool)
        for i in range(len(self.cells)):
            if i - 1 >= 0:
                left = self.cells[i - 1]
            else:
                left = self.cells[len(self.cells) - 1]
            if i + 1 < len(self.cells):
                right = self.cells[i + 1]
            else:
                right = self.cells[0]
            center = self.cells[i]
            next_cells[i] = left ^ (center | right)
        self.cells = next_cells

    def create_image(self, height, img_name):
        start_time = time.perf_counter()
        img = np.empty((height, self.size))
        for i in range(height):
            f = lambda v: 0xFF if v else 0
            img[i, :] = np.array([f(e) for e in self.cells])
            self.tick()
            if i % int(height / 10) == 0:
                logger.info("Progress: {}%".format(round(100 * i / height)))
        cv2.imwrite(img_name, img)
        logger.info("Image generated in {:.2f}s".format(time.perf_counter() - start_time))

    def get_string(self, bits = None):
        m = { True: "1", False: "0" }
        if bits is None:
            return "".join(m[c] for c in self.cells)
        else:
            return "".join(m[c] for c in bits)
    def print_cells(self):
        print(self.get_string())



