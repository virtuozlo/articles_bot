from config.loader import db


def change_db(user_id: int, nickname: str = None):
    if not db.get_user(user_id):
        db.add_user(user_id, nickname)
    else:
        db.update_user(user_id, nickname)
