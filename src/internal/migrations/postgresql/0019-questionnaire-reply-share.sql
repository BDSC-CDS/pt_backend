CREATE TABLE public.questionnaire_reply_share (
  id SERIAL PRIMARY KEY,
  questionnairereplyid integer NOT NULL,
  userid integer NOT NULL,
  tenantid integer NOT NULL,
  sharedwith_userid integer NOT NULL,
  share_type TEXT NOT NULL,
  createdat timestamp without time zone NOT NULL,
  updatedat timestamp without time zone NOT NULL,
  deletedat timestamp without time zone NULL,

  CONSTRAINT questionnaire_reply_versions_fk FOREIGN KEY (questionnairereplyid) REFERENCES questionnaire_replies(id),
  CONSTRAINT questionnaire_reply_versions_user_fk FOREIGN KEY (userid) REFERENCES users(id),
  CONSTRAINT questionnaire_reply_versions_sharedwith_user_fk FOREIGN KEY (sharedwith_userid) REFERENCES users(id)

);
