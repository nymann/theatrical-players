from theatrical_players.string_statement_printer import StringStatementPrinter


def statement(invoice, plays):
    return StringStatementPrinter(invoice=invoice, plays=plays).print()
