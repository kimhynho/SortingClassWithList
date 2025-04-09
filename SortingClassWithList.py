########################
#프로그램명 : SortingClassWithList.py
#작성자 : 소웨 김현호
#작성일 : 3/25 ~ 3/30
#이 파이썬 프로그램은 학생들의 성적을 관리하는 간단한 성적 관리 시스템입니다. 주요 기능은 다음과 같습니다:
#학생의 성적 입출력 (총점, 평균, 학점 등 포함)
#등수 계산
#학생 삭제 및 탐색
#총점 기준 정렬
#평균 80점 이상 학생 수 확인
#실행 시 메뉴를 통해 원하는 기능을 선택할 수 있습니다.
#################################
#작동예시
#1. 성적 입력
#학번: 2024001
#이름: Alice
#영어 점수: 90
#C-언어 점수: 85
#파이썬 점수: 92
#2. 성적 출력
#학번	이름	영어	C-언어	파이썬	총점	평균	학점	등수
#2024001	Alice	90	85	92	267	89.00	B	0





students = []  # 학생 정보를 담을 리스트

# 학생 성적 입력 함수
def input_scores():
    student_id = input("학번: ")
    name = input("이름: ")
    english = int(input("영어 점수: "))
    c_language = int(input("C-언어 점수: "))
    python = int(input("파이썬 점수: "))  # <- 여기서 문법 오류 있었던 거 주의!
    
    total = english + c_language + python  # 총점 계산
    avg = total / 3  # 평균 계산
    grade = calculate_grade(avg)  # 평균 기반 학점 계산
    
    # 학생 정보를 딕셔너리로 추가
    students.append({
        "학번": student_id, "이름": name, "영어": english, "C-언어": c_language, "파이썬": python,
        "총점": total, "평균": avg, "학점": grade, "등수": 0  # 등수는 나중에 계산
    })


# 평균 점수에 따른 학점 계산 함수
def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


# 등수 계산 함수 (총점을 기준으로)
def calculate_ranks():
    # 총점만 뽑아서 내림차순 정렬
    total_scores = [student['총점'] for student in students]
    sorted_scores = sorted(total_scores, reverse=True)
    
    # 각 학생의 총점이 정렬된 리스트에서 몇 번째인지 찾아 등수 부여
    for student in students:
        student['등수'] = sorted_scores.index(student['총점']) + 1

    print("등수별 학생 목록:")
    for student in students:
        print(f"{student['등수']}등: {student['이름']}")


# 학생 성적 출력 함수
def print_scores():
    print("학번", "이름", "영어", "C-언어", "파이썬", "총점", "평균", "학점", "등수", sep='\t')
    for student in students:
        print(
            student['학번'], student['이름'], student['영어'], student['C-언어'], student['파이썬'],
            student['총점'], f"{student['평균']:.2f}", student['학점'], student['등수'], sep='\t'
        )


# 학생 성적 삭제 함수 (학번 기준)
def delete_score():
    student_id = input("삭제할 학생의 학번: ")
    for i, student in enumerate(students):
        if student['학번'] == student_id:
            del students[i]
            print(f"학번 {student_id} 학생의 성적이 삭제되었습니다.")
            return
    print("해당 학번을 찾을 수 없습니다.")


# 학생 탐색 함수 (학번 또는 이름)
def search_student():
    search_key = input("학번 또는 이름을 입력하세요: ")
    for student in students:
        if student['학번'] == search_key or student['이름'] == search_key:
            print(student)
            return
    print("학생을 찾을 수 없습니다.")


# 총점 기준 정렬 함수
def sort_by_total():
    students.sort(key=lambda x: x['총점'], reverse=True)  # 총점을 기준으로 내림차순 정렬
    calculate_ranks()  # 정렬 후 등수 재계산
    print_scores()


# 평균 80점 이상 학생 수 출력
def count_above_80():
    count = sum(1 for student in students if student['평균'] >= 80)
    print(f"80점 이상 학생 수: {count}")


# 메인 메뉴 루프
def main():
    while True:
        print("\n=== 학생 성적 관리 프로그램 ===")
        print("1. 성적 입력")
        print("2. 성적 출력")
        print("3. 등수 계산")
        print("4. 성적 삭제")
        print("5. 성적 탐색")
        print("6. 총점 정렬")
        print("7. 80점 이상 학생 수")
        print("8. 종료")
        
        choice = input("메뉴를 선택하세요: ")
        if choice == '1':
            input_scores()
        elif choice == '2':
            print_scores()
        elif choice == '3':
            calculate_ranks()
        elif choice == '4':
            delete_score()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_by_total()
        elif choice == '7':
            count_above_80()
        elif choice == '8':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다.")


# 프로그램 실행
if __name__ == "__main__":
    main()
