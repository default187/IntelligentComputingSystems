import numpy as np
import random

# Параметры задачи
n = 8  # Размер доски n x n
population_size = 100  # Размер популяции
generations = 10000  # Максимальное количество поколений
mutation_rate = 0.01  # Вероятность мутации

def create_individual():
    """Создает индивидуальную расстановку шашек"""
    return np.random.permutation(n)

def create_population(size):
    """Создает начальную популяцию заданного размера"""
    return [create_individual() for _ in range(size)]

def fitness(individual):
    """Оценивает расстановку по количеству неатакующих шашек"""
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return n * (n - 1) / 2 - conflicts

def select(population):
    """Выбирает лучшие расстановки для создания следующего поколения"""
    weights = [fitness(individual) for individual in population]
    return random.choices(population, weights=weights, k=len(population))

def crossover(parent1, parent2):
    """Создает потомство путем комбинирования двух родителей"""
    point = random.randint(0, n - 1)
    child = np.concatenate((parent1[:point], parent2[point:]))
    if len(set(child)) < n:  # Убедиться, что потомство - это перестановка
        child = np.random.permutation(n)
    return child

def mutate(individual):
    """Случайно изменяет расстановку (мутация)"""
    if random.random() < mutation_rate:
        i, j = random.sample(range(n), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

def genetic_algorithm():
    """Основной цикл генетического алгоритма"""
    population = create_population(population_size)
    
    for generation in range(generations):
        population = select(population)
        new_population = []
        
        for i in range(0, population_size, 2):
            parent1, parent2 = population[i], population[i + 1]
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
        
        # Проверка на решение
        for individual in population:
            if fitness(individual) == n * (n - 1) / 2:
                return individual, generation
        
        # Вывод текущего поколения и наилучшего результата
        best_fitness = max(fitness(ind) for ind in population)
        print(f"Эпоха {generation}: лучший результат {best_fitness}") #best_fitness - мера качества расстановки ферзей на доске (n*(n-1)/2)
    
    return None, generations

def print_board(individual):
    """Выводит доску с расстановкой шашек"""
    board = np.zeros((n, n), dtype=int)
    for row, col in enumerate(individual):
        board[row, col] = 1
    for row in board:
        print(" ".join(str(x) for x in row))

# Запуск генетического алгоритма
solution, gen = genetic_algorithm()

# Вывод результата
if solution is not None:
    print(f"Решение найдено на поколении {gen}:")
    print_board(solution)
else:
    print("Решение не найдено.")
