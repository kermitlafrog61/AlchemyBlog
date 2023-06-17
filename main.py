import blogging_platform as bp
from core.db import Base, engine


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
    print(bp.get_post(post2.id))

    bp.update_post(
        post1.id, "Wow, look at this, now!!!", "Even newer legends!!!")

    print(bp.get_post(post1.id))

    bp.delete_post(1)
    print(bp.get_post(post1.id))  # None
