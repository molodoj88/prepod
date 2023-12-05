import json


def get_classes_by_teacher(teacher_name, day_of_week, dictionary):
    teacher_schedule = dictionary.get(teacher_name, None)
    if teacher_schedule is None:
        return None
    return teacher_schedule.get(day_of_week, None)


def get_schedule_by_class(class_name, day_of_week, dictionary):
    new_dict = {}
    for teacher_name, teacher_schedule in dictionary.items():
        day_schedule = teacher_schedule.get(day_of_week, None)
        if day_schedule is None:
            continue
        for k, v in day_schedule.items():
            if v["аудитория"] == class_name:
                new_dict[k] = {"преподаватель": teacher_name, "предмет": v["предмет"]}
    return new_dict


def main():
    file_path = "prepod.json"
    with open(file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    dictionary = dict(json_data)
    print(get_classes_by_teacher("Иванов Иван Иванович", "понедельник", dictionary))
    print(get_schedule_by_class("101", "понедельник", dictionary))


if __name__ == "__main__":
    main()
