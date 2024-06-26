import datetime
from dataclasses import dataclass, fields, _MISSING_TYPE


@dataclass
class QuestionnaireQuestionAnswerRulePrefill:
    id: int = None

    questionid: int = 0
    answerid: int = None
    answer_text: str = ""

    createdat: datetime.datetime = None
    updatedat: datetime.datetime = None
    deletedat: datetime.datetime = None

    def __post_init__(self):
        for field in fields(self):
            if not isinstance(field.default, _MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)

@dataclass
class QuestionnaireQuestionAnswer:
    id: int = None

    text: str = ""
    risk_level: int = 0

    rule_prefills: list[QuestionnaireQuestionAnswerRulePrefill] = None

    createdat: datetime.datetime = None
    updatedat: datetime.datetime = None
    deletedat: datetime.datetime = None

    def __post_init__(self):
        for field in fields(self):
            if not isinstance(field.default, _MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)

@dataclass
class QuestionnaireQuestion:
    id: int = None

    tab: str = ""
    question: str = ""
    risk_weight: int = 0
    answer_type: str = ""
    flag: str = ""
    tooltip: str = ""

    answers: list[QuestionnaireQuestionAnswer] = None

    createdat: datetime.datetime = None
    updatedat: datetime.datetime = None
    deletedat: datetime.datetime = None

    def __post_init__(self):
        for field in fields(self):
            if not isinstance(field.default, _MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)


@dataclass
class QuestionnaireVersion:
    id: int = None

    version: str = ""

    questions: list[QuestionnaireQuestion] = None

    createdat: datetime.datetime = None
    updatedat: datetime.datetime = None
    deletedat: datetime.datetime = None

    def __post_init__(self):
        for field in fields(self):
            if not isinstance(field.default, _MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)

@dataclass
class Questionnaire:
    id: int = None

    userid: int = 0
    tenantid: int = 0
    name: str = ""
    reply_editable: bool = False

    versions: list[QuestionnaireVersion] = None
    last_version: str = ""

    createdat: datetime.datetime = None
    updatedat: datetime.datetime = None
    deletedat: datetime.datetime = None

    def __post_init__(self):
        for field in fields(self):
            if not isinstance(field.default, _MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)







