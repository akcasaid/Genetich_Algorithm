import random

# Genetik algoritma parametreleri
POPULATION_SIZE = 10  # Popülasyon büyüklüğü
GENOME_LENGTH = 8  # Her bireyin gen uzunluğu
MUTATION_RATE = 0.01  # Mutasyon oranı
GENERATIONS = 100  # Maksimum nesil sayısı

def create_individual():
    """Rastgele bir birey oluştur."""
    return [random.randint(0, 1) for _ in range(GENOME_LENGTH)]

def create_population():
    """Rastgele bir popülasyon oluştur."""
    return [create_individual() for _ in range(POPULATION_SIZE)]

def fitness(individual):
    """Bir bireyin uygunluk değerini hesapla. (Burada, sadece bitlerin toplamı)"""
    return sum(individual)

def selection(population):
    """Rulet tekerleği yöntemi ile seçim."""
    total_fitness = sum(fitness(individual) for individual in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual in population:
        current += fitness(individual)
        if current > pick:
            return individual

def crossover(parent1, parent2):
    """İki ebeveyn arasında çaprazlama yaparak yeni bireyler oluştur."""
    point = random.randint(1, GENOME_LENGTH - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    """Bireyde mutasyon yap."""
    for i in range(GENOME_LENGTH):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 if individual[i] == 0 else 0

def genetic_algorithm():
    """Genetik algoritmayı çalıştır."""
    population = create_population()
    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = selection(population)
            parent2 = selection(population)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            mutate(offspring1)
            mutate(offspring2)
            new_population.extend([offspring1, offspring2])
        population = new_population

        # En iyi bireyi bul ve uygunluk değerini yazdır
        best_individual = max(population, key=fitness)
        print(f"Nesil {generation + 1}: En iyi uygunluk = {fitness(best_individual)}")

    # En iyi bireyi döndür
    best_individual = max(population, key=fitness)
    return best_individual

# Genetik algoritmayı çalıştır ve sonucu yazdır
best = genetic_algorithm()
print("En iyi birey:", best)
print("En iyi uygunluk değeri:", fitness(best))
