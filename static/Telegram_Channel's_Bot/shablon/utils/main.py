from loader import db
async def main():
    users = db.select_all_users()
    print(users)

main()