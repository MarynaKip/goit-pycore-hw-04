def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries_list = []
            data = file.readlines()
            for line in data:
                salary = line.split(",")[1]
                salaries_list.append(int(salary))
            median = sum(salaries_list) / len(salaries_list)
            return median
    except FileNotFoundError:
        print("File was not found!")
    except ValueError:
        print("Wrong data in the file!")

print(total_salary('salaries.txt'))

def get_cats_info(path):
    try:
        with open(path) as file:
            cats_dict = []
            data = file.readlines()
            for line in data:
                cat = line.split(',')
                cats_dict.append({'id': cat[0], 'name': cat[1], 'age': int(cat[2])})
            return cats_dict
    except FileNotFoundError:
        print("File was not found!")

print(get_cats_info('cats.txt'))
