import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import logging

from functions import pend, r_1, r_2, r_3, r_4
from radar_diagram import RadarDiagram
from utils import lines

data_sol = []
logger = logging.getLogger('uvicorn.error')


def fill_diagrams(data, initial_equations, restrictions):
    radar1 = RadarDiagram()
    radar1.draw('./static/images/diagram.png', initial_equations, u_list,
                "Характеристики системы в начальный момент времени", restrictions)
    radar1.draw('./static/images/diagram2.png', data[int(len(data) / 4)], u_list,
                "Характеристики системы в 1 четверти", restrictions)
    radar1.draw('./static/images/diagram3.png', data[int(len(data) / 2)], u_list,
                "Характеристики системы во 2 четверти", restrictions)
    radar1.draw('./static/images/diagram4.png', data[int(len(data) / 4 * 3)], u_list,
                "Характеристики системы в 3 четверти", restrictions)
    radar1.draw('./static/images/diagram5.png', data[-1, :], u_list,
                "Характеристики системы в последний момент времени", restrictions)


def create_graphic(t, data, faks):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(111)
    for i in range(15):
        plt.plot(t, data[:, i], color=lines[i][0], linestyle=lines[i][1], label=u_list[i])
    plt.xlabel("t")
    plt.legend(loc=(.75, .64), labelspacing=0.1, fontsize='small')
    # plt.draw()
    plt.xlim([0, 1])
    draw_third_graphic(t, faks)
    fig.savefig('./static/images/figure.png')


def draw_third_graphic(t, faks):
    fig, axs = plt.subplots(figsize=(15, 10))
    plt.subplot(1, 1, 1)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for i in t:
        y1.append(r_1(i, faks[0]))
        y2.append(r_2(i, faks[1]))
        y3.append(r_3(i, faks[2]))
        y4.append(r_4(i, faks[3]))

    plt.plot(t, y1, label='R1')
    plt.plot(t, y2, label='R2')
    plt.plot(t, y3, label='R3')
    plt.plot(t, y4, label='R4')
    plt.legend(loc='best')
    plt.xlabel('t')
    # plt.draw()
    fig.savefig("./static/images/figure2.png")


def cast_to_float(initial_equations, faks, equations, restrictions):
    for i in range(len(initial_equations)):
        initial_equations[i] = float(initial_equations[i])

    logger.info("init_eq")

    for i in range(len(faks)):
        for j in range(len(faks[i])):
            faks[i][j] = float(faks[i][j])

    logger.info("faks")

    for i in range(len(equations)):
        for j in range(len(equations[i])):
            equations[i][j] = float(equations[i][j])

    logger.info("equations")

    for i in range(len(restrictions)):
        restrictions[i] = float(restrictions[i])

    logger.info("restrictions")
    return initial_equations, faks, equations, restrictions


def process(initial_equations, faks, equations, restrictions):
    global data_sol

    cast_to_float(initial_equations, faks, equations, restrictions)

    t = np.linspace(0, 1)
    data_sol = odeint(pend, initial_equations, t, args=(faks, equations))
    create_graphic(t, data_sol, faks)
    fill_diagrams(data_sol, initial_equations, restrictions)


u_list = [
    "Время испарения химически опасных веществ в районе аварии с поверхности земли",
    "Время ликвидации последствий аварии на химически опасном объекте",
    "Площадь заражения в результате аварии",
    "Время подхода первичного и/или вторичного облака к населенным пунктам",
    "Потери от первичного облака",
    "Потери от вторичного облака",
    "Количество получивших амбулаторную помощь, чел.",
    "Количество размещенных в стационаре и реанимации, чел.",
    "Количество пораженной техники",
    "Количество объемов и растворов для обеззараживания местности",
    "Количество сил и средств, необходимых для проведения аварийно-спасательных работ",
    "Эффективность системы оповещения, %.",
    "Количество людей в зоне поражения",
    "Количество спасателей в зоне поражения",
    "Развитость системы МЧС"
]
