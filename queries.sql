"""CREATE TABLE employers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL
    )""")
    conn.commit()  # Создание бд компании и вакансии

"""CREATE TABLE vacancies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    salary varchar(255) ,
    url VARCHAR(255) NOT NULL,
    employer_id INTEGER NOT NULL,
    FOREIGN KEY (employer_id) REFERENCES employers (id)
    )""")
        conn.commit()

"""INSERT INTO employers (name, url) VALUES (%s, %s) RETURNING id""", (name, url)) # заполнение таблиц компании

"""INSERT INTO vacancies (name, salary, url, employer_id) VALUES (%s, %s, %s, %s)""", (name, None, url, employer_id) # заполнение таблиц вакансии по параметрам

"""SELECT employers.name, COUNT(vacancies.id) FROM employers LEFT JOIN vacancies ON employers.id = vacancies.employer_id
            GROUP BY employers.name""" # количество вакансий у компаний

"""SELECT  employers.name, vacancies.name, vacancies.salary, vacancies.url
            FROM vacancies
            INNER JOIN employers ON vacancies.employer_id = employer_id """ # функция вывода компании вакансий зп и ссылке

"""SELECT AVG(CAST(salary AS numeric)) FROM vacancies""" # функция поиска средней зп

"""SELECT AVG(CAST(salary AS numeric)) FROM vacancies"""
"""SELECT * FROM vacancies WHERE CAST(salary AS numeric) > {avg_salary}""") # поиск вакансии по средней зп и фильтрации выше нее

"""SELECT * FROM vacancies WHERE name LIKE 'Python%';""" # поиск вакансии с фильтром по слову

 """DROP TABLE vacancies,employers""" # функция для перезапуска без удаления бд в редакторе бд