import math


def statement(invoice, plays):
    total_amount = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    def amount_for_tragedy(perf) -> float:
        this_amount = 40000
        if perf["audience"] > 30:
            this_amount += 1000 * (perf["audience"] - 30)
        return this_amount

    def amount_for_comedy(perf) -> float:
        this_amount = 30000
        if perf["audience"] > 20:
            this_amount += 10000 + 500 * (perf["audience"] - 20)

        this_amount += 300 * perf["audience"]
        return this_amount

    def amount_for_performance(perf) -> float:
        play = plays[perf["playID"]]
        if play["type"] == "tragedy":
            return amount_for_tragedy(perf)
        if play["type"] == "comedy":
            return amount_for_comedy(perf)
        raise ValueError(f'unknown type: {play["type"]}')

    def volume_credits_for_performances() -> float:
        volume_credits = 0
        for perf in invoice["performances"]:
            play = plays[perf["playID"]]
            volume_credits += max(perf["audience"] - 30, 0)
            if "comedy" == play["type"]:
                volume_credits += math.floor(perf["audience"] / 5)
        return volume_credits

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = amount_for_performance(perf)
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits_for_performances()} credits\n"
    return result
