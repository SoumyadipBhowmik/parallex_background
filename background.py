import pygame

clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

scroll = 0
bg_images = []

for i in range(0, 5):
    bg_image = pygame.image.load(f"graphics\Backgroundlayers\{i}.png").convert_alpha()
    scaled_background = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_images.append(scaled_background)
bg_width = bg_images[0].get_width()


def draw_bg():
    for x in range(10):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 1


pygame.display.set_caption("BG")

run = True
while run:
    clock.tick(FPS)

    draw_bg()

    #keypresses:
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 1
    if key[pygame.K_RIGHT] and scroll < 500:
        scroll += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

