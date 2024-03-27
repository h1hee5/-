# 성적관리 프로그램2
# 2021002006 신희주

# 입력 함수
def input_students():
    students = []
    for i in range(5):
        student = {}
        student['학번'] = input("학번을 입력하세요: ")
        student['이름'] = input("이름을 입력하세요: ")
        student['영어'] = int(input("영어 점수를 입력하세요: "))
        student['C언어'] = int(input("C언어 점수를 입력하세요: "))
        student['파이썬'] = int(input("파이썬 점수를 입력하세요: "))
        students.append(student)
    return students

# 총점/평균 계산 함수
def calculate_total_average(students):
    for student in students:
        total = student['영어'] + student['C언어'] + student['파이썬']
        average = total / 3
        student['총점'] = total
        student['평균'] = average

# 학점 계산 함수
def calculate_grade(student):
    if student['평균'] >= 90:
        return 'A+'
    elif student['평균'] >= 80:
        return 'B+'
    elif student['평균'] >= 70:
        return 'C+'
    elif student['평균'] >= 60:
        return 'D+'
    else:
        return 'F'

# 등수 계산 함수
def calculate_rank(students):
    sorted_students = sorted(students, key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(sorted_students):
        student['등수'] = i + 1

# 출력 함수
def print_students(students):
    print("성적관리 프로그램") 
    print("=" * 80)
    print(" 학번     \t이름\t영어\tC-언어\t파이썬 \t총점 \t평균 \t학점  \t등수")
    print("=" * 80)
    for student in students:
        print(f"{student['학번']}\t{student['이름']}\t{student['영어']}\t{student['C언어']}\t{student['파이썬']}\t{student['총점']}\t{student['평균']:.2f}\t{calculate_grade(student)}\t{student['등수']}")
    print("=" * 80)

# 메인 함수
def main():
    students = input_students()
    calculate_total_average(students)
    calculate_rank(students)
    print_students(students)

if __name__ == "__main__":
    main()
