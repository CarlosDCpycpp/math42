from ._bases.convertion_bases import *
from ._utils import number


__all__: list[str] = ['distance', 'weight', 'area', 'volume', 'speed', 'time']


def distance(a: str, b: str, num: number) -> number:
    """Converts distance between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm,cm, dm, m, dam, hm, km"""

    units = ["mm", "cm", "dm", "m", "dam", "hm", "km"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm":
            for i, j in conv_mm.items():
                if i == b:
                    return num * j
        case "cm":
            for i, j in conv_cm.items():
                if i == b:
                    return num * j
        case "dm":
            for i, j in conv_dm.items():
                if i == b:
                    return num * j
        case "m":
            for i, j in conv_m.items():
                if i == b:
                    return num * j
        case "dam":
            for i, j in conv_dam.items():
                if i == b:
                    return num * j
        case "hm":
            for i, j in conv_hm.items():
                if i == b:
                    return num * j
        case "km":
            for i, j in conv_km.items():
                if i == b:
                    return num * j


def weight(a: str, b: str, num: number) -> number:
    """Converts weight between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mg, g, kg, t"""

    units = ["mg", "g", "kg", "t"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mg":
            for i, j in conv_mg.items():
                if i == b:
                    return num * j
        case "g":
            for i, j in conv_g.items():
                if i == b:
                    return num * j
        case "kg":
            for i, j in conv_kg.items():
                if i == b:
                    return num * j
        case "t":
            for i, j in conv_t.items():
                if i == b:
                    return num * j


def area(a: str, b: str, num: number) -> number:
    """Converts area between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm2, cm2, dm2, m2, dam2, hm2, ha, ac, km2"""

    units = ["mm2", "cm2", "dm2", "m2", "dam2", "hm2", "ha", "ac", "km2"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm2":
            for i, j in conv_mm2.items():
                if i == b:
                    return num * j
        case "cm2":
            for i, j in conv_cm2.items():
                if i == b:
                    return num * j
        case "dm2":
            for i, j in conv_dm2.items():
                if i == b:
                    return num * j
        case "m2":
            for i, j in conv_m2.items():
                if i == b:
                    return num * j
        case "dam2":
            for i, j in conv_dam2.items():
                if i == b:
                    return num * j
        case "hm2":
            for i, j in conv_hm2.items():
                if i == b:
                    return num * j
        case "ha":
            for i, j in conv_ha.items():
                if i == b:
                    return num * j
        case "ac":
            for i, j in conv_ac.items():
                if i == b:
                    return num * j
        case "km2":
            for i, j in conv_km2.items():
                if i == b:
                    return num * j


def volume(a: str, b: str, num: number) -> number:
    """Converts volume between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm3, cm3, dm3, m3, dam3, hm3, km3"""

    units = ["mm3", "cm3", "dm3", "m3", "dam3", "hm3", "km3"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm3":
            for i, j in conv_mm3.items():
                if i == b:
                    return num * j
        case "cm3":
            for i, j in conv_cm3.items():
                if i == b:
                    return num * j
        case "dm3":
            for i, j in conv_dm3.items():
                if i == b:
                    return num * j
        case "m3":
            for i, j in conv_m3.items():
                if i == b:
                    return num * j
        case "dam3":
            for i, j in conv_dam3.items():
                if i == b:
                    return num * j
        case "hm3":
            for i, j in conv_hm3.items():
                if i == b:
                    return num * j
        case "km3":
            for i, j in conv_km3.items():
                if i == b:
                    return num * j


def speed(a: str, b: str, num: number) -> number:
    """Converts speed between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: mm/s, cm/s, dm/s, m/s, dam/s, hm/s, km/h"""

    units = ["mm/s", "cm/s", "dm/s", "m/s", "dam/s", "hm/s", "km/h"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "mm/s":
            for i, j in conv_mm_s.items():
                if i == b:
                    return num * j
        case "cm/s":
            for i, j in conv_cm_s.items():
                if i == b:
                    return num * j
        case "dm/s":
            for i, j in conv_dm_s.items():
                if i == b:
                    return num * j
        case "m/s":
            for i, j in conv_m_s.items():
                if i == b:
                    return num * j
        case "dam/s":
            for i, j in conv_dam_s.items():
                if i == b:
                    return num * j
        case "hm/s":
            for i, j in conv_hm_s.items():
                if i == b:
                    return num * j
        case "km/h":
            for i, j in conv_km_h.items():
                if i == b:
                    return num * j


def time(a: str, b: str, num: number) -> number:
    """Converts time between units (metric).
    The units must be input in the "a" and "b" variables, "a" is the original and "b" the unit of the return,
    the units have to be input as a string in the formation of the list below.
    Accepted units: ms, s, min, h, d, wk, mo, yr"""

    units = ["ms", "s", "min", "h", "d", "wk", "mo", "yr"]

    if a not in units or b not in units:
        raise TypeError(f"Either {a} or {b} are not identified units.")

    match a:
        case "ms":
            for i, j in conv_ms.items():
                if i == b:
                    return num * j
        case "s":
            for i, j in conv_s.items():
                if i == b:
                    return num * j
        case "min":
            for i, j in conv_min.items():
                if i == b:
                    return num * j
        case "h":
            for i, j in conv_h.items():
                if i == b:
                    return num * j
        case "d":
            for i, j in conv_d.items():
                if i == b:
                    return num * j
        case "wk":
            for i, j in conv_wk.items():
                if i == b:
                    return num * j
        case "mo":
            for i, j in conv_mo.items():
                if i == b:
                    return num * j

        case "yr":
            for i, j in conv_yr.items():
                if i == b:
                    return num * j
