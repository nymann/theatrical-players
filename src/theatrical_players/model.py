from dataclasses import dataclass


@dataclass
class Play:
    name: str
    type: str


@dataclass
class Performance:
    play: Play
    audience: int


@dataclass
class CustomerPerformances:
    customer: str
    performances: list[Performance]

    @classmethod
    def from_json(cls, invoice: dict, plays: dict) -> "CustomerPerformances":
        customer = invoice["customer"]
        performances: list[Performance] = []
        for performance in invoice["performances"]:
            play_id = performance["playID"]
            performances.append(
                Performance(
                    play=Play(**plays[play_id]),
                    audience=int(performance["audience"]),
                ),
            )
        return cls(customer=customer, performances=performances)
