import random


def calculate_hit(name, weapon):
    """
    Arvutab löögijõu vastavalt kangelase nime pikkusele ja relva nime pikkusele.

    Löögijõud = kangelase nime pikkus + juhuslik arv vahemikus 0 kuni relva pikkus.

    Args:
        hero_name (str): Tegelase nimi.
        weapon (str): Relva nimi.

    Returns:
        int: Löögijõu arvuline väärtus.
    """

    baas = len(name)
    boonus = random.randint(0, len(weapon))

    return baas + boonus