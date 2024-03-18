def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1 = line2 = line3 = line4 = ''

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem.'

        num1, operator, num2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        length = max(len(num1), len(num2)) + 2
        top = num1.rjust(length)
        bottom = operator + num2.rjust(length - 1)
        dashes = '-' * length
        answer = ''
        if show_answers:
            answer = str(eval(problem)).rjust(length)

        if line1 == '':
            line1 = top
            line2 = bottom
            line3 = dashes
            if show_answers:
                line4 = answer
        else:
            line1 += '    ' + top
            line2 += '    ' + bottom
            line3 += '    ' + dashes
            if show_answers:
                line4 += '    ' + answer

    arranged_problems = f'{line1}\n{line2}\n{line3}'
    if show_answers:
        arranged_problems += '\n' + line4

    return arranged_problems

# Test examples
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))