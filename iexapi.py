
class Sandbox:
    def __init__(self):
        self.token = "Tpk_a92c306efffe4bbea4f9706eca184920"
        self.apiBase ="https://sandbox.iexapis.com/stable"


class Prod:
    def __init__(self):
        self.token = ""
        self.apiBase = ""


class Stock:
    def __init__(self, symbol, field):
        self.symbol = symbol
        self.field = field

    def value(self, baseAPI):
        url = baseAPI.apiBase + "/stock/" + self.symbol + "/" + self.field + "?token=" + baseAPI.token



