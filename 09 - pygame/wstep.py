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

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center = position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_w]:
        delta_y -= speed
    elif keys[pygame.K_a]:
        delta_x -= speed
    elif keys[pygame.K_s]:
        delta_y += speed
    elif keys[pygame.K_d]:
        delta_x += speed
    return [delta_x, delta_y]

pygame.display.set_caption("Pierwsza gra") # ustawiamy napis okna

clock = pygame.time.Clock()

player_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('images/player.png', player_position)

new_item = load_image('images/bonus_1.png', [SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20])

background_color = [0, 0, 0]

game_status = True

while game_status: # główna pętla gry

    events = pygame.event.get() # zbieranie zdarzeń

    for event in events:
        print(event) # wyświetlanie zdarzeń

        if event.type == pygame.QUIT: # jeżeli klikniemy na X w rogu okna to wychodzimy z pętli
            game_status = False

    screen_surface.fill(background_color)

    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)

    player_position[0] += delta_x
    player_position[1] += delta_y

    player = set_position_image(player, player_position)

    print_image(player)
    # print_image(new_item)
    pygame.display.update() # aktualizujemy ekran

    clock.tick(60)

pygame.quit() # wychodzimy
quit()

"""
Utwórz ikonę gracza, 40x40 px, może być w paincie, nazwij plik Gracz.png, zaimportuj go do gry i wyświelt w prawym górym rogu ekranu.
Do 10:10


Zmień pozycję new_item do prawego dolnego rogu ekranu.
"""