from UniPy import *
import asyncio
import pygame

_color = UniColor.green

SCREEN_WIDTH = 400
SCREEN_HEIGHT  = 500
FPS = 60

pygame.init()

clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

testScene = Scene("TestScene", SCREEN)
pygame.display.set_caption(testScene.sceneName)

physics = Physics(testScene)

go = GameObject("TestObject")
go.AddComponent(SpriteRenderer())
go.AddComponent(Animator())
#go.AddComponent(BoxCollider())
go.AddComponent(CircleCollider(radius=16))

go.transform.position = Vector(200,250)
go.transform.scale = Vector.one * 2
go.layer = "NOT"

sprite = Sprite("Sprite/Character_Right.png")
_clip = AnimationClip(clock, 8)
_clip.AddBySpriteSheet(sprite)
go.GetComponent("Animator").SetClip(_clip)

sprite = Sprite("Sprite/Character_Right1.png")
go1 = GameObject("TestObject1")
go1.AddComponent(SpriteRenderer(sprite))
go1.AddComponent(BoxCollider(Vector(32,32)))
#go1.AddComponent(CircleCollider(radius=16))

go1.transform.position = Vector(250,250)
go1.transform.scale = Vector.one * 2
#go1.transform.rotation = 45

#testScene.hierarchy.append(go)
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

    if pygame.mouse.get_pressed()[0] == 1:
        go1.transform.rotation += 1
    if pygame.mouse.get_pressed()[2] == 1:
        go1.transform.rotation = 0

    SCREEN.fill([0,0,0])

    #detected = physics.OverlapCircleAll(Vector(200,250), 16)
    detected = physics.OverlapBoxAll(Vector(200,250), 32)
    #print(len(detected))

    if len(detected) > 0:
        _color = UniColor.red
    else:
        _color = UniColor.green


    go1.transform.position = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    testScene.Update()

    #pygame.draw.circle(SCREEN, _color, [200,250], 16 ,1)
    pygame.draw.rect(SCREEN, _color, [200-16,250-16,32,32], 1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()