import pygame
import random 


pygame.init() #inicjalizacja pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # deklaracja wymiarów okienka
FRAMES_PER_SECOND = 60


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

def limit_position(position):
    """
    Tworzymy funkcję limit_position, która przyjmuje współrzędne i sprawdza, czy są poprawne. Jeśli nie są poprawne zmienia współrzędne, tak aby zawsze były na ekranie.
    
    """
    x = position[0]
    y = position[1]

    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))


    return [x, y]

pygame.display.set_caption("Pierwsza gra") # ustawiamy napis okna

clock = pygame.time.Clock()

player_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('images/player.png', player_position)

bonus_images = [ #lista ścieżek do plików
    'images/bonus_1.png', 
    'images/bonus_2.png', 
    'images/bonus_3.png'
]

bonus_objects = []

def generate_bonus_object():
    image_path = random.choice(bonus_images)

    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)

    new_object = load_image(image_path, [x, y])
    bonus_objects.append(new_object)

def print_bonus_objects():

    for object in bonus_objects:
        print_image(object)

def check_collisions():
    rect_player = player[2]

    # Przeiteruj przez listę bonusowych obiektów
    for bonus_object in bonus_objects:
        rect_object = bonus_object[2]
    # Sprawdź czy gracz dotyka obiektu
    # Obiekt usuń z listy obiektów jeżeli tak
        if rect_object.colliderect(rect_player):
            bonus_objects.remove(bonus_object)


    

background_color = [0, 0, 0]

game_status = True
frames_counter = 0

while game_status: # główna pętla gry
    frames_counter += 1

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

    player_position = limit_position(player_position)

    player = set_position_image(player, player_position)

    print_image(player)

    if frames_counter % (FRAMES_PER_SECOND * 4) == 0:
        generate_bonus_object()
    check_collisions()
    print_bonus_objects()

    pygame.display.update() # aktualizujemy ekran

    clock.tick(FRAMES_PER_SECOND)

pygame.quit() # wychodzimy
quit()

"""
Utwórz ikonę gracza, 40x40 px, może być w paincie, nazwij plik Gracz.png, zaimportuj go do gry i wyświelt w prawym górym rogu ekranu.
Do 10:10


Zmień pozycję new_item do prawego dolnego rogu ekranu.
"""