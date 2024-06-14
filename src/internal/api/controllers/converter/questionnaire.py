from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire import QuestionnaireVersion
from src.pkg.questionnaire.model.questionnaire import QuestionnaireQuestion
from src.pkg.questionnaire.model.questionnaire import QuestionnaireQuestionAnswer
from src.pkg.questionnaire.model.questionnaire import QuestionnaireQuestionAnswerRulePrefill
from server_template.models import TemplatebackendQuestionnaire
from server_template.models import TemplatebackendQuestionnaireVersion
from server_template.models import TemplatebackendQuestionnaireQuestion
from server_template.models import TemplatebackendQuestionnaireQuestionAnswer
from server_template.models import TemplatebackendQuestionnaireQuestionAnswerRulePrefill

# def questionnaire_to_business(questionnaire: TemplatebackendQuestionnaire) -> Questionnaire:
#     return Questionnaire(
#         id=questionnaire.id,
#         userid=questionnaire.user_id,
#         frequency=questionnaire.frequency,
#     )

# def questionnaire_from_business(questionnaire: Questionnaire) -> TemplatebackendQuestionnaire:
#     return TemplatebackendQuestionnaire(
#         id=questionnaire.id,
#         user_id=questionnaire.userid,
#         created_at=questionnaire.createdat,
#         updated_at=questionnaire.updatedat
#     )

def questionnaire_from_business(questionnaire: Questionnaire) -> TemplatebackendQuestionnaire:
    return TemplatebackendQuestionnaire(
        id=questionnaire.id,
        name=questionnaire.name,
        reply_editable=questionnaire.reply_editable,
        versions=[questionnaire_version_from_business(version) for version in questionnaire.versions] if questionnaire.versions else [],
        created_at=questionnaire.createdat,
        updated_at=questionnaire.updatedat,
    )


def questionnaire_version_from_business(version: QuestionnaireVersion) -> TemplatebackendQuestionnaireVersion:
    return TemplatebackendQuestionnaireVersion(
        id=version.id,
        version=version.version,
        questions=[questionnaire_question_from_business(question) for question in version.questions] if version.questions else [],
        created_at=version.createdat,
        updated_at=version.updatedat,
    )


def questionnaire_question_from_business(question: QuestionnaireQuestion) -> TemplatebackendQuestionnaireQuestion:
    return TemplatebackendQuestionnaireQuestion(
        id=question.id,
        tab=question.tab,
        question=question.question,
        risk_weight=question.risk_weight,
        answer_type=question.answer_type,
        flag=question.flag,
        tooltip=question.tooltip,
        answers=[questionnaire_question_answer_from_business(answer) for answer in question.answers] if question.answers else [],
        created_at=question.createdat,
        updated_at=question.updatedat,
    )


def questionnaire_question_answer_from_business(answer: QuestionnaireQuestionAnswer) -> TemplatebackendQuestionnaireQuestionAnswer:
    return TemplatebackendQuestionnaireQuestionAnswer(
        id=answer.id,
        text=answer.text,
        risk_level=answer.risk_level,
        rule_prefills=[questionnaire_question_answer_rule_prefill_from_business(rule) for rule in answer.rule_prefills] if answer.rule_prefills else [],
        created_at=answer.createdat,
        updated_at=answer.updatedat,
    )


def questionnaire_question_answer_rule_prefill_from_business(rule: QuestionnaireQuestionAnswerRulePrefill) -> TemplatebackendQuestionnaireQuestionAnswerRulePrefill:
    return TemplatebackendQuestionnaireQuestionAnswerRulePrefill(
        id=rule.id,
        questionid=rule.questionid,
        answerid=rule.answerid,
        answer_text=rule.answer_text,
        created_at=rule.createdat,
        updated_at=rule.updatedat,
    )

def questionnaire_to_business(questionnaire: TemplatebackendQuestionnaire) -> Questionnaire:
    return Questionnaire(
        id=questionnaire.id,
        name=questionnaire.name,
        reply_editable=questionnaire.reply_editable,
        versions=[questionnaire_version_to_business(version) for version in questionnaire.versions] if questionnaire.versions else [],
        createdat=questionnaire.created_at,
        updatedat=questionnaire.updated_at,
    )

def questionnaire_version_to_business(version: TemplatebackendQuestionnaireVersion) -> QuestionnaireVersion:
    return QuestionnaireVersion(
        id=version.id,
        version=version.version,
        questions=[questionnaire_question_to_business(question) for question in version.questions] if version.questions else [],
        createdat=version.created_at,
        updatedat=version.updated_at,
    )

def questionnaire_question_to_business(question: TemplatebackendQuestionnaireQuestion) -> QuestionnaireQuestion:
    return QuestionnaireQuestion(
        id=question.id,
        tab=question.tab,
        question=question.question,
        risk_weight=question.risk_weight,
        answer_type=question.answer_type,
        flag=question.flag,
        tooltip=question.tooltip,
        answers=[questionnaire_question_answer_to_business(answer) for answer in question.answers] if question.answers else [],
        createdat=question.created_at,
        updatedat=question.updated_at,
    )

def questionnaire_question_answer_to_business(answer: TemplatebackendQuestionnaireQuestionAnswer) -> QuestionnaireQuestionAnswer:
    return QuestionnaireQuestionAnswer(
        id=answer.id,
        text=answer.text,
        risk_level=answer.risk_level,
        rule_prefills=[questionnaire_question_answer_rule_prefill_to_business(rule) for rule in answer.rule_prefills] if answer.rule_prefills else [],
        createdat=answer.created_at,
        updatedat=answer.updated_at,
    )

def questionnaire_question_answer_rule_prefill_to_business(rule: TemplatebackendQuestionnaireQuestionAnswerRulePrefill) -> QuestionnaireQuestionAnswerRulePrefill:
    return QuestionnaireQuestionAnswerRulePrefill(
        id=rule.id,
        questionid=rule.questionid,
        answerid=rule.answerid,
        answer_text=rule.answer_text,
        createdat=rule.created_at,
        updatedat=rule.updated_at,
    )
