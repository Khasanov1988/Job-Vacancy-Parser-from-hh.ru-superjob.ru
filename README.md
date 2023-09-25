# Job Vacancy Parser from hh.ru & superjob.ru

"Job Vacancy Parser from hh.ru & superjob.ru" is a Python project that interacts with the HeadHunter.ru and SuperJob.ru
APIs to collect data about employers and vacancies, stores this data in a PostgreSQL database, and provides various query
options for analyzing the collected information.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
    - [Data Collection](#data-collection)
    - [Database Setup](#database-setup)
    - [Query Options](#query-options)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- PostgreSQL database server installed and running
- [Requests library](https://pypi.org/project/requests/) installed (`pip install requests`)
- [Psycopg2 library](https://pypi.org/project/psycopg2/) installed (`pip install psycopg2`)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Khasanov1988/Job-Vacancy-Parser-from-hh.ru-superjob.ru.git
   ```

2. Navigate to the project directory:

   ```bash
   cd src
   ```

## Usage

### Data Collection

**Data Collection from HeadHunter API**

   To collect data from the HeadHunter and SuperJob APIs, you need to run the `main.py` script. This script interacts with the
   HeadHunter and SuperJob APIs and take information about employers a CSV file (`employers.csv` in this case).

   ```bash
   python main.py
   ```

### Query Options

After collecting and storing data, you can perform various queries and analysis using the `main.py` script.

1. **Display All Selected Companies**

   To display all selected companies from the CSV file, push "1" in main menu

2. **Display the Number of Vacancies for Each Company**

   To display the number of vacancies for each company, push "2" in main menu

3. **Display the Average Salary Across Companies**

   To display the average salary across companies, push "3" in main menu

4. **Display Vacancies with Salaries Higher Than the Average**

   To display vacancies with salaries higher than the average, push "4" in main menu

5. **Display Vacancies with a Specific Keyword Filter**

   To display vacancies with a specific keyword filter, push "5" in main menu and then tipe Specific Keyword

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Description of your changes'`
4. Push your changes to your forked repository: `git push origin feature-name`
5. Create a pull request.

## License

This project is licensed under the MIT License