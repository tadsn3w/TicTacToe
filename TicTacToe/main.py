import pygame

# pygame setup
pygame.init()

WINDOW_WIDTH = WINDOW_HEIGHT = 720
PIXEL_WIDTH = WINDOW_WIDTH // 3

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)
winner_text = font.render("", True, 'green')
text_rect = winner_text.get_rect()
text_rect.center = (WINDOW_WIDTH // 2 - PIXEL_WIDTH // 2, WINDOW_HEIGHT // 2)

running = True


def load_icons(path, resolution):
    icon = pygame.image.load(path)
    return pygame.transform.scale(icon, resolution)


ICON_X = load_icons('icons/x-icon.png', (PIXEL_WIDTH, PIXEL_WIDTH))
ICON_O = load_icons('icons/o-icon.png', (PIXEL_WIDTH, PIXEL_WIDTH))
GRID = load_icons('icons/grid.png', (WINDOW_WIDTH, WINDOW_HEIGHT))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    screen.blit(GRID, (0, 0))
    screen.blit(ICON_X, (0, 0))
    screen.blit(ICON_O, (PIXEL_WIDTH, PIXEL_WIDTH))
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
