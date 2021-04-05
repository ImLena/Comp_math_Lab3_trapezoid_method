import solve


def input_type():
    print("Выберите функцию\n" +
          "1. 1/x\n" +
          "2. x^2\n" +
          "3. 8x + x^2 - x^3 / 3\n" +
          "4. sin(x)/x\n" +
          "5. sqrt(x)")
    answer = int(input().strip())
    if answer in range(1, 6):
        limits = input_limits()
        accuracy = input_accuracy()
        print_answer(solve.set_function(answer, limits, accuracy))
    else:
        print("Неверный тип")
        input_type()


def input_limits():
    print("Введите пределы интегрирования")
    answer = input().split(' ')
    return answer


def input_accuracy():
    print("Введите точность")
    answer = float(input().strip())
    return answer

def print_answer(result):
    if result[0] == 3:
        print("Функция не определена на заданном отрезке или его части")
        return
    if result[0] == 2:
        print("Pазрыв 2-го рода")
        return
    elif result[0] == 1:
        print("Интервал содержит точку разрыва 1-го типа\n")
    print("Интеграл = " + str(result[1]) + "\n" +
          "Число разбиений: " + str(result[2]) + "\n" +
          "Погрешость: " + str(result[3]) + "\n")


input_type()
