from dataclasses import dataclass, asdict

@dataclass
class RiskAssessment:
    userid: int = None

    def to_dict(self):
        return asdict(self)
