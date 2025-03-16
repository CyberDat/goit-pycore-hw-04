def total_salary(path):
    with open(path, 'r', encoding='utf-8') as file:
        salaries = []
        for line in file:
            line = line.strip()
            if ',' in line:
                name, salary = line.split(',')
                if salary.isdigit():
                    salaries.append(int(salary))

        if len(salaries) == 0:
            return 0, 0

        total = sum(salaries)
        average = total / len(salaries)
        return total, average

file_content = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(file_content)

total, average = total_salary("text.txt")
if total is not None and average is not None:
    print(f"Общая сумма заработной платы: {total}, Средняя заработная плата: {average}")


