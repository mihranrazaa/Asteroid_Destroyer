import pygame
from pygame import mixer

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from sound import gameover


def end_screen(screen, score):
    screen.fill("black")

    game_over_font = pygame.font.Font(None, 64)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    )
    screen.blit(game_over_text, game_over_rect)

    score_font = pygame.font.Font(None, 48)
    final_score_text = score_font.render(f"Final Score: {score}", True, (255, 255, 255))
    final_score_rect = final_score_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10)
    )
    screen.blit(final_score_text, final_score_rect)

    restart_font = pygame.font.Font(None, 36)
    restart_text = restart_font.render(
        "Press Space to Restart OR Esc to Quit", True, (255, 255, 255)
    )
    restart_rect = restart_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    )
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()
    gameover()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    mixer.music.unpause()
                    return True
