from dataclasses import dataclass, asdict

@dataclass
class RiskAssessment:
    userid: int = None
    dataset_id: int = None
    tenantid: int = None
    risk_assessment: str = ""

    def to_dict(self):
        return asdict(self)
