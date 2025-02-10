CREATE TABLE public.questionnaire_reply_versions (
  id SERIAL PRIMARY KEY,
  questionnairereplyid integer NOT NULL,
  userid integer NOT NULL,
  tenantid integer NOT NULL,
  createdat timestamp without time zone NOT NULL,
  updatedat timestamp without time zone NOT NULL,
  deletedat timestamp without time zone NULL,

  CONSTRAINT questionnaire_reply_versions_fk FOREIGN KEY (questionnairereplyid) REFERENCES questionnaire_replies(id)
);

INSERT INTO public.questionnaire_reply_versions
    (id, questionnairereplyid, userid, tenantid, createdat, updatedat, deletedat)
SELECT
    id, id, userid, tenantid, createdat, updatedat, deletedat
FROM public.questionnaire_replies;

-- increment serial id to avoid conflict
SELECT setval('questionnaire_reply_versions_id_seq', (SELECT MAX(id) FROM questionnaire_reply_versions));

ALTER TABLE questionnaire_question_reply DROP CONSTRAINT questionnaire_question_reply_replyid_fk;

ALTER TABLE questionnaire_question_reply
ADD CONSTRAINT questionnaire_question_reply_replyid_fk FOREIGN KEY (replyid) REFERENCES questionnaire_reply_versions(id);