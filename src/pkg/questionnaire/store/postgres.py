from sqlalchemy import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from contextlib import contextmanager
from src.pkg.questionnaire.model.questionnaire import Questionnaire
from src.pkg.questionnaire.model.questionnaire import QuestionnaireVersion
from src.pkg.questionnaire.model.questionnaire import QuestionnaireQuestion
from src.pkg.questionnaire.model.questionnaire import QuestionnaireQuestionAnswer
from src.pkg.questionnaire.model.questionnaire import QuestionnaireQuestionAnswerRulePrefill
from src.pkg.questionnaire.model.questionnaire import Reply
from src.pkg.questionnaire.model.questionnaire import QuestionReply


class QuestionnaireStore:
    def __init__(self, db: Engine):
        self.db = db

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        Session = sessionmaker(bind=self.db)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_questionnaire(self, questionnaire: Questionnaire) -> Questionnaire:
        questionnaire_query = """
        INSERT INTO questionnaires 
            (userid, tenantid, name, reply_editable, createdat, updatedat) 
        VALUES 
            (:userid, :tenantid, :name, COALESCE(:reply_editable, FALSE), now(), now()) 
        RETURNING id;
        """

        with self.session_scope() as session:
            try:
                # Insert questionnaire
                result = session.execute(text(questionnaire_query), {
                    'userid': questionnaire.userid,
                    'tenantid': questionnaire.tenantid,
                    'name': questionnaire.name,
                    'reply_editable': questionnaire.reply_editable
                }).fetchone()
                questionnaire_id = result[0]
                
                if questionnaire.versions is not None:
                    for version in questionnaire.versions:
                        self.create_questionnaire_version_inner(
                            tenantid=questionnaire.tenantid, userid=questionnaire.userid, 
                            questionnaire_id=questionnaire_id, version=version, 
                            session=session
                        )

            except SQLAlchemyError as e:
                raise e

            return Questionnaire(id=questionnaire_id)
        
    def create_questionnaire_version(self, tenantid: int, userid: int, questionnaire_id: int, version: QuestionnaireVersion) -> QuestionnaireVersion:
        with self.session_scope() as session:
            try:
                res = self.create_questionnaire_version_inner(tenantid, userid, questionnaire_id, version, session)
            except SQLAlchemyError as e:
                raise e
        return res

    def create_questionnaire_version_inner(self, tenantid: int, userid: int, questionnaire_id: int, version: QuestionnaireVersion, session) -> QuestionnaireVersion:
        questionnaires_unpublish_all = """
        UPDATE questionnaire_versions SET
            published=false,
            updatedat=now()
        WHERE
            questionnaireid = :questionnaireid;
        """
        
        questionnaire_version_query = """
        INSERT INTO questionnaire_versions 
            (userid, tenantid, questionnaireid, version, published, createdat, updatedat) 
        VALUES 
            (:userid, :tenantid, :questionnaireid, :version, :published, now(), now()) 
        RETURNING id;
        """

        questionnaire_question_query = """
        INSERT INTO questionnaire_questions 
            (userid, tenantid, questionnaireid, questionnaire_versionid, tab, question, risk_weight, answer_type, flag, tooltip, createdat, updatedat) 
        VALUES 
            (:userid, :tenantid, :questionnaireid, :questionnaire_versionid, :tab, :question, :risk_weight, :answer_type, :flag, :tooltip, now(), now()) 
        RETURNING id;
        """

        questionnaire_answer_query = """
        INSERT INTO questionnaire_question_answers 
            (userid, tenantid, questionnaire_questionid, text, risk_level, high_risk, createdat, updatedat) 
        VALUES 
            (:userid, :tenantid, :questionnaire_questionid, :text, :risk_level, :high_risk, now(), now()) 
        RETURNING id;
        """

        questionnaire_rule_prefill_query = """
        INSERT INTO questionnaire_question_answer_rule_prefills 
            (userid, tenantid, questionnaire_question_answerid, questionid, answerid, answer_text, createdat, updatedat) 
        VALUES 
            (:userid, :tenantid, :questionnaire_question_answerid, :questionid, :answerid, :answer_text, now(), now()) 
        RETURNING id;
        """

        if version.published:
            # first unplish all other versions
            session.execute(text(questionnaires_unpublish_all), {
                'questionnaireid': questionnaire_id,
            })

        # Insert questionnaire version
        result = session.execute(text(questionnaire_version_query), {
            'userid': userid,
            'tenantid': tenantid,
            'questionnaireid': questionnaire_id,
            'published': version.published,
            'version': version.version
        }).fetchone()
        version_id = result[0]

        for question in version.questions:
            # Insert questionnaire question
            result = session.execute(text(questionnaire_question_query), {
                'userid': userid,
                'tenantid': tenantid,
                'questionnaireid': questionnaire_id,
                'questionnaire_versionid': version_id,
                'tab': question.tab,
                'question': question.question,
                'risk_weight': question.risk_weight,
                'answer_type': question.answer_type,
                'flag': question.flag,
                'tooltip': question.tooltip
            }).fetchone()
            question_id = result[0]

            for answer in question.answers:
                # Insert questionnaire question answer
                result = session.execute(text(questionnaire_answer_query), {
                    'userid': userid,
                    'tenantid': tenantid,
                    'questionnaire_questionid': question_id,
                    'text': answer.text,
                    'risk_level': answer.risk_level,
                    'high_risk': answer.high_risk
                }).fetchone()
                answer_id = result[0]

                for rule_prefill in answer.rule_prefills:
                    # Insert questionnaire question answer rule prefill
                    session.execute(text(questionnaire_rule_prefill_query), {
                        'userid': userid,
                        'tenantid': tenantid,
                        'questionnaire_question_answerid': answer_id,
                        'questionid': rule_prefill.questionid,
                        'answerid': rule_prefill.answerid,
                        'answer_text': rule_prefill.answer_text
                    })

        return QuestionnaireVersion(id=version_id)
        
    def create_reply(self, tenantid: int, userid: int, reply: Reply) -> Reply:
        questionnaire_reply_query = """
        INSERT INTO questionnaire_replies 
            (project_name, userid, tenantid, questionnaire_versionid, questionnaireid, createdat, updatedat) 
        VALUES 
            (:project_name, :userid, :tenantid, :questionnaire_versionid, (select questionnaireid from questionnaire_versions where id = :questionnaire_versionid), now(), now()) 
        RETURNING id;
        """

        questionnaire_question_reply_query = """
        INSERT INTO questionnaire_question_reply 
            (replyid, userid, tenantid, questionnaire_versionid, questionnaire_questionid, questionnaireid, answer, createdat, updatedat) 
        VALUES 
            (:replyid, :userid, :tenantid, :questionnaire_versionid, :questionnaire_questionid, (select questionnaireid from questionnaire_versions where id = :questionnaire_versionid), :answer, now(), now()) 
        RETURNING id;
        """

        with self.session_scope() as session:
            try:
                result = session.execute(text(questionnaire_reply_query), {
                    'project_name': reply.project_name,
                    'userid': userid,
                    'tenantid': tenantid,
                    'questionnaire_versionid': reply.questionnaire_version_id
                }).fetchone()
                reply_id = result[0]

                for question_reply in reply.replies:
                    session.execute(text(questionnaire_question_reply_query), {
                        'replyid': reply_id,
                        'userid': userid,
                        'tenantid': tenantid,
                        'questionnaire_versionid': reply.questionnaire_version_id,
                        'questionnaire_questionid': question_reply.questionnaire_question_id,
                        'answer': question_reply.answer
                    })

            except SQLAlchemyError as e:
                raise e

            return Reply(
                id=reply_id
            )
    
    def get_reply(self, tenantid: int, userid: int, reply_id: int) -> Reply:
        reply_query = """
        SELECT id, userid, tenantid, project_name, questionnaire_versionid, createdat, updatedat, deletedat
        FROM questionnaire_replies
        WHERE id = :reply_id and deletedat is null;
        """

        question_reply_query = """
        SELECT id, userid, tenantid, questionnaire_questionid, answer, createdat, updatedat, deletedat
        FROM questionnaire_question_reply
        WHERE replyid = :reply_id;
        """

        with self.session_scope() as session:
            try:
                result = session.execute(text(reply_query), {'reply_id': reply_id}).mappings().fetchone()
                if not result:
                    return None  

                reply = Reply(
                    id=result['id'],
                    userid=result['userid'],
                    tenantid=result['tenantid'],
                    project_name=result['project_name'],
                    questionnaire_version_id=result['questionnaire_versionid'],
                    createdat=result['createdat'],
                    updatedat=result['updatedat'],
                    deletedat=result['deletedat'],
                    replies=[]
                )

                question_reply_results = session.execute(text(question_reply_query), {'reply_id': reply.id}).mappings().fetchall()
                for question_reply_row in question_reply_results:
                    question_reply = QuestionReply(
                        id=question_reply_row['id'],
                        userid=question_reply_row['userid'],
                        tenantid=question_reply_row['tenantid'],
                        questionnaire_question_id=question_reply_row['questionnaire_questionid'],
                        answer=question_reply_row['answer'],
                        createdat=question_reply_row['createdat'],
                        updatedat=question_reply_row['updatedat'],
                        deletedat=question_reply_row['deletedat']
                    )
                    reply.replies.append(question_reply)

            except SQLAlchemyError as e:
                raise e

            return reply
    
    def list_replies(self, tenantid: int, userid: int, offset: int, limit: int) -> list[Reply]:
        reply_query = """
        SELECT id, userid, tenantid, project_name, questionnaire_versionid, createdat, updatedat, deletedat
        FROM questionnaire_replies
        WHERE userid = :userid and deletedat is null
        OFFSET :offset
        LIMIT :limit;
        """

        with self.session_scope() as session:
            try:
                results = session.execute(text(reply_query), {
                    'userid': userid,
                    'offset': offset,
                    'limit': limit,
                }).mappings().fetchall()

                replies = [
                    Reply(
                        id=result['id'],
                        userid=result['userid'],
                        tenantid=result['tenantid'],
                        project_name=result['project_name'],
                        questionnaire_version_id=result['questionnaire_versionid'],
                        createdat=result['createdat'],
                        updatedat=result['updatedat'],
                        deletedat=result['deletedat'],
                        replies=[]
                    ) for result in results
                ]

            except SQLAlchemyError as e:
                raise e

            return replies

        
    def get_questionnaire(self, tenantid: int, userid: int, questionnaire_id: int) -> Questionnaire:
        questionnaire_query = """
        SELECT id, userid, tenantid, name, reply_editable, createdat, updatedat, deletedat
        FROM questionnaires
        WHERE id = :questionnaire_id and deletedat is null;
        """

        questionnaire_version_query = """
        SELECT id, version, published, createdat, updatedat, deletedat
        FROM questionnaire_versions
        WHERE questionnaireid = :questionnaire_id  and deletedat is null
        ORDER BY createdat DESC;
        """

        questionnaire_question_query = """
        SELECT id, tab, question, risk_weight, answer_type, flag, tooltip, createdat, updatedat, deletedat
        FROM questionnaire_questions
        WHERE questionnaireid = :questionnaire_id AND questionnaire_versionid = :version_id;
        """

        questionnaire_answer_query = """
        SELECT id, text, risk_level, high_risk, createdat, updatedat, deletedat
        FROM questionnaire_question_answers
        WHERE questionnaire_questionid = :question_id;
        """

        questionnaire_rule_prefill_query = """
        SELECT id, questionid, answerid, answer_text, createdat, updatedat, deletedat
        FROM questionnaire_question_answer_rule_prefills
        WHERE questionnaire_question_answerid = :answer_id;
        """

        with self.session_scope() as session:
            try:
                # Fetch the questionnaire
                result = session.execute(text(questionnaire_query), {'questionnaire_id': questionnaire_id}).mappings().fetchone()
                if not result:
                    return None  # or raise an exception if you prefer

                questionnaire = Questionnaire(
                    id=result['id'],
                    userid=result['userid'],
                    tenantid=result['tenantid'],
                    name=result['name'],
                    reply_editable=result['reply_editable'],
                    createdat=result['createdat'],
                    updatedat=result['updatedat'],
                    deletedat=result['deletedat'],
                    versions=[]
                )

                # Fetch the versions
                version_results = session.execute(text(questionnaire_version_query), {'questionnaire_id': questionnaire_id}).mappings().fetchall()
                for version_row in version_results:
                    version = QuestionnaireVersion(
                        id=version_row['id'],
                        version=version_row['version'],
                        published=version_row['published'],
                        createdat=version_row['createdat'],
                        updatedat=version_row['updatedat'],
                        deletedat=version_row['deletedat'],
                        questions=[]
                    )

                    # Fetch the questions for this version
                    question_results = session.execute(text(questionnaire_question_query), {'questionnaire_id': questionnaire_id, 'version_id': version.id}).mappings().fetchall()
                    for question_row in question_results:
                        question = QuestionnaireQuestion(
                            id=question_row['id'],
                            tab=question_row['tab'],
                            question=question_row['question'],
                            risk_weight=question_row['risk_weight'],
                            answer_type=question_row['answer_type'],
                            flag=question_row['flag'],
                            tooltip=question_row['tooltip'],
                            createdat=question_row['createdat'],
                            updatedat=question_row['updatedat'],
                            deletedat=question_row['deletedat'],
                            answers=[]
                        )

                        # Fetch the answers for this question
                        answer_results = session.execute(text(questionnaire_answer_query), {'question_id': question.id}).mappings().fetchall()
                        for answer_row in answer_results:
                            answer = QuestionnaireQuestionAnswer(
                                id=answer_row['id'],
                                text=answer_row['text'],
                                risk_level=answer_row['risk_level'],
                                high_risk=answer_row['high_risk'],
                                createdat=answer_row['createdat'],
                                updatedat=answer_row['updatedat'],
                                deletedat=answer_row['deletedat'],
                                rule_prefills=[]
                            )

                            # Fetch the rule prefills for this answer
                            rule_prefill_results = session.execute(text(questionnaire_rule_prefill_query), {'answer_id': answer.id}).mappings().fetchall()
                            for rule_prefill_row in rule_prefill_results:
                                rule_prefill = QuestionnaireQuestionAnswerRulePrefill(
                                    id=rule_prefill_row['id'],
                                    questionid=rule_prefill_row['questionid'],
                                    answerid=rule_prefill_row['answerid'],
                                    answer_text=rule_prefill_row['answer_text'],
                                    createdat=rule_prefill_row['createdat'],
                                    updatedat=rule_prefill_row['updatedat'],
                                    deletedat=rule_prefill_row['deletedat']
                                )
                                answer.rule_prefills.append(rule_prefill)

                            question.answers.append(answer)
                        version.questions.append(question)
                    questionnaire.versions.append(version)

            except SQLAlchemyError as e:
                raise e

            return questionnaire

    def list_questionnaires(self, tenantid: int, userid: int, offset: int = 0, limit: int = None) -> list[Questionnaire]:
        questionnaire_query = """
        SELECT 
            q.id, 
            q.userid, 
            q.tenantid, 
            q.name, 
            q.reply_editable, 
            q.createdat, 
            q.updatedat, 
            q.deletedat,
            v.version as last_version
        FROM 
            questionnaires q
        LEFT JOIN (
            SELECT 
                questionnaireid, 
                MAX(id) AS max_version_id
            FROM 
                questionnaire_versions
            WHERE 
                deletedat IS NULL
            GROUP BY 
                questionnaireid
        ) subq ON q.id = subq.questionnaireid
        LEFT JOIN 
            questionnaire_versions v ON subq.max_version_id = v.id
        WHERE
            q.deletedat is null
        OFFSET 
            :offset 
        LIMIT 
            :limit;
        """


        with self.session_scope() as session:
            try:
                # Fetch the questionnaire
                results = session.execute(text(questionnaire_query), {'offset': offset, 'limit': limit}).mappings().fetchall()
                if not results:
                    return None  # or raise an exception if you prefer

                questionnaires = [
                    Questionnaire(
                        id=result['id'],
                        userid=result['userid'],
                        tenantid=result['tenantid'],
                        name=result['name'],
                        reply_editable=result['reply_editable'],
                        createdat=result['createdat'],
                        updatedat=result['updatedat'],
                        deletedat=result['deletedat'],
                        versions=[],
                        last_version=result['last_version'],
                    ) for result in results
                ]

                # # Fetch the versions
                # version_results = session.execute(text(questionnaire_version_query), {'questionnaire_id': questionnaire_id}).mappings().fetchall()
                # for version_row in version_results:
                #     version = QuestionnaireVersion(
                #         id=version_row['id'],
                #         version=version_row['version'],
                #         published=version_row['published'],
                #         createdat=version_row['createdat'],
                #         updatedat=version_row['updatedat'],
                #         deletedat=version_row['deletedat'],
                #         questions=[]
                #     )

                #     # Fetch the questions for this version
                #     question_results = session.execute(text(questionnaire_question_query), {'questionnaire_id': questionnaire_id, 'version_id': version.id}).mappings().fetchall()
                #     for question_row in question_results:
                #         question = QuestionnaireQuestion(
                #             id=question_row['id'],
                #             tab=question_row['tab'],
                #             question=question_row['question'],
                #             risk_weight=question_row['risk_weight'],
                #             answer_type=question_row['answer_type'],
                #             flag=question_row['flag'],
                #             tooltip=question_row['tooltip'],
                #             createdat=question_row['createdat'],
                #             updatedat=question_row['updatedat'],
                #             deletedat=question_row['deletedat'],
                #             answers=[]
                #         )

                #         # Fetch the answers for this question
                #         answer_results = session.execute(text(questionnaire_answer_query), {'question_id': question.id}).mappings().fetchall()
                #         for answer_row in answer_results:
                #             answer = QuestionnaireQuestionAnswer(
                #                 id=answer_row['id'],
                #                 text=answer_row['text'],
                #                 risk_level=answer_row['risk_level'],
                #                 createdat=answer_row['createdat'],
                #                 updatedat=answer_row['updatedat'],
                #                 deletedat=answer_row['deletedat'],
                #                 rule_prefills=[]
                #             )

                #             # Fetch the rule prefills for this answer
                #             rule_prefill_results = session.execute(text(questionnaire_rule_prefill_query), {'answer_id': answer.id}).mappings().fetchall()
                #             for rule_prefill_row in rule_prefill_results:
                #                 rule_prefill = QuestionnaireQuestionAnswerRulePrefill(
                #                     id=rule_prefill_row['id'],
                #                     questionid=rule_prefill_row['questionid'],
                #                     answerid=rule_prefill_row['answerid'],
                #                     answer_text=rule_prefill_row['answer_text'],
                #                     createdat=rule_prefill_row['createdat'],
                #                     updatedat=rule_prefill_row['updatedat'],
                #                     deletedat=rule_prefill_row['deletedat']
                #                 )
                #                 answer.rule_prefills.append(rule_prefill)

                #             question.answers.append(answer)
                #         version.questions.append(question)
                #     questionnaire.versions.append(version)

            except SQLAlchemyError as e:
                raise e

            return questionnaires