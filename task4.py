""" У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, 
кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 
7 днів включаючи поточний день. У вашому розпорядженні є список users, кожен елемент якого містить інформацію 
про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, 
ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, 
якщо необхідно.

Вимоги до завдання:
Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
"""


from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        bday_this_year = bday.replace(year=today.year)

        if bday_this_year < today:
            bday_this_year = bday_this_year.replace(year=today.year + 1)

        days = (bday_this_year - today).days

        if days <= 7 and days >= 0:
            congrat_date = bday_this_year
            if congrat_date.weekday() == 5:
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:
                congrat_date += timedelta(days=1)
            result.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return result


users = [{"name": "John Doe", "birthday": "1985.10.15"}, {"name": "Jane Smith", "birthday": "1990.10.27"}]
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))