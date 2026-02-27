# Variables: Exams
exams = ['E1', 'E2', 'E3']

# Domains: Available proctors for each exam
domains = {
    'E1': ['P1', 'P2', 'P3','P4', 'P5', 'P6'],
    'E2': ['P1', 'P2', 'P3','P4', 'P5', 'P6'],
    'E3': ['P1', 'P2', 'P3','P4', 'P5', 'P6']
}

# Proctor availability (time slots)
availability = {
    'P1': ['9AM'],
    'P2': ['9AM', '10AM'],
    'P3': ['10AM'],  # P3 cannot invigilate 9AM exam
    'P4': ['9AM', '10AM'],
    'P5': ['9AM', '10AM'],
    'P6': ['9AM','10AM']
}

# Exam schedule (time slot for each exam)
exam_schedule = {
    'E1': '9AM',
    'E2': '9AM',
    'E3': '10AM'
}

# Exam skill requirements
exam_skill = {
    'E1': 'Math',
    'E2': 'Social',
    'E3': 'Math',
    'E4': 'Science',
    'E5': 'Math'
}

# Proctor skills
proctor_skill = {
    'P1': ['Math'],
    'P2': ['Science'],
    'P3': ['Math'],
    'P4': ['Math,Science'],
    'P5': ['Math'],
    'P6': ['Social']
    
}

# Function to check if assignment is valid
def is_consistent(exam, proctor, assignment):
    # 1. Check if proctor is already assigned to another exam at the same time
    for e, p in assignment.items():
        if p == proctor and exam_schedule[e] == exam_schedule[exam]:
            return False
    # 2. Check if proctor is available at the exam time
    if exam_schedule[exam] not in availability[proctor]:
        return False
    # 3. Check if proctor has the required skill
    if exam_skill[exam] not in proctor_skill[proctor]:
        return False
    return True

# Backtracking function
def backtrack(assignment):
    # If all exams are assigned a proctor, return solution
    if len(assignment) == len(exams):
        return assignment

    # Select first unassigned exam
    for exam in exams:
        if exam not in assignment:
            current_exam = exam
            break

    # Try each proctor in the domain
    for proctor in domains[current_exam]:
        if is_consistent(current_exam, proctor, assignment):
            assignment[current_exam] = proctor
            result = backtrack(assignment)
            if result is not None:
                return result
            # Backtrack
            del assignment[current_exam]

    return None

# Start solving
solution = backtrack({})

# Print result
if solution:
    print("Conflict-free proctor assignment found:")
    for exam, proctor in solution.items():
        print(f"{exam}: {proctor}")
else:
    print("No conflict-free assignment possible.")
