
calibration_table = [
    (value_ps10, psi) for value_ps10, psi in [
        (0, 0),
        (8226, 0),

        # 10 psi
        (11410, 10),
        (11426, 10),
        (11474, 10),
        (11490, 10),
        (11522, 10),
        (11538, 10),

        # 30 psi
        (15027, 30),
        (15107, 30),
        (15075, 30),
        (15123, 30),
        (15139, 30),
        (15155, 30),

        # 40 psi
        (17732, 40),
        (17748, 40),
        (17812, 40),
        (17844, 40),
        (17860, 40),

        # 50 psi
        (19332, 50),
        (19364, 50),
        (19428, 50),
        (19460, 50),
        (19492, 50),

        # 60 psi
        (22085, 60),
        (22101, 60),
        (22117, 60),
        (22165, 60),
        (22181, 60),
        (22229, 60),
        (22245, 60),
        (22309, 60),
    ]
]


def ps10_to_psi(ps10_value):
    low_point = None
    high_point = None

    for value_ps10, psi in calibration_table:
        if value_ps10 <= ps10_value:
            low_point = (value_ps10, psi)
        else:
            high_point = (value_ps10, psi)
            break

    if low_point is None or high_point is None:
        return None

    x0, y0 = low_point
    x1, y1 = high_point
    psi = y0 + (y1 - y0) * (ps10_value - x0) / (x1 - x0)
    return psi


def psi_to_bar(psi):
    return (psi*0.0689476)


def psi_to_kgfcm2(psi):
    return (psi*0.070307)
