import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
file_path = "benchmark_results.csv"
df = pd.read_csv(file_path, header=None, names=["algorithm", "size", "time"])

# Liczba unikalnych rozmiarów zbiorów danych
unique_sizes = df["size"].unique()
num_sizes = len(unique_sizes)

# Lista unikalnych algorytmów
unique_algorithms = df["algorithm"].unique()

# Podział na 5 kategorii (co 78 wierszy)
num_rows_per_category = 78
categories = ["random_array", "ascending", "descending", "constant", "a_shaped"]
data_categories = {category: df.iloc[i * num_rows_per_category:(i + 1) * num_rows_per_category] for i, category in enumerate(categories)}

# Tworzenie wykresów dla każdej kategorii
plt.figure(figsize=(15, 10))
for i, (category, data) in enumerate(data_categories.items(), 1):
    plt.subplot(3, 2, i)
    for algo in unique_algorithms:
        subset = data[data["algorithm"] == algo]
        plt.plot(subset["size"], subset["time"], marker='o', linestyle='-', label=algo)
    
    plt.title(f"{category}")
    plt.xlabel("Rozmiar tablicy")
    plt.ylabel("Czas wykonania (s)")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
