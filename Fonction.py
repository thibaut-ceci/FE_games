
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT


def deplacement(event, player_unit):
    if event.type == KEYDOWN:
        if event.key == K_UP:
            player_unit.move(0, -1)
        elif event.key == K_DOWN:
            player_unit.move(0, 1)
        elif event.key == K_LEFT:
            player_unit.move(-1, 0)
        elif event.key == K_RIGHT:
            player_unit.move(1, 0)
        player_turn = False
    
    return player_turn, player_unit