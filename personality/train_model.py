import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import joblib

print("=" * 40)
print("ОБУЧАЮ МОДЕЛЬ")
print("=" * 40)

df = pd.read_csv('personality_synthetic_dataset.csv')
print(f"Загружено {len(df)} человек")

X = df[['social_energy', 'alone_time_preference', 'talkativeness']]
print(f"Использую признаки: social_energy, alone_time_preference, talkativeness")

print("Обучаю K-Means...")
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

joblib.dump(kmeans, 'kmeans_model.pkl')
print("Модель сохранена в файл 'kmeans_model.pkl'")

df['cluster'] = kmeans.labels_
print("Кластеры добавлены!")

plt.figure(figsize=(10, 6))
colors = ['red', 'green', 'blue']

for i in range(3):
    cluster_data = df[df['cluster'] == i]
    plt.scatter(cluster_data['social_energy'],
               cluster_data['talkativeness'],
               c=colors[i],
               label=f'Кластер {i}',
               alpha=0.6)

plt.xlabel("Социальная энергия", fontsize=12)
plt.ylabel("Разговорчивость", fontsize=12)
plt.title("Кластеры личностей (K-Means)", fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("clusters.png", dpi=100)
plt.show()

print("\nГрафик сохранён как 'clusters.png'")
print("=" * 40)
print("ГОТОВО! Теперь запусти predict.py")
print("=" * 40)