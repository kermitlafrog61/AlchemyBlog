import blogging_platform as bp
from db import Base, engine

"""
12. Извлеките и выведите на экран конкретную запись из блога с использованием функции get_post() в main.py.
13. Обновите заголовок и содержимое записи блога с использованием функции update_post() в main.py.
14. Удалите запись из блога с использованием функции delete_post() в main.py.
"""


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    post1 = bp.create_post(
        title="Wow, look at this",
        content="New Shadow Legends",
        author="Zindaya"
    )

    post2 = bp.create_post(
        title="Interesting news",
        content="Our sharehold is going to be destroyed",
        author="Shareholder223"
    )

    print(bp.get_post(post1.id))

    update_post = bp.update_post(
        post1.id, "Wow, look at this", "New Sadow Legends")

    print(bp.get_post(post1.id))

    bp.delete_post(1)
