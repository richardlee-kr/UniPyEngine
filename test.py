from UniPy import *
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT  = 500
FPS = 60

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

go = GameObject("TestObject")
sprite = Sprite("Sprite/Character_Right.png")
go.AddComponent(SpriteRenderer())
go.transform.position = Vector(200,250)
go.transform.scale = Vector.one * 5

_clip = AnimationClip(clock, 8)
_clip.AddBySpriteSheet(sprite)

go.AddComponent(Animator())
go.GetComponent("Animator").SetClip(_clip)

go.AddComponent(BoxCollider())
print(go.GetComponent("BoxCollider").size)

def func(other):
    if(other.name == "asdf"):
        print(other.name)

go.GetComponent("BoxCollider").OnTriggerEnter(func)


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    go.GetComponent("SpriteRenderer").Render(SCREEN)

    go.GetComponent("Animator").Update()
    go.transform.rotation += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()