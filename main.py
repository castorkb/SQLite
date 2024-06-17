import sqlite3 as sq
'''1'''

# with sq.connect('practice_1.db') as con:
#     cur = con.cursor()
#
#     # cur.execute("DROP TABLE IF EXISTS Manufacturers") # Удаление таблицы при необходимости
#     # cur.execute("DROP TABLE IF EXISTS Brands") # Удаление таблицы при необходимости
#     # cur.execute("DROP TABLE IF EXISTS Cars") # Удаление таблицы при необходимости
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS Manufacturers (
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Name TEXT NOT NULL
#     )""")  # Создаем таблицу Manufacturers и столбцы
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS Brands (
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Name TEXT NOT NULL,
#     Manufacturer TEXT NOT NULL
#     )""")  # Создаем таблицу Brands и столбцы
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS Cars (
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Model TEXT NOT NULL,
#     Brand TEXT NOT NULL,
#     Year INTEGER NOT NULL,
#     Price REAL NOT NULL
#     )""")  # Создаем таблицу Cars и столбцы
#
#
#
#
#     cur.execute("INSERT INTO Manufacturers (Name) VALUES"
#                 " ('Toyota'), "
#                 "('Ford'), "
#                 "('BMW')")  # Вставка данных в таблицу Manufacturers
#
#     cur.execute("INSERT INTO Brands (Name, Manufacturer) VALUES "
#                 "('Camry', 'Toyota'), "
#                 "('Mustang', 'Ford'), "
#                 "('Series 3', 'BMW')")  # Вставка данных в таблицу Brands
#
#     cur.execute("""INSERT INTO Cars (Model, Brand, Year, Price) VALUES
#     ('Camry LE', 'Camry', 2020, 24000),
#     ('Camry SE', 'Camry', 2021, 26000),
#     ('Mustang GT', 'Mustang', 2019, 36000),
#     ('Mustang EcoBoost', 'Mustang', 2020, 32000),
#     ('Series 3 Sedan', 'Series 3', 2020, 41000),
#     ('Series 3 Coupe', 'Series 3', 2021, 45000)""")  # Вставка данных в таблицу Cars
#
#
#
#
#     # 1. Найти все автомобили марки "Mustang"

#     cur.execute("SELECT * FROM Cars WHERE Brand = 'Mustang'")
#     mustang_cars = cur.fetchall()
#     print("Машины Mustang:")
#     for car in mustang_cars:
#         print(car)
#
#
#
#
#     # 2. Обновить цену для определенной модели

#     cur.execute("UPDATE Cars SET Price = 27000.00 WHERE Model = 'Camry SE' AND Year = 2021")
#     con.commit()
#
#
#
#
#     # 3. Удалить устаревшие модели

#     cur.execute("DELETE FROM Cars WHERE Year < 2010")
#     con.commit()
#
#
#
#     # 4. Подсчитать количество автомобилей каждой марки

#     cur.execute("SELECT Brand, COUNT(*) AS CarCount FROM Cars GROUP BY Brand")
#     brand_counts = cur.fetchall()
#     print("Счет автомобилей по марке:")
#     for count in brand_counts:
#         print(count)
#
#
#
#     # 5. Определить среднюю цену автомобилей каждого производителя

#     cur.execute('''
#     SELECT b.Manufacturer, AVG(c.Price) AS AveragePrice
#     FROM Cars c
#     JOIN Brands b ON c.Brand = b.Name
#     GROUP BY b.Manufacturer
#     ''')
#     average_prices = cur.fetchall()
#     print("Средние цены по производителям:")
#     for price in average_prices:
#         print(price)




'''2'''
#
# #1: Создание Таблиц
#
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#
#     # Создание таблицы Книг
#     cur.execute("""CREATE TABLE IF NOT EXISTS Books (
#         BookID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Title TEXT NOT NULL,
#         Author TEXT NOT NULL,
#         Year INTEGER NOT NULL
#     )""")
#
#     # Создание таблицы Читателей
#     cur.execute("""CREATE TABLE IF NOT EXISTS Readers (
#         ReaderID INTEGER PRIMARY KEY AUTOINCREMENT,
#         FirstName TEXT NOT NULL,
#         LastName TEXT NOT NULL,
#         RegistrationDate DATE NOT NULL
#     )""")
#
#     # Создание таблицы Жанров
#     cur.execute("""CREATE TABLE IF NOT EXISTS Genres (
#         GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
#         GenreName TEXT NOT NULL
#     )""")
#
#     # Создание таблицы Привязки книг к жанрам
#     cur.execute("""CREATE TABLE IF NOT EXISTS BookGenres (
#         BookID INTEGER NOT NULL,
#         GenreID INTEGER NOT NULL,
#         FOREIGN KEY (BookID) REFERENCES Books (BookID),
#         FOREIGN KEY (GenreID) REFERENCES Genres (GenreID)
#     )""")
#
#
# #Вставка Данных
#
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#
#     # Вставка данных в таблицу Books
#     cur.execute("INSERT INTO Books (Title, Author, Year) VALUES "
#                 "('Война и мир', 'Лев Толстой', 1869), "
#                 "('Гордость и предубеждение', 'Джейн Остин', 1813), "
#                 "('1984', 'Джордж Оруэлл', 1949)")
#
#     # Вставка данных в таблицу Readers
#     cur.execute("INSERT INTO Readers (FirstName, LastName, RegistrationDate) VALUES "
#                 "('Иван', 'Матюшин', '2021-01-15'), "
#                 "('Петр', 'Вальдемаров', '2022-06-23'), "
#                 "('Элиза', 'Темирбекова', '2023-03-19')")
#
#     # Вставка данных в таблицу Genres
#     cur.execute("INSERT INTO Genres (GenreName) VALUES "
#                 "('Историческая беллетристика'), "
#                 "('Романс'), "
#                 "('Антиутопический')")
#
#     # Вставка данных в таблицу BookGenres
#     cur.execute("INSERT INTO BookGenres (BookID, GenreID) VALUES "
#                 "(1, 1), "
#                 "(2, 2), "
#                 "(3, 3)")
#
#
# # 3: Выборка Данных с Условиями
#
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#
#     # Выборка всех книг, изданных до 1870 года
#     cur.execute("SELECT * FROM Books WHERE Year < 1870")
#     old_books = cur.fetchall()
#     print("Книги, изданные до 1870 года:")
#     for book in old_books:
#         print(book)
#
#     # Выборка всех книг определённого жанра (например, Romance)
#     genre = 'Romance'
#     cur.execute("""
#         SELECT Books.*
#         FROM Books
#         JOIN BookGenres ON Books.BookID = BookGenres.BookID
#         JOIN Genres ON BookGenres.GenreID = Genres.GenreID
#         WHERE Genres.GenreName = ?
#     """, (genre,))
#     romance_books = cur.fetchall()
#     print(f"Книги жанра {genre}:")
#     for book in romance_books:
#         print(book)
#
#     # Выборка всех читателей, зарегистрированных после определённой даты
#     date = '2022-01-01'
#     cur.execute("SELECT * FROM Readers WHERE RegistrationDate > ?", (date,))
#     recent_readers = cur.fetchall()
#     print(f"Читатели, зарегистрированные после {date}:")
#     for reader in recent_readers:
#         print(reader)
#
#
# #4: Объединение и Пересечение
#
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#
#     # Пример использования INTERSECT
#     cur.execute("""
#         SELECT Books.Title
#         FROM Books
#         JOIN BookGenres ON Books.BookID = BookGenres.BookID
#         INTERSECT
#         SELECT Books.Title
#         FROM Books
#         JOIN Readers ON Readers.ReaderID = Books.BookID
#     """)
#     intersect_books = cur.fetchall()
#     print("Книги, которые читались читателями:")
#     for book in intersect_books:
#         print(book)
#
#     # Пример использования UNION ALL
#     cur.execute("""
#         SELECT Title FROM Books
#         UNION ALL
#         SELECT Title FROM Books WHERE Year > 1900
#     """)
#     union_books = cur.fetchall()
#     print("Объединение всех книг с книгами, изданными после 1900 года:")
#     for book in union_books:
#         print(book)
#
#
# #5: Группировка и Агрегация
#
# with sq.connect('library.db') as con:
#     cur = con.cursor()
#
#     # Подсчёт количества книг, написанных каждым автором
#     cur.execute("SELECT Author, COUNT(*) AS BookCount FROM Books GROUP BY Author")
#     author_counts = cur.fetchall()
#     print("Количество книг по каждому автору:")
#     for count in author_counts:
#         print(count)
#
#     # Подсчёт общего числа книг, выданных каждому читателю
#     cur.execute("""
#         SELECT Readers.FirstName, Readers.LastName, COUNT(*) AS BookCount
#         FROM Readers
#         JOIN Books ON Readers.ReaderID = Books.BookID
#         GROUP BY Readers.ReaderID
#     """)
#     reader_counts = cur.fetchall()
#     print("Общее число книг, выданных каждому читателю:")
#     for count in reader_counts:
#         print(count)
#
#     # Выборка всех читателей, зарегистрированных после определённой даты
#     date = '2022-01-01'
#     cur.execute("SELECT * FROM Readers WHERE RegistrationDate > ?", (date,))
#     recent_readers = cur.fetchall()
#     print(f"Читатели, зарегистрированные после {date}:")
#     for reader in recent_readers:
#         print(reader)


'''3'''

# # Подключение к базе данных SQLite
# conn = sqlite3.connect('sqlite_db_file.db')  # Замените 'sqlite_db_file' на путь к вашей базе данных
# cur = conn.cursor()
#
# try:
#     # 1. Сколько разных спортсменов участвовало в соревнованиях за весь период?
#     query1 = "SELECT COUNT(DISTINCT Name) FROM results"
#     cur.execute(query1)
#     unique_athletes = cur.fetchone()[0]
#     print(f"Уникальных спортсменов: {unique_athletes}")
#
#     # 2. Кто пробежал самую длинную дистанцию?
#     query2 = "SELECT Name, MAX(KM) FROM results"
#     cur.execute(query2)
#     longest_distance = cur.fetchone()
#     print(f"{longest_distance[0]} пробежал самую длинную дистанцию: {longest_distance[1]} км")
#
#     # 3. Сколько раз участвовал в соревнованиях Иван Зелин?
#     query3 = "SELECT COUNT(*) FROM results WHERE Name = 'Иван Зелин'"
#     cur.execute(query3)
#     ivan_zelin_count = cur.fetchone()[0]
#     print(f"Иван Зелин участвовал в соревнованиях {ivan_zelin_count} раз(а)")
#
#     # 4. В каком году команда ездила в город Набережные Челны?
#     query4 = "SELECT DISTINCT strftime('%Y', Date) FROM results WHERE Place = 'Набережные Челны'"
#     cur.execute(query4)
#     years = [year[0] for year in cur.fetchall()]
#     print(f"Команда ездила в Набережные Челны в следующие годы: {', '.join(years)}")
#
#     # 5. Сколько раз становился призёром Михаил Мещанов?
#     query5 = "SELECT COUNT(*) FROM results WHERE Name = 'Михаил Мещанов' AND Rank = 1"  # Предположим, что 1 - это код призёра
#     cur.execute(query5)
#     mikhail_meshchanov_count = cur.fetchone()[0]
#     print(f"Михаил Мещанов становился призёром {mikhail_meshchanov_count} раз(а)")
#
#     # 6. Найдите самое популярное место для соревнований.
#     query6 = "SELECT Place, COUNT(*) AS CompetitionCount FROM results GROUP BY Place ORDER BY CompetitionCount DESC LIMIT 1"
#     cur.execute(query6)
#     most_popular_place = cur.fetchone()
#     print(f"Самое популярное место для соревнований: {most_popular_place[0]}, количество соревнований: {most_popular_place[1]}")
#
#     # 7. Сформируйте рейтинг спортсменов по суммарному километражу.
#     query7 = "SELECT Name, SUM(KM) AS TotalDistance FROM results GROUP BY Name ORDER BY TotalDistance DESC"
#     cur.execute(query7)
#     athlete_ranking = cur.fetchall()
#     print("Рейтинг спортсменов по суммарному километражу:")
#     for rank, athlete in enumerate(athlete_ranking, start=1):
#         print(f"{rank}. {athlete[0]}: {athlete[1]} км")
#
# except sqlite3.Error as e:
#     print(f"Ошибка при работе с базой данных: {e}")
#
# finally:
#     conn.close()  # Закрываем соединение с базой данных



'''4'''

# #1: Создание таблиц
#
# import sqlite3 as sq
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#
#     # Создание таблицы Continents
#     cur.execute("""CREATE TABLE IF NOT EXISTS Continents (
#         ContinentID INTEGER PRIMARY KEY AUTOINCREMENT,
#         ContinentName TEXT NOT NULL
#     )""")
#
#     # Создание таблицы Countries
#     cur.execute("""CREATE TABLE IF NOT EXISTS Countries (
#         CountryID INTEGER PRIMARY KEY AUTOINCREMENT,
#         CountryName TEXT NOT NULL,
#         ContinentID INTEGER,
#         FOREIGN KEY (ContinentID) REFERENCES Continents (ContinentID)
#     )""")
#
#     # Создание таблицы Cities
#     cur.execute("""CREATE TABLE IF NOT EXISTS Cities (
#         CityID INTEGER PRIMARY KEY AUTOINCREMENT,
#         CityName TEXT NOT NULL,
#         CountryID INTEGER,
#         Population INTEGER,
#         FOREIGN KEY (CountryID) REFERENCES Countries (CountryID)
#     )""")
#
#     # Создание таблицы Economy
#     cur.execute("""CREATE TABLE IF NOT EXISTS Economy (
#         CityID INTEGER,
#         GDP REAL,
#         UnemploymentRate REAL,
#         FOREIGN KEY (CityID) REFERENCES Cities (CityID)
#     )""")
#
#
#
# #2: Вставка данных
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#
#     # Вставка данных в таблицу Continents
#     cur.execute("INSERT INTO Continents (ContinentName) VALUES "
#                 "('Азия'), "
#                 "('Европа'), "
#                 "('Северная Америка')")
#
#     # Вставка данных в таблицу Countries
#     cur.execute("INSERT INTO Countries (CountryName, ContinentID) VALUES "
#                 "('Китай', 1), "
#                 "('Индия', 1), "
#                 "('Германия', 2), "
#                 "('Франция', 2), "
#                 "('США', 3), "
#                 "('Канада', 3)")
#
#     # Вставка данных в таблицу Cities
#     cur.execute("INSERT INTO Cities (CityName, CountryID, Population) VALUES "
#                 "('Пекин', 1, 21540000), "
#                 "('Шанхай', 1, 24240000), "
#                 "('Мумбаи', 2, 20411000), "
#                 "('Берлин', 3, 3645000), "
#                 "('Парижs', 4, 2148000), "
#                 "('Нью-Йорк', 5, 8419000), "
#                 "('Лос Анжелес', 5, 3980400), "
#                 "('Торонто', 6, 2731571)")
#
#     # Вставка данных в таблицу Economy
#     cur.execute("INSERT INTO Economy (CityID, GDP, UnemploymentRate) VALUES "
#                 "(1, 5300.75, 4.5), "
#                 "(2, 4800.60, 5.2), "
#                 "(3, 3700.45, 3.8), "
#                 "(4, 2200.30, 4.1), "
#                 "(5, 3000.50, 8.3), "
#                 "(6, 9300.20, 7.4), "
#                 "(7, 6800.80, 9.1), "
#                 "(8, 3500.10, 5.5)")
#
#
#3: Запросы
#
# #Основная выборка данных:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Cities.CityName, Cities.Population, Countries.CountryName
#         FROM Cities
#         JOIN Countries ON Cities.CountryID = Countries.CountryID
#     """)
#     cities = cur.fetchall()
#     print("Все города с их населением и названием страны:")
#     for city in cities:
#         print(city)
#
# #Получение городов по заданной стране:
#
# country_name = 'USA'
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Cities.CityName
#         FROM Cities
#         JOIN Countries ON Cities.CountryID = Countries.CountryID
#         WHERE Countries.CountryName = ?
#     """, (country_name,))
#     cities = cur.fetchall()
#     print(f"Города в стране {country_name}:")
#     for city in cities:
#         print(city)
#
# #Получить список стран, которые принадлежат определенному континенту:
#
# continent_name = 'Europe'
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Countries.CountryName
#         FROM Countries
#         JOIN Continents ON Countries.ContinentID = Continents.ContinentID
#         WHERE Continents.ContinentName = ?
#     """, (continent_name,))
#     countries = cur.fetchall()
#     print(f"Страны в континенте {continent_name}:")
#     for country in countries:
#         print(country)
#
# #Поиск городов с определённой численностью населения:
#
# min_population = 500000
# max_population = 1000000
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT CityName, Population
#         FROM Cities
#         WHERE Population BETWEEN ? AND ?
#     """, (min_population, max_population))
#     cities = cur.fetchall()
#     print(f"Города с населением от {min_population} до {max_population}:")
#     for city in cities:
#         print(city)
#
# #Агрегатные функции и группировка:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Countries.CountryName, SUM(Cities.Population) AS TotalPopulation
#         FROM Cities
#         JOIN Countries ON Cities.CountryID = Countries.CountryID
#         GROUP BY Countries.CountryName
#     """)
#     populations = cur.fetchall()
#     print("Общее население по каждой стране:")
#     for population in populations:
#         print(population)
#
# #Сложное объединение:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Cities.CityName, Economy.GDP, Economy.UnemploymentRate
#         FROM Cities
#         JOIN Economy ON Cities.CityID = Economy.CityID
#     """)
#     city_economies = cur.fetchall()
#     print("Города с их ВВП и уровнем безработицы:")
#     for city_economy in city_economies:
#         print(city_economy)
#
# #LEFT JOIN и фильтрация:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Countries.CountryName, Cities.CityName, Cities.Population
#         FROM Countries
#         LEFT JOIN Cities ON Countries.CountryID = Cities.CountryID
#         WHERE Cities.Population > 1000000
#     """)
#     results = cur.fetchall()
#     print("Страны и города с населением более 1 миллиона человек:")
#     for result in results:
#         print(result)
#
# #Объединение данных с UNION ALL:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Countries.CountryName, Continents.ContinentName
#         FROM Countries
#         JOIN Continents ON Countries.ContinentID = Continents.ContinentID
#         UNION ALL
#         SELECT Cities.CityName, Countries.CountryName
#         FROM Cities
#         JOIN Countries ON Cities.CountryID = Countries.CountryID
#     """)
#     union_results = cur.fetchall()
#     print("Список стран с континентами и городов с указанием страны:")
#     for result in union_results:
#         print(result)
#
# #Использование агрегатных функций MIN, MAX, AVG:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Countries.CountryName, MIN(Cities.Population), MAX(Cities.Population), AVG(Cities.Population)
#         FROM Cities
#         JOIN Countries ON Cities.CountryID = Countries.CountryID
#         GROUP BY Countries.CountryName
#     """)
#     population_stats = cur.fetchall()
#     print("Минимальное, максимальное и среднее население городов для каждой страны:")
#     for stats in population_stats:
#         print(stats)
#
# #Сортировка и лимитирование результатов:
#
# with sq.connect('world.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT Cities.CityName, Economy.GDP
#         FROM Cities
#         JOIN Economy ON Cities.CityID = Economy.CityID
#         ORDER BY Economy.GDP DESC
#         LIMIT 5
#     """)
#     top_gdp_cities = cur.fetchall()
#     print("Топ-5 городов с самым высоким ВВП:")
#     for city in top_gdp_cities:
#         print(city)








