import numpy as np

def f(x):
    return x ** 2

def monte_carlo_integral(f, a, b, N=100000):
    x_rand = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(0, f(b), N)
    under_curve = y_rand < f(x_rand)
    area_estimate = (b- a) * f(b) * np.sum(under_curve) / N
    return area_estimate

if __name__ == "__main__":
    a = 0
    b = 2
    monte_carlo_result = monte_carlo_integral(f, a, b)
    print("Оцінка інтегралу методом Монте-Карло: ", monte_carlo_result)