@dataclass(frozen=True)
class Outcome:
    category: str
    kind: str
    days: Decimal
    note: str

@dataclass(frozen=True)
class Balance:
    user_id: int
    category: str
    days: Decimal

def _convert_vacation(unused: Decimal, ratio: Decimal) -> Decimal:
    if unused <= 0 or ratio <= 0:
        return Decimal("0")
    return (unused / ratio).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def plan(policy: Policy, kind: str, balances: list[Balance], year: int) -> list[Outcome]:
