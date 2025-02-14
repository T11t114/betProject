from bet_maker.app import crud


def get_create_bet() -> callable:
    return crud.create_bet

def get_get_bets() -> callable:
    return crud.get_all_bets