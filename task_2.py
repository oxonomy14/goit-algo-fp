"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle


def draw_tree(branch_length, level):
    if level == 0 or branch_length < 5:
        return

    turtle.forward(branch_length)

    turtle.left(30)
    draw_tree(branch_length * 0.7, level - 1)

    turtle.right(60)
    draw_tree(branch_length * 0.7, level - 1)

    turtle.left(30)
    turtle.backward(branch_length)


def main():
    try:
        level = int(input("Введіть рівень рекурсії (1–12): "))

        if not 1 <= level <= 12:
            print("Помилка: введіть число від 1 до 12.")
            return

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return

    screen = turtle.Screen()
    screen.title("Фрактал — дерево Піфагора")
    screen.bgcolor("white")
    screen.setup(width=1000, height=800)

    turtle.speed(0)
    turtle.pensize(2)
    turtle.color("darkgreen")
    turtle.penup()
    turtle.goto(0, -300)
    turtle.setheading(90)
    turtle.pendown()

    draw_tree(120, level)

    turtle.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
