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


def _format_line(index, prompt):
    star = " ⭐" if prompt["favorite"] else ""
    return f"{index}. [{prompt['category']}] {prompt['title']}{star}"


def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")
    title = _read_nonempty("제목: ")
    content = _read_nonempty("내용: ")
    category = _choose_category()
    prompts.append(
        {"title": title, "content": content, "category": category, "favorite": False}
    )
    print("\n프롬프트가 추가되었습니다!")


def show_list(prompts):
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(prompts, start=1):
        print(_format_line(i, prompt))
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category(prompts):
    print("\n=== 카테고리별 조회 ===")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")
    choice = input("선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 번호입니다.")
        return
    category = CATEGORIES[int(choice) - 1]
    matched = [p for p in prompts if p["category"] == category]
    print(f"\n[{category}] 카테고리 프롬프트:")
    if not matched:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return
    for i, prompt in enumerate(matched, start=1):
        print(_format_line(i, prompt))
    print(f"\n총 {len(matched)}개의 프롬프트")


def search_prompt(prompts):
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip().lower()
    matched = [
        p for p in prompts
        if keyword in p["title"].lower() or keyword in p["content"].lower()
    ]
    print("\n검색 결과:")
    if not matched:
        print("검색 결과가 없습니다.")
        return
    for i, prompt in enumerate(matched, start=1):
        print(_format_line(i, prompt))
    print(f"\n{len(matched)}개의 프롬프트를 찾았습니다.")


def show_menu():
    print(MENU_TEXT)
    return input("선택: ").strip()


ACTIONS = {
    "1": add_prompt,
    "2": show_list,
    "3": show_by_category,
    "4": search_prompt,
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
