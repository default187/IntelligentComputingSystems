#Задача 8 пешек
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.optimizers import Adam

# Параметры
n = 8
input_size = n * n
hidden_size = 64
output_size = n * n
learning_rate = 0.001
episodes = 10000

# Создание модели
model = Sequential([
    Flatten(input_shape=(n, n)),
    Dense(hidden_size, activation='relu'),
    Dense(output_size, activation='linear'),
    Reshape((n, n))
])

model.compile(optimizer=Adam(learning_rate=learning_rate), loss='mse')

def is_valid(board):
    rows = np.sum(board, axis=1)
    cols = np.sum(board, axis=0)
    if not np.all(rows <= 1) or not np.all(cols <= 1):
        return False
    main_diag = [np.sum(np.diag(board, k)) for k in range(-n+1, n)]
    anti_diag = [np.sum(np.diag(np.fliplr(board), k)) for k in range(-n+1, n)]
    if not np.all(np.array(main_diag) <= 1) or not np.all(np.array(anti_diag) <= 1):
        return False
    return True

def get_reward(board):
    if np.sum(board) != n:
        return -1
    if is_valid(board):
        return 1
    return -1

# Обучение модели
for episode in range(episodes):
    board = np.zeros((n, n))
    for step in range(n):
        q_values = model.predict(board[np.newaxis])
        action = np.unravel_index(np.argmax(q_values), (n, n))
        board[action] = 1
        reward = get_reward(board)
        if reward == 1:
            break
        elif reward == -1:
            board[action] = 0
    target = reward
    target_f = model.predict(board[np.newaxis])
    target_f[0][action] = target
    model.fit(board[np.newaxis], target_f, epochs=1, verbose=0)

# Тестирование модели
def print_board(board):
    for row in board:
        print(" ".join(str(int(x)) for x in row))

test_board = np.zeros((n, n))
for step in range(n):
    q_values = model.predict(test_board[np.newaxis])
    action = np.unravel_index(np.argmax(q_values), (n, n))
    test_board[action] = 1

print("Решение:")
print_board(test_board)
