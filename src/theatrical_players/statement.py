from theatrical_players.currency_converter import UsdFormatter
from theatrical_players.model import CustomerPerformances
from theatrical_players.plaintext_statement import PlaintextStatement


def statement(invoice: dict, plays: dict) -> str:
    statement_renderer = PlaintextStatement(currentcy_formatter=UsdFormatter())
    return statement_renderer.render(customer_performances=CustomerPerformances.from_json(invoice=invoice, plays=plays))
