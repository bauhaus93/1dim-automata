import logging
import time
import random
import numpy as np
import cv2

logger = logging.getLogger()

def rule(number, value):
    return (number >> value) & 1

class Automata:

    def __init__(self, rule_number, size, allow_odd_rule = False):
        self.rule_number = rule_number
        self.size = size
        self.allow_odd_rule = allow_odd_rule
        self.set_state_one_true()

    def randomize_rule(self):
        self.rule_number = random.randint(0, 0xFF)
        if not self.allow_odd_rule and self.rule_number % 2 == 1:
            self.rule_number = (self.rule_number + 1) % 256

    def randomize_state(self):
        self.cells = np.random.choice([0, 1], size = self.size)
    
    def set_state_one_true(self):
        self.cells = np.full(self.size, 0)
        self.cells[round(self.size / 2)] = 1

    def is_zero(self):
        return not np.any(self.cells)
    
    def is_one(self):
        return np.all(self.cells)

    def run(self, count):
        for _ in range(count):
            self.tick()

    def tick(self):
        next_cells = np.empty_like(self.cells)
        for i in range(len(self.cells)):
            v = 4 * self.cells[(i - 1) % self.size]
            v |= 2 * self.cells[i]
            v |= self.cells[(i + 1) % self.size]
            next_cells[i] = rule(self.rule_number, v)
        self.cells = next_cells
   
    def get_string(self, bits = None):
        return "".join(str(c) for c in self.cells)

    def print_cells(self):
        print(self.get_string())



