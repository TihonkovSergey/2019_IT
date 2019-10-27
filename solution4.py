import matplotlib.pyplot as plt
import numpy as np

def get_efficients(X):
    """
    Возвращает одномерные массив,
    где для каждого i-го вектора в i-й позиции
    стоит True если он эффективен по парето 
    False - если не эффективен
    """
    candidates = np.ones(X.shape[0], dtype=bool)
    for i, vec in enumerate(X): # с- вектор, кандидат (на данный момент) на эф-ть по парето
        if candidates[i]: # если текущая точка - кандидат на эф-ть
            candidates[candidates] = np.any(X[candidates] > vec, axis=1) # обновляем для остальных кандидатов
            candidates[i] = True  # могли занулить самого себя
    return candidates

def main():
    n = 5
    m = 4

    x = np.random.randint(0, 10, (n, m)) # генерим рандомные вектора
 
    # считаем эф-ть по парето, делим вектора на хорошие и плохие
    candidates = get_efficients(x)
    efficients = x[candidates]
    others = x[np.invert(candidates)]

    # рисуем
    _, plots = plt.subplots(ncols=2, subplot_kw=dict(polar=True))
    plt.subplots_adjust(wspace=0.7)
    plots[0].set_title('Первоначальный массив', pad=20)
    plots[1].set_title('Парето', pad=20)
    
    axis = np.linspace(0,  2 * np.pi, num=x[0].shape[0] + 1)

    for v in efficients:
        plots[1].plot(axis, np.append(v, v[0]), color = "g")

    for v in others:
        plots[1].plot(axis, np.append(v, v[0]), color = "r") 

    for v in x:
        plots[0].plot(axis, np.append(v, v[0]))

    plt.show()

if __name__ == '__main__':
    main()