import src.utils.ps10_dataset as datasets


def ps10_to_psi(ps10_value):
    low_point = None
    high_point = None

    for value_ps10, psi in datasets.ps10_050_250_calibration_table:
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
    if psi == None:
        return 0
    return (psi*0.0689476)


def psi_to_kgfcm2(psi):
    if psi == None:
        return 0
    return (psi*0.07142)
