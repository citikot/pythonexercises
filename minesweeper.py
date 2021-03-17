"""
У цьому завданні ви спробуєте створити спрощену версію популярної одиночної гри «Сапер» (англ. Minesweeper). 
Ми надамо Python-модуль з чорновим кодом для майбутньої гри, а ваша задача – реалізувати функцію generate_maze. 
Зауважте, що не можна прибирати/модифікувати ніякий інший код, крім області видимості функції generate_maze, 
тому ваш розв’язок має міститися тільки в тілі функції generate_maze.

generate_maze має створювати сітку для майбутньої гри в форматі списку списків (приклад сітки 2X2: grid = [[X,X],[X, X]]), 
де кожна точка сітки має бути -1, якщо це міна. 
В іншому випадку, вона має бути іншим цілим числом, яке відповідає кількості замінованих сусідніх точок.

"""

import random
import sys

ALLOWED_GAME_MODES = {'beginner', 'medium', 'expert'}
PREDEFINED_MODES = {
    'beginner': (8, 8, 10),
    'medium': (16, 16, 40),
    'expert': (16, 30, 99),
}


def generate_maze(max_rows, max_cols, max_mines):
    ...


def print_maze(maze_matrix):
    for i in range(len(maze_matrix)):
        for j in range(len(maze_matrix[0])):
            item = "*" if maze_matrix[i][j] == -1 else str(maze_matrix[i][j])
            print(item, end=' ')
        print()


def main(mode='beginner'):
    print_maze(generate_maze(*PREDEFINED_MODES[mode]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Only one parameter is allowed.')

    game_mode = sys.argv[1]
    if game_mode not in ALLOWED_GAME_MODES:
        raise ValueError('Only beginner, medium and expert models are allowed')

    main(game_mode)
