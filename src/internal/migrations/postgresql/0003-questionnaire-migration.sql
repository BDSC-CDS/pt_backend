CREATE TABLE IF NOT EXISTS questionnaires (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    tenantid INT NOT NULL,

    name TEXT NOT NULL,
    reply_editable BOOLEAN NOT NULL DEFAULT FALSE,


    createdat TIMESTAMP NOT NULL DEFAULT now(),
    updatedat TIMESTAMP NOT NULL DEFAULT now(),
    deletedat TIMESTAMP,


    CONSTRAINT questionnaire_user_fk FOREIGN KEY (userid) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS questionnaire_versions (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    tenantid INT NOT NULL,

    questionnaireid INT NOT NULL,
    version TEXT UNIQUE NOT NULL,

    createdat TIMESTAMP NOT NULL DEFAULT now(),
    updatedat TIMESTAMP NOT NULL DEFAULT now(),
    deletedat TIMESTAMP,


    CONSTRAINT questionnaire_versions_user_fk FOREIGN KEY (userid) REFERENCES users(id),
    CONSTRAINT questionnaire_versions_questionnaire_fk FOREIGN KEY (questionnaireid) REFERENCES questionnaires(id)
);

CREATE TABLE IF NOT EXISTS questionnaire_questions (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    tenantid INT NOT NULL,

    questionnaireid INT NOT NULL,
    questionnaire_versionid INT NOT NULL,

    tab TEXT NOT NULL,
    question TEXT NOT NULL,
    risk_weight INT NOT NULL,
    answer_type TEXT NOT NULL,
    flag TEXT NOT NULL,
    tooltip TEXT NOT NULL,

    createdat TIMESTAMP NOT NULL DEFAULT now(),
    updatedat TIMESTAMP NOT NULL DEFAULT now(),
    deletedat TIMESTAMP,


    CONSTRAINT questionnaire_questions_user_fk FOREIGN KEY (userid) REFERENCES users(id),
    CONSTRAINT questionnaire_questions_questionnaire_fk FOREIGN KEY (questionnaireid) REFERENCES questionnaires(id),
    CONSTRAINT questionnaire_questions_questionnaire_version_fk FOREIGN KEY (questionnaire_versionid) REFERENCES questionnaire_versions(id)
);

CREATE TABLE IF NOT EXISTS questionnaire_question_answers (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    tenantid INT NOT NULL,

    questionnaire_questionid INT NOT NULL,

    text TEXT NOT NULL,
    risk_level INT NOT NULL,

    createdat TIMESTAMP NOT NULL DEFAULT now(),
    updatedat TIMESTAMP NOT NULL DEFAULT now(),
    deletedat TIMESTAMP,


    CONSTRAINT questionnaire_question_answer_user_fk FOREIGN KEY (userid) REFERENCES users(id),
    CONSTRAINT questionnaire_question_answer_question_fk FOREIGN KEY (questionnaire_questionid) REFERENCES questionnaire_questions(id)
);

CREATE TABLE IF NOT EXISTS questionnaire_question_answer_rule_prefills (
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    tenantid INT NOT NULL,

    questionnaire_question_answerid INT NOT NULL,

    questionid INT NOT NULL,
    answerid INT,
    answer_text TEXT,

    createdat TIMESTAMP NOT NULL DEFAULT now(),
    updatedat TIMESTAMP NOT NULL DEFAULT now(),
    deletedat TIMESTAMP,

    CONSTRAINT questionnaire_question_answer_rule_prefill_user_fk FOREIGN KEY (userid) REFERENCES users(id),
    CONSTRAINT questionnaire_question_answer_rule_prefill_answer_fk FOREIGN KEY (questionnaire_question_answerid) REFERENCES questionnaire_question_answers(id),
    
    CONSTRAINT questionnaire_question_answer_rule_prefill_question_fk FOREIGN KEY (questionid) REFERENCES questionnaire_questions(id),
    CONSTRAINT questionnaire_question_answer_rule_prefill_selected_answer_fk FOREIGN KEY (answerid) REFERENCES questionnaire_question_answers(id)

);
