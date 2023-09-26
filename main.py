import csv
import os

from src.get_data import HeadHunterAPI
from src.DBManager import DBManager


def main():
    # Instantiate the HeadHunterAPI class
    vac = HeadHunterAPI()

    # Populate data from "employers.csv" file
    vac.instantiate_from_csv("employers.csv")

    # Create a PostgreSQL database named "test" and save data to it
    vac.create_database("test")
    vac.save_data_to_database("test")

    # Create a DBManager instance to interact with the database
    db_manager = DBManager("test")

    while True:
        print("\nEnter your query of interest:\n"
              "1 - Display all selected companies:\n"
              "2 - Display the number of vacancies for each company:\n"
              "3 - Display the average salary across companies:\n"
              "4 - Display vacancies with salaries higher than the average:\n"
              "5 - Display vacancies with a specific keyword filter:\n"
              "Type 'exit' to quit:\n")

        inp = input()
        try:
            if inp == "1":
                # Display all selected companies from the CSV file
                csvfile = open(os.path.join(os.path.dirname(__file__), "src/employers.csv"), encoding="utf-8", newline='')
                data = csv.DictReader(csvfile)
                for row in data:
                    print(row['Employer'])
                csvfile.close()
            elif inp == "2":
                # Display the number of vacancies for each company
                for i in db_manager.get_companies_and_vacancies_count():
                    print(f"Company: {i[0]}\nNumber of vacancies: {i[1]},")
            elif inp == "3":
                # Display the average salary across companies
                print(f"Average salary: {round(db_manager.get_avg_salary())}")
            elif inp == "4":
                # Display vacancies with salaries higher than the average
                for i in db_manager.get_vacancies_with_higher_salary():
                    print(f"Vacancy: {i[0]} {i[2]}\nSalary: {i[5]},")
            elif inp == "5":
                # Display vacancies with a specific keyword filter
                print("Enter a keyword to search for:")
                a = input()
                print(f"Searching for vacancies containing the word: {a}")
                for i in db_manager.get_vacancies_with_keyword(a):
                    print(f"Vacancy: {i[0]} {i[2]}\nVacancy link: {i[8]},")
            else:
                print("Invalid choice")
        finally:
            if inp == "exit":
                print("Work completed")
                break

    # Close the database connection
    db_manager.close()


if __name__ == '__main__':
    main()
