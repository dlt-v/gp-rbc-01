import pygame



pygame.init() #inicjalizacja pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # deklaracja wymiarów okienka


screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #stworzenie okienka

def load_image(img_path, position): # Ładowanie do gry obrazków
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center = position)

    return [image, surface, rect]

def print_image(img_list):
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)

pygame.display.set_caption("Pierwsza gra") # ustawiamy napis okna

clock = pygame.time.Clock()

player_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('images/player.png', player_position)

game_status = True

while game_status: # główna pętla gry

    events = pygame.event.get() # zbieranie zdarzeń

    for event in events:
        print(event) # wyświetlanie zdarzeń

        if event.type == pygame.QUIT: # jeżeli klikniemy na X w rogu okna to wychodzimy z pętli
            game_status = False
    print_image(player)
    pygame.display.update() # aktualizujemy ekran

    clock.tick(60)

pygame.quit() # wychodzimy
quit()