ALTER TABLE questionnaire_question_answers
ADD COLUMN default_answer BOOLEAN 
NOT NULL DEFAULT FALSE;
