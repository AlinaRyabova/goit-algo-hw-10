import scipy.integrate as spi

def f(x):
    return x ** 2

if __name__ == "__main__":
    a = 0
    b = 2
    result, error = spi.quad(f, a, b)
    print("Інтеграл (функція quad): ", result)
    print("Оцінка абсолютної помилки: ", error)