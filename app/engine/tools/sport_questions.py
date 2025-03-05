from llama_index.core.tools import FunctionTool

questions = [
    "Kysymys 1: Pidätkö enemmän fyysisestä aktiivisuudesta vai ajattelutyöstä?",
    "Kysymys 2: Nautitko enemmän yksin toimimisesta vai tykkäätkö olla osa tiimiä?",
    "Kysymys 3: Haluatko kehittää taitojasi nopeammin, vai oletko valmis panostamaan pidempään harjoitteluun ja kehittymiseen?",
    "Kysymys 4: Pidätkö ulkoilusta vai oletko enemmän sisätiloissa viihtyvä tyyppi?",
    "Kysymys 5: Haluatko osallistua lajiin, joka vaatii nopeaa reaktiokykyä ja jännitystä, vai tykkäätkö rauhallisemmista ja keskittyneemmistä lajeista?",
    "Kysymys 6: Onko sinulle tärkeää, että harrastus tarjoaa mahdollisuuden rentoutua ja lievittää stressiä, vai haluatko jotain, joka haastaa ja pistää sinut kunnon koetukselle?"
]


def get_sports_questions() -> list:
    """Useful for getting questions to ask users with the goal of finding a good sport choice for user."""
    print("Getting sports questions...")
    return questions


def get_tools(**kwargs):
    return [FunctionTool.from_defaults(get_sports_questions)]