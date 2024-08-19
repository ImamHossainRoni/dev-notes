from user_model import User
from user_repository import UserRepository


def main():
    users = [
        User(1, "Husna Afrin Tithi"),
        User(2, "Abrar"),
        User(3, "Sunny"),
    ]

    user_repository = UserRepository(users)
    all_users = user_repository.get_all_users()
    print(all_users)

    for user in all_users:
        print(user.name)


if __name__ == "__main__":
    main()
