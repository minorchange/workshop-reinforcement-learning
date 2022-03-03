import numpy as np


class FlowerField():
    
    def __init__(self) -> None:
        self.n_flowers = 11
        self._initialize_flowers()

    def _initialize_flowers(self):
        self.means = np.arange(self.n_flowers).astype(np.float32)
        self.stds = np.ones(self.n_flowers) * 1

    def visit_flower_nr(self, n):
        mean = self.means[n]
        std = self.stds[n]
        amount_of_pollen = np.random.normal(mean, std, 1)[0]
        amount_of_pollen = np.clip(amount_of_pollen, a_min = 0, a_max=self.means.max() + 2)
        return amount_of_pollen