import psycopg2


class DBManager:
    """Class for managing database connection, data retrieval, and filtering."""

    def __init__(self, database_name: str):
        """
        Initialize the DBManager object.

        Args:
            database_name (str): The name of the database.

        """
        self.conn = psycopg2.connect(dbname=database_name, host='localhost', user='postgres', password='PGNWyG')
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """
        Get the number of vacancies for each company.

        Returns:
            list of tuple: A list of tuples where each tuple contains the company name and the number of vacancies.

        """
        self.cur.execute("""
            SELECT employers.title, COUNT(vacancies.vacancy_id)
            FROM employers
            LEFT JOIN vacancies ON employers.employer_id = vacancies.employer_id
            GROUP BY employers.title
        """)
        result = self.cur.fetchall()
        return result

    def get_all_vacancies(self):
        """
        Get all vacancies with information about the company, vacancy title, salary, and URL.

        Returns:
            list of dict: A list of dictionaries where each dictionary represents information about a vacancy.

        """
        self.cur.execute("""
            SELECT employers.title, vacancies.title, vacancies.salary, vacancies.url
            FROM vacancies
            INNER JOIN employers ON vacancies.employer_id = employers.employer_id
        """)
        result = self.cur.fetchall()
        vacancies = []
        for row in result:
            vacancy = {
                "employer_name": row[0],
                "vacancy_name": row[1],
                "salary": row[2],
                "url": row[3]
            }
            vacancies.append(vacancy)
        return vacancies

    def get_avg_salary(self):
        """
        Get the average salary across all vacancies.

        Returns:
            float: The average salary.

        """
        self.cur.execute("""
            SELECT AVG(CAST(salary AS numeric))
            FROM vacancies
        """)
        result = self.cur.fetchone()[0]
        return result

    def get_vacancies_with_higher_salary(self):
        """
        Get vacancies with a salary higher than the average salary.

        Returns:
            list of tuple: A list of vacancies with salaries higher than the average salary.

        """
        avg_salary = self.get_avg_salary()
        self.cur.execute(f"""
            SELECT *
            FROM vacancies
            WHERE CAST(salary AS numeric) > {avg_salary}
        """)
        result = self.cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, word):
        """
        Get vacancies containing a keyword in their title.

        Args:
            word (str): The keyword to search for.

        Returns:
            list of tuple: A list of vacancies with titles containing the keyword.

        """
        self.cur.execute(f"SELECT * FROM vacancies WHERE title LIKE '%{word}%'")
        result = self.cur.fetchall()
        return result

    def close(self):
        """Close the database connection."""
        self.cur.close()
        self.conn.close()
