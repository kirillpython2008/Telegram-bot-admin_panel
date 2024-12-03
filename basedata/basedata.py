import aiosqlite


async def add_users(user_id: int):
    connect = await aiosqlite.connect("users.db")
    cursor = await connect.cursor()

    await cursor.execute("INSERT INTO user (id) VALUES (?)", (user_id,))
    await connect.commit()

    await cursor.close()
    await connect.close()


async def return_count_users():
    connect = await aiosqlite.connect("users.db")
    cursor = await connect.cursor()

    count_users = await cursor.execute("SELECT count(*) FROM user")
    count_users = await count_users.fetchone()

    await cursor.close()
    await connect.close()

    return count_users[0]


async def return_list_id_users():
    connect = await aiosqlite.connect("users.db")
    cursor = await connect.cursor()

    users_id = await cursor.execute("SELECT id FROM user")
    users_id = await users_id.fetchall()

    await cursor.close()
    await connect.close()

    list_users_id = [i[0] for i in users_id]

    return list_users_id
