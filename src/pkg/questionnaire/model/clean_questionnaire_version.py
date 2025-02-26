import json
import uuid

id_to_uuid_map = {}

def generate_uuid(id: int):
    if id not in id_to_uuid_map:
        id_to_uuid_map[id] = str(uuid.uuid4())
    return id_to_uuid_map[id]
    
def clean_questionnaire(obj: any, in_rule_prefills=False):
    if isinstance(obj, dict):
        if not in_rule_prefills:
            if "id" in obj:
                obj["tmpUUID"] = generate_uuid(obj.pop("id"))
        else:
            obj.pop("id", None)
        if "questionId" in obj:
            obj["tmpQuestionUUID"] = generate_uuid(obj.pop("questionId"))
        if "answerId" in obj:
            obj["tmpAnswerUUID"] = generate_uuid(obj.pop("answerId"))
        obj.pop("createdAt", None)
        obj.pop("updatedAt", None)
        for key, value in obj.items():
            if key == "rulePrefills" and isinstance(value, list):
                obj[key] = [clean_questionnaire(item, True) for item in value]
            else:
                obj[key] = clean_questionnaire(value, in_rule_prefills)
    elif isinstance(obj, list):
        return [clean_questionnaire(item, in_rule_prefills) for item in obj]
    return obj

def write_json_to_file(obj: dict, filename: str):
    with open(filename, "w") as f:
        json.dump(obj, f, indent=2)

def read_json_from_file(filename: str):
    with open(filename) as f:
        obj = json.load(f)
        return obj
    
def main():
    obj = read_json_from_file("questionnaire_v2.1.0.json")
    cleaned_obj = clean_questionnaire(obj)
    # Replace tmpUUID with id in cleaned object
    cleaned_obj.pop("tmpUUID", None)
    cleaned_obj["id"] = 1
    write_json_to_file(cleaned_obj, "cleaned_questionnaire_v2.1.0.json")

if __name__ == "__main__":
    main()