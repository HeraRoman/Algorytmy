def add_author(name):
    def decorator(func):
        func.author = name
        return func
    return decorator
@add_author("Роман Романович")
def my_function():
    return "Результат роботи функції"
print(my_function())
print(f"Автор функції: {my_function.author}")