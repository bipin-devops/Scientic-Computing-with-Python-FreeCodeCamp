def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        
        # Split the operands and operators
        first_num, operator, second_num  = problem.split()
        
        
        # Validation as per requirement
        if operator not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not all(num.isdigit() for num in (first_num, second_num)):
            return "Error: Numbers must only contain digits."
        if len(first_num) > 4 or len(second_num) > 4:
            return "Error: Numbers cannot be more than four digits."
            
            
        # format calculation
        max_length = max(len(first_num), len(second_num))
        width = max_length + 2
        
        # Format each line
        first_line.append(first_num.rjust(width))
        second_line.append(operator + second_num.rjust(width - 1))
        dashes.append("-" * width)
        
        # Answer Calculation
        if show_answers:
            if operator == "+":
                answer = str(int(first_num) + int(second_num))
            else:
                answer = str(int(first_num) - int(second_num))
            
            answers.append(answer.rjust(width))
            
    
    # Join everything together
    problems = ("    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + '    '.join(dashes))
    
    # in the case second argument is true, join results as well
    if show_answers:
        problems += "\n" + "    ".join(answers)
    return problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

