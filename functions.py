def r_1(t, params):
    return (params[0] * t) ** 3 + (params[1] * t) ** 2 + (params[2] * t) + params[3]


def r_2(t, params):
    return (params[0] * t) ** 3 + (params[1] * t) ** 2 + (params[2] * t) + params[3]


def r_3(t, params):
    return (params[0] * t) ** 3 + (params[1] * t) ** 2 + (params[2] * t) + params[3]


def r_4(t, params):
    return (params[0] * t) ** 3 + (params[1] * t) ** 2 + (params[2] * t) + params[3]


def pend(k, t, faks, f):
    seq = list(range(56))
    fxu = lambda x: fx(k[x - 1], f[seq.pop(0)])

    dkdt = [
        # 0
        (
            -(fxu(10) * fxu(11) * fxu(14))
        ),

        # 1
        (
                fxu(3) * fxu(7) * fxu(8) * fxu(9) * fxu(13) -
                (fxu(10) * fxu(11) * fxu(14) * fxu(15) *
                 r_1(t, faks[0]) + r_2(t, faks[1]) + r_3(t, faks[2]) + r_4(t, faks[3]))
        ),

        # 2
        (
                fxu(1) - (fxu(15) * r_1(t, faks[0]) + r_3(t, faks[2]) + r_4(t, faks[3]))
        ),

        # 3
        (
            fxu(1)
        ),

        # 4
        (
                fxu(1) * r_2(t, faks[1]) - r_1(t, faks[0])
        ),

        # 5
        (
                r_2(t, faks[1]) - (fxu(4) * fxu(11) * fxu(12) * fxu(14) * r_1(t, faks[0]))
        ),

        # 6
        (
                fxu(5) * fxu(6) * fxu(13) * fxu(15) * r_1(t, faks[0]) + r_2(t, faks[1]) + r_3(t, faks[2])
        ),

        # 7
        (
                fxu(5) * fxu(6) * fxu(11) * fxu(13) * fxu(14) * fxu(15) *
                r_1(t, faks[0]) + r_2(t, faks[1]) + r_3(t, faks[2])
        ),

        # 8
        (
                fxu(3) * fxu(13) * r_2(t, faks[1]) - fxu(10) * fxu(11) * fxu(14) * r_1(t, faks[0])
        ),

        # 9
        (
                fxu(3) * fxu(9) * fxu(15) *
                r_1(t, faks[0]) + r_2(t, faks[1]) + r_3(t, faks[2]) + r_4(t, faks[3])
        ),

        # 10
        (
                fxu(3) * fxu(13) * fxu(14) * r_1(t, faks[0]) + r_2(t, faks[1]) + r_3(t, faks[2]) -
                fxu(15) * r_4(t, faks[3])
        ),

        # 11
        (
                fxu(11) * fxu(13) * fxu(14) * r_1(t, faks[0]) + r_2(t, faks[1]) + r_3(t, faks[2]) -
                fxu(15)
        ),

        # 12
        (
                fxu(2) * fxu(3) * r_2(t, faks[1])
        ),

        # 13
        (
                fxu(11) * fxu(12) * fxu(13) * r_1(t, faks[0]) + r_2(t, faks[1])
        ),

        # 14
        (
                fxu(2) * fxu(3) * fxu(13) * fxu(14) * r_1(t, faks[0]) + r_2(t, faks[1])
        )
    ]
    return dkdt


def fx(x, params):
    return (params[0] * x) ** 3 + (params[1] * x) ** 2 + (params[2] * x) + params[3]
