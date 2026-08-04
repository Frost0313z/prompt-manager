from .data import CATEGORIES, DEFAULT_PROMPTS

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


def _read_nonempty(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("값을 입력해야 합니다. 다시 입력해주세요.")


def _choose_category():
    print("\n카테고리 선택:")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")
    choice = input("번호를 선택하거나 새 카테고리명을 입력하세요: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        return CATEGORIES[int(choice) - 1]
    return choice or "기타"


def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")
    title = _read_nonempty("제목: ")
    content = _read_nonempty("내용: ")
    category = _choose_category()
    prompts.append(
        {"title": title, "content": content, "category": category, "favorite": False}
    )
    print("\n프롬프트가 추가되었습니다!")


def show_menu():
    print(MENU_TEXT)
    return input("선택: ").strip()


ACTIONS = {
    "1": add_prompt,
}


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
