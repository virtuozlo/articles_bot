from config.loader import db


def change_db(user_id: int, nickname: str = None):
    """
    Если db не строка (значит это инстанс базы данных), то записать дополнения к юзеру
    :param user_id: tlg.user.id
    :param nickname: tls.user.username
    :return:
    """
    if not isinstance(db, str):  # Если база данных не строка
        if not db.get_user(user_id):
            db.add_user(user_id, nickname)
        else:
            db.update_user(user_id, nickname)
