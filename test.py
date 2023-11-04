from UniPy import *
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT  = 500
FPS = 60

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

testScene = Scene("TestScene", SCREEN)
pygame.display.set_caption(testScene.sceneName)

go = GameObject("TestObject")
go.AddComponent(SpriteRenderer())
go.AddComponent(Animator())
go.AddComponent(BoxCollider())

go.transform.position = Vector(200,250)
go.transform.scale = Vector.one * 2

sprite = Sprite("Sprite/Character_Right.png")
_clip = AnimationClip(clock, 8)
_clip.AddBySpriteSheet(sprite)
go.GetComponent("Animator").SetClip(_clip)

sprite = Sprite("Sprite/Character_Right1.png")
go1 = GameObject("TestObject")
go1.AddComponent(SpriteRenderer(sprite))
go1.AddComponent(BoxCollider())

go1.transform.position = Vector(250,250)
go1.transform.scale = Vector.one * 2

testScene.hierarchy.append(go)
testScene.hierarchy.append(go1)

def func(other):
    if(other.name == "asdf"):
        print(other.name)

#go.GetComponent("BoxCollider").OnTriggerEnter(func)

#go.transform.scale = Vector(-1,1) * 5

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    testScene.Update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()