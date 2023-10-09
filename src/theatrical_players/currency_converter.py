from abc import ABC
from abc import abstractmethod


class CurrencyFormatter(ABC):
    @abstractmethod
    def format(self, amount: float) -> str:
        raise NotImplementedError


class UsdFormatter(CurrencyFormatter):
    def format(self, amount: float) -> str:
        dollars = amount / 100
        return f"${dollars:0,.2f}"
