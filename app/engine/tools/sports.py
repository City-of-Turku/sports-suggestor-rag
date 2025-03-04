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


def get_sports() -> list:
    """Usfeful for getting all sport options and their defining attributes."""
    #print("Getting sports...")
    return sports_list


def get_tools(**kwargs):
    return [FunctionTool.from_defaults(get_sports)]