from dataclasses import dataclass, asdict

@dataclass
class RiskAssessment:
    userid: int = None
    dataset_id: int = None
    tenantid: int = None
    average_prosecutor_risk: int = None
    maximum_prosecutor_risk: int = None 
    quasi_identifiers: str = ""
    risk_assessment: str = ""

    def to_dict(self):
        return asdict(self)
