from llama_index.core.tools import FunctionTool


sports_list = [
  {
    "sport": "Ampumaurheilu",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "environment": "Sisä",
    "intensity": "Rauhallinen"
  },
  {
    "sport": "BMX ja pyöräily",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Ulko",
    "intensity": "Reaktio"
  },
  {
    "sport": "Cheerleading ja cheertanssi",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Golf",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "environment": "Ulko",
    "intensity": "Rauhallinen"
  },
  {
    "sport": "Jalkapallo ja futsal",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Ulko ja sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Joukkuevoimistelu",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Jääkiekko",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Kamppailulajit",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Koripallo",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Lentopallo ja beach volley",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Moottoriurheilu",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "environment": "Ulko",
    "intensity": "Rauhallinen"
  },
  {
    "sport": "Nyrkkeily",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Paini",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Ratsastus",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "environment": "Ulko",
    "intensity": "Rauhallinen"
  },
  {
    "sport": "Salibandy",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Suunnistus",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "environment": "Ulko",
    "intensity": "Rauhallinen"
  },
  {
    "sport": "Taito- ja muodostelmaluistelu",
    "activity_type": "Aktiivinen",
    "interaction_type": "yksin ja yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Tanssi",
    "activity_type": "Aktiivinen",
    "interaction_type": "yksin ja yhdessä",
    "environment": "Sisä",
    "intensity": "Rauhallinen"
  },
  {
    "sport": "Telinevoimistelu",
    "activity_type": "Aktiivinen",
    "interaction_type": "yksin",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Tennis ja padel",
    "activity_type": "Aktiivinen",
    "interaction_type": "yksin ja yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Uinti ja vesiliikunta",
    "activity_type": "Aktiivinen",
    "interaction_type": "yksin ja yhdessä",
    "environment": "Sisä",
    "intensity": "Reaktio"
  },
  {
    "sport": "Yleisurheilu",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "environment": "Ulko",
    "intensity": "Reaktio"
  }
]

sports_list_large = [
  {
    "sport": "Ampumaurheilu",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Rauhallinen",
    "challenge_level": "Helppo"
  },
  {
    "sport": "BMX ja pyöräily",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Pidemmin",
    "environment": "Ulko",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Cheerleading ja cheertanssi",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Golf",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "progress_rate": "Pidemmin",
    "environment": "Ulko",
    "intensity": "Rauhallinen",
    "challenge_level": "Helppo"
  },
  {
    "sport": "Jalkapallo ja futsal",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Ulko ja sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Joukkuevoimistelu",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Rauhallinen",
    "challenge_level": "Helppo"
  },
  {
    "sport": "Jääkiekko",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Kamppailulajit",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Koripallo",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Lentopallo ja beach volley",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Moottoriurheilu",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "progress_rate": "Pidemmin",
    "environment": "Ulko",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Muut lajit",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin ja pidemmin",
    "environment": "Ulko ja sisä",
    "intensity": "Reaktio ja rauhallinen",
    "challenge_level": "Helppo ja haastava"
  },
  {
    "sport": "Muut palloilulajit",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin ja yhdessä",
    "progress_rate": "Nopeammin ja pidemmin",
    "environment": "Ulko ja sisä",
    "intensity": "Reaktio ja rauhallinen",
    "challenge_level": "Helppo ja haastava"
  },
  {
    "sport": "Muut voimistelulajit ja sirkus",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Helppo"
  },
  {
    "sport": "Nyrkkeily",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Paini",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Ratsastus",
    "activity_type": "Ajattelu",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin",
    "environment": "Ulko",
    "intensity": "Rauhallinen",
    "challenge_level": "Helppo"
  },
  {
    "sport": "Salibandy",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Suunnistus",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin",
    "environment": "Ulko",
    "intensity": "Rauhallinen",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Taito- ja muodostelmaluistelu",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin ja yhdessä",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Rauhallinen",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Tanssi",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin ja yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio ja rauhallinen",
    "challenge_level": "Helppo"
  },
  {
    "sport": "Telinevoimistelu",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin ja yhdessä",
    "progress_rate": "Pidemmin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Tennis ja padel",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin ja yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  },
  {
    "sport": "Uinti ja vesiliikunta",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin ja yhdessä",
    "progress_rate": "Nopeammin",
    "environment": "Sisä",
    "intensity": "Rauhallinen",
    "challenge_level": "Helppo"
  },
  {
    "sport": "Yleisurheilu",
    "activity_type": "Aktiivinen",
    "interaction_type": "Yksin",
    "progress_rate": "Nopeammin",
    "environment": "Ulko",
    "intensity": "Reaktio",
    "challenge_level": "Haastava"
  }
]


def get_sports() -> list:
    """Useful for getting all sport options and their defining attributes."""
    #print("Getting sports...")
    #return sports_list
    return sports_list_large


def get_tools(**kwargs):
    return [FunctionTool.from_defaults(get_sports)]