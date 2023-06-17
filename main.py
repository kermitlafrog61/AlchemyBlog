import blogging_platform as bp
from db import Base, engine


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
