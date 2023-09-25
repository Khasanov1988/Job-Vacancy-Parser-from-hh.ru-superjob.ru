from abc import ABC, abstractmethod
import json

from src.vacancies import Vacancy  # Assuming you have a Vacancy class in your 'src' module


class VacancyError(Exception):
    """Custom exception for vacancy-related errors."""

    def __str__(self):
        return 'The object used is not an instance of the Vacancy class.'


class JsonAbs(ABC):
    @abstractmethod
    def save_to_json(self):
        """Save to a JSON file."""
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_min, salary_max):
        """Get vacancies within a salary range."""
        pass

    @abstractmethod
    def delete_vacancy(self, id):
        """Delete a vacancy from the file."""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Add a vacancy."""
        pass

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Print a dictionary in a JSON-like format with indentation."""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class JSONSaver(JsonAbs):
    def __init__(self, data: list):
        self.data = data

    def save_to_json(self):
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file)

    def get_vacancies_by_salary(self, salary_min: int, salary_max: int):
        answer = []
        for vacancy in self.data:
            if isinstance(vacancy["salary_from"], int) and salary_min <= vacancy["salary_from"] <= salary_max:
                answer.append(vacancy)
            elif isinstance(vacancy["salary_to"], int) and salary_min <= vacancy["salary_to"] <= salary_max:
                answer.append(vacancy)
        return answer

    def delete_vacancy(self, vacancy_id: int):
        file = open('data.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        del_dict = None
        for i in range(len(data)):
            if data[i]["id"] == vacancy_id:
                del_dict = data[i]
        if del_dict is None:
            print("There is no vacancy with this id in the list of vacancies.")
        else:
            data.remove(del_dict)
        self.data = data
        file = open('data.json', 'w', encoding='utf-8')
        json.dump(data, file)
        file.close()

    def add_vacancy(self, vacancy):
        if isinstance(vacancy, Vacancy):
            entry = {
                "source": vacancy.source,
                "id": vacancy.id,
                "title": vacancy.title,
                "client": vacancy.employer,
                "link": vacancy.link,
                "area": vacancy.area,
                "salary_from": vacancy.salary_from,
                "salary_to": vacancy.salary_to,
                "salary_currency": vacancy.salary_currency
            }
            file = open('data.json', 'r', encoding='utf-8')
            data = json.load(file)
            file.close()
            data.append(entry)
            self.data = data
            file = open('data.json', 'w', encoding='utf-8')
            json.dump(data, file)
            file.close()
        else:
            raise VacancyError
