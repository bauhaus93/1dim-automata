import logging
import time
import numpy as np
import cv2

logger = logging.getLogger()

class Rule30:

    def __init__(self, size, dry_runs = 0):
        size += 24 - size % 24
        self.cells = np.full(size, False)
        self.cells[0] = True
        self.run(dry_runs)

    def get_size(self):
        return self.cells.shape[0]

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

    def get_number(self):
        self.tick()
        return int(self.get_string(), 2)

    def get_numbers(self, count):
        for c in range(count):
            yield self.get_number()

    def create_line(self):
        data = self.cells.reshape((-1, 8))
        img = np.empty(len(data), dtype = np.uint8)
        for i, bits in enumerate(data):
            img[i] = int(self.get_string(bits), 2)
        return img.reshape((1, -1, 3))

    def create_fixed_line(self, width):
        line = self.create_line()
        full_line = None
        for l in range(0, width, line.shape[1]):
            self.tick()
            if full_line is None:
                full_line = line
            else:
                full_line = np.append(full_line, line, axis = 1)
            line = self.create_line()
        return full_line[:, :width]

    def create_image(self, width, height, img_name):
        start_time = time.perf_counter()
        logger.info("Creating image of size {}x{}".format(width, height))
        img = np.empty((height, width, 3))
        for i in range(height):
            line = self.create_fixed_line(width)
            img[i, :] = line
            self.tick()
            if i % int(width / 10) == 0:
                logger.info("Progress: {:.2f}%".format(100 * i / width))
        cv2.imwrite(img_name, img)
        logger.info("Created image in {:.2f}s".format(time.perf_counter() - start_time))

    def get_string(self, bits = None):
        m = { True: "1", False: "0" }
        if bits is None:
            return "".join(m[c] for c in self.cells)
        else:
            return "".join(m[c] for c in bits)
    def print_cells(self):
        print(self.get_string())



