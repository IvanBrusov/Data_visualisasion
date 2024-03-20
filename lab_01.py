#  Lab 01 - Ivan Brusov - Variant 3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def Plot2D():
    def f_1(x):
        return (2 + np.power(np.sin(x), 3)) / (1 + np.power(x, 2))

    def f_2(x):
        return np.where(x <= 0, (5 * np.power(x, 2)) / (1 + np.power(x, 2)), np.sqrt(1 + (2 * x) / (1 + np.power(x, 2))))

    X = np.arange(-10, 10, 0.01)
    y = f_1(X)
    plt.plot(X, y)
    plt.title(r"$y = \frac{2+sin^3(x)}{1+x^2}$", fontsize=15, y=1.1, pad=-14)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    z = f_2(X)
    plt.plot(X, z)
    plt.title(r"$z={}\frac{5x^2}{1+x^2}, x≤0,"
              r"\sqrt{1+\frac{2x}{1+x^2}}, x>0$", fontsize=15, y=1.1, pad=-14)
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.show()


def PlotSurface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(-10, 10, 0.1)
    Y = np.arange(-10, 10, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = 10 * np.power(X, 3) * np.power(np.sin(Y), 2) - 2 * np.power(X, 2) * np.power(Y, 3)

    surf = ax.plot_surface(X, Y, Z, cmap='viridis')
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title("$z = 10x^3sin^2(y)-2x^2y^3$", fontsize=15)
    plt.xlabel("X")
    plt.ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


def PlotPolar():
    def strophoid_polar(theta):
        a = 0.1
        r = a * ((1 + np.sin(theta))/(np.cos(theta)))
        return r, theta

    theta = np.linspace(0, 2 * np.pi, 500)
    r, theta = strophoid_polar(theta)
    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, r)
    ax.set_rmax(50)
    ax.set_rticks([0, 25, 50])
    ax.set_rlabel_position(-22.5)
    ax.grid(True)
    ax.set_title(r"$ρ = \frac{(1±sinφ)}{cosφ }$")
    plt.show()


def PlotSurfaceSecondOrder():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    a, b, c = 1, 2, 3
    X = np. arange(-5, 5, 0.25)
    Y = np. arange(-5, 5, 0.25)
    X, Y = np. meshgrid(X, Y)

    Z1 = c * np.sqrt(1 + np.power(X, 2)/np.power(a, 2) + np.power(Y, 2)/np.power(b, 2))
    Z2 = -c * np.sqrt(1 + np.power(X, 2)/np.power(a, 2) + np.power(Y, 2)/np.power(b, 2))


    ax.plot_surface(X, Y, Z1, cmap='viridis',
                           linewidth=0, antialiased=False)
    ax.plot_surface(X, Y, Z2, cmap='viridis',
                           linewidth=0, antialiased=False)

    ax.set_title(r"$ \frac{x^2}{a^2} +\frac{y^2}{b^2}+\frac{z^2}{c^2}=-1 $", fontsize=25)
    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)
    ax.set_zlabel('Z', fontsize=14)
    ax.view_init(elev=30, azim=-45)

    plt.show()


def PlotBarCart():
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
    germany_values = [29, 51, 59, 478, 93, 244, 420, 510, 575, 625]
    france_values = [28, 46, 57, 52, 63, 93, 190, 275, 310, 355]
    uk_values = [53, 73, 84, 105, 130, 180, 245, 265, 300, 335]
    ussr_values = [40, 70, 80, 105, 205, 480, 725, 935, 1000, 545]

    fig, ax = plt.subplots(figsize=(12, 6))
    bar_width = 0.2
    index = range(len(years))
    ax.bar(index, germany_values, bar_width, label='Германія', color="orange")
    ax.bar([i + bar_width for i in index], france_values, bar_width, label='Франція')
    ax.bar([i + 2*bar_width for i in index], uk_values, bar_width, label='Великобританія')
    ax.bar([i + 3*bar_width for i in index], ussr_values, bar_width, label='СРСР')

    ax.set_xlabel('Рік', fontsize=12)
    ax.set_ylabel('млрд. дол', fontsize=12)
    ax.set_xticks([i + 1.5*bar_width for i in index])
    ax.set_xticklabels(years, rotation=45, ha='right')
    ax.set_title("Промислове виробництво, додана вартість")
    ax.legend()

    plt.tight_layout()
    plt.show()


def Plot3DChart():
    ax = plt.axes(projection="3d")

    countries = [" ", " ","Германія", " ", "Франція", " ", "Великобританія", " ", "СРСР"]
    data = np.array([[29, 51, 59, 478, 93, 244, 420, 510, 575, 625],
                     [28, 46, 57, 52, 63, 93, 190, 275, 310, 355],
                     [53, 73, 84, 105, 130, 180, 245, 265, 300, 335],
                     [40, 70, 80, 105, 205, 480, 725, 935, 1000, 545]])
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970,  1980, 1990, 2000]
    numOfCols = 10
    numOfRows = 4

    xpos = np.arange(0, numOfCols, 1)
    ypos = np.arange(0, numOfRows, 1)
    xpos, ypos = np.meshgrid(xpos + 0.5, ypos + 0.5)


    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros(numOfCols * numOfRows)

    dx = np.ones(numOfRows * numOfCols) * 0.5
    dy = np.ones(numOfCols * numOfRows) * 0.5
    dz = data.flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    index = np. arange(10)
    ax. set_xticks(index + 8 / 9)
    ax.set_xticklabels(years, fontsize=5)
    ax.set_yticklabels(countries)

    ax.set_xlabel('Роки')
    ax.set_zlabel('млрд. дол')

    plt.show()


def main():
    Plot2D()
    PlotSurface()
    PlotPolar()
    PlotSurfaceSecondOrder()
    PlotBarCart()
    Plot3DChart()


if __name__ == "__main__":
    main()
