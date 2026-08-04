from .data import DEFAULT_PROMPTS

MENU_TEXT = """
=== 나만의 프롬프트 관리 ===
1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록
0. 종료
"""


def show_menu():
    print(MENU_TEXT)
    return input("선택: ").strip()


ACTIONS = {}


def run():
    prompts = [dict(p) for p in DEFAULT_PROMPTS]
    while True:
        choice = show_menu()
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("잘못된 번호입니다. 다시 선택해주세요.")
            continue
        action(prompts)
