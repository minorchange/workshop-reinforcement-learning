import pandas as pd
import numpy as np
import random


class Bumblebee():
    def __init__(self) -> None:
        self.n_flowers = 11
        self.exploration_fraction = 0.1
        self.__initialize_memory()
        
    def __initialize_memory(self):
        initial_preference = np.random.uniform(low=0.0, high=0.0000000001, size=self.n_flowers)
        initial_n_times_visited = np.zeros(self.n_flowers)
        data = np.transpose([initial_preference, initial_n_times_visited])
        self.memory_df = pd.DataFrame(data, columns = ["preference", "n_times_visited"])

    def update_memory(self, flower_id, amount_of_pollen):
        row = self.memory_df.iloc[flower_id]
        new_n_times_visited = row["n_times_visited"] + 1
        total_amount_of_pollen_from_this_flower = row["preference"]* row["n_times_visited"] + amount_of_pollen * 1
        new_preference = total_amount_of_pollen_from_this_flower / new_n_times_visited
        row["preference"] = new_preference
        row["n_times_visited"] =new_n_times_visited

    def _explore(self):
        random_flower_id = random.choice(self.memory_df.index)
        return random_flower_id

    def _exploit(self):
        most_prommising_flower_id = self.memory_df.idxmax(axis=0)["preference"]
        return most_prommising_flower_id

    def choose_flower(self):
        feel_lucky = random.uniform(0,1) <= self.exploration_fraction
        if feel_lucky:
            flower_id = self._explore()
        else:
            flower_id = self._exploit()
        return flower_id