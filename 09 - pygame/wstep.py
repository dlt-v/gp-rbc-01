import pygame

pygame.init() #inicjalizacja pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 # deklaracja wymiarów okienka

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #stworzenie okienka

pygame.display.set_caption("Pierwsza gra") # ustawiamy napis okna
clock = pygame.time.Clock()

game_status = True

while game_status: # główna pętla gry

    events = pygame.event.get() # zbieranie zdarzeń

    for event in events:
        print(event) # wyświetlanie zdarzeń

        if event.type == pygame.QUIT: # jeżeli klikniemy na X w rogu okna to wychodzimy z pętli
            game_status = False

    pygame.display.update() # aktualizujemy ekran

    clock.tick(60)

pygame.quit() # wychodzimy
quit()