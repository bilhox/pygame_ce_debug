
import pygame

screen = pygame.display.set_mode(pygame.Vector2(1920, 1080) * 2/3)

# sound = pygame.mixer.Sound(r"C:\Users\lodyB\OneDrive\Documents\workspace_python\tea_mansion\assets\sfx\game.wav")
# array = pygame.sndarray.array(sound)
# print(array)

surf = pygame.Surface(pygame.Vector2(1920, 1080))
surf.fill((255, 0, 0, 128))

surf = pygame.transform.scale(surf, (1920 * 15, 1080 * 18))
# s = surf1.copy()

running = True
clock = pygame.Clock()

while running:
    screen.fill("black")
    dt = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        dx, dy = 0, 0
        if keys[pygame.K_RIGHT]:
            dx += 6
        elif keys[pygame.K_LEFT]:
            dx -= 6
        
        if keys[pygame.K_DOWN]:
            dy += 6
        elif keys[pygame.K_UP]:
            dy -= 6

        surf.scroll(dx, dy)

    # s = pygame.transform.box_blur(surf1, 3, False)

    screen.blit(surf, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"FPS : {round(clock.get_fps(), 2)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.image.save(surf, "../out.png")