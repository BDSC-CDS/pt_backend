ALTER TABLE questionnaire_versions
ADD COLUMN published BOOLEAN default false;

ALTER TABLE questionnaire_replies
ADD COLUMN project_name TEXT default '';

ALTER TABLE questionnaire_question_reply
ADD COLUMN replyid INT NOT NULL;

ALTER TABLE questionnaire_question_reply
ADD CONSTRAINT questionnaire_question_reply_replyid_fk FOREIGN KEY (replyid) REFERENCES questionnaire_replies(id);