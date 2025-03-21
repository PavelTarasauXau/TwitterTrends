

import json
import matplotlib.pyplot as plt

class State:
    def __init__(self, name, regions):
        self.name = name
        self.regions = regions

    def plot(self, ax):
        """Рисует границы штата на переданной оси."""
        for region in self.regions:
            for polygon in region:
                if isinstance(polygon[0], list):  # Проверяем, является ли первый элемент списком координат
                    lons, lats = zip(*polygon)
                    ax.plot(lons, lats, label=self.name)
                else:
                    print(f"Ошибка в данных штата {self.name}: {polygon}")

class StatePlotter:
    def __init__(self, json_file):
        self.json_file = json_file
        self.states = self.load_states()

    def load_states(self):
        """Загружает JSON-файл и создает объекты State."""
        with open(self.json_file, "r") as file:
            states_data = json.load(file)
        return [State(name, regions) for name, regions in states_data.items()]

    def plot_states(self):
        """Рисует границы всех штатов на графике."""
        fig, ax = plt.subplots(figsize=(10, 8))

        for state in self.states:
            state.plot(ax)

        ax.set_title("Границы штатов")
        ax.set_xlabel("Долгота")
        ax.set_ylabel("Широта")
        ax.legend()
        ax.grid(True)
        plt.show()

# Использование классов
if __name__ == "__main__":
    plotter = StatePlotter("states.json")
    plotter.plot_states()
