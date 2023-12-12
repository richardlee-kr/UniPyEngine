from UniPy import *
import asyncio
import pygame

_color = UniColor.green

scene = Scene("Test", SCREEN)
sceneManager.AddScene(scene)
sceneManager.LoadScene(0)

physics = Physics(sceneManager.currentScene)
pygame.display.set_caption(sceneManager.currentScene.sceneName)

scene2 = Scene("Test2", SCREEN)
sceneManager.AddScene(scene2)


pygame.init()

clock = pygame.time.Clock()


'''
go = GameObject("TestObject")
go.AddComponent(SpriteRenderer())
go.AddComponent(Animator())
go.AddComponent(BoxCollider(Vector(32,32)))
#go.AddComponent(CircleCollider(radius=16))

go.transform.position = Vector(200,250)
go.transform.scale = Vector.one * 2
go.layer = "Default"

sprite1 = Sprite("Sprite/Character_Right.png")
_clip1 = AnimationClip(clock, 8)
_clip1.AddBySpriteSheet(sprite1)
_clip1.looping = True
sprite2 = Sprite("Sprite/Character_Left.png")
_clip2 = AnimationClip(clock, 8)
_clip2.AddBySpriteSheet(sprite2)
_clip2.looping = False

#go.GetComponent("Animator").SetClip(_clip1)
_animator:Animator = go.GetComponent("Animator")
_animator.AddParameter("FacingRight", "bool")
_animator.AddNode("Right", _clip1)
_animator.AddNode("Left", _clip2)

condition1 = Condition("FacingRight", "bool")
condition1.value = True
condition2 = Condition("FacingRight", "bool")
condition2.value = False
condition3 = Condition("unconditional","trigger")
condition3.conditionType = ConditionType.TRIGGERED
_animator.AddTransition("Right", "Left", condition1)
#_animator.AddTransition("Left", "Right", condition2)
_animator.AddTransition("Left", "Right", condition3)


#go.GetComponent("BoxCollider").OnTriggerEnter(func)
#go.transform.scale = Vector(-1,1) * 5

scene.hierarchy.append(go)
'''
'''
sprite = Sprite("Sprite/Character_Right1.png")
go1 = GameObject("RigidbodyTest")
go1.AddComponent(SpriteRenderer(sprite))
#go1.AddComponent(BoxCollider(Vector(32,32)))
go1.AddComponent(CircleCollider(radius=16))
#go1.AddComponent(Rigidbody())

go1.transform.position = Vector(200,250)
go1.transform.scale = Vector.one * 2
#go1.transform.rotation = 45

scene.hierarchy.append(go1)
'''

'''
audioClip1 = AudioClip("Audio/sfx.wav")
go2 = GameObject("AudioSourceTest")
go2.AddComponent(AudioSource())
audioSource = go2.GetComponent("AudioSource")
audioSource.clip = audioClip1
audioSource.set_volume(0.1)
'''
canvas = UI("Canvas")
canvas.transform.position = Vector(WIDTH/2, HEIGHT/2)
canvas.AddComponent(Canvas(SCREEN))

scene.hierarchy.append(canvas)

image = UI("Image")
image.AddComponent(Image())
image.transform.parent = canvas.transform

text = UI("Text")
text.AddComponent(Text("Test"))
text.transform.parent = canvas.transform
text.transform.position = Vector(0,-50)

button = UI("Button")
button.AddComponent(Image())
t = button.AddComponent(Text("Button"))
t.fontColor = UniColor.black
t.fontSize = 15
button.AddComponent(Button())
button.transform.parent = canvas.transform
button.transform.position = Vector(0, 0)

#scene.hierarchy.append(image)
#scene.hierarchy.append(text)
scene.hierarchy.append(button)
'''
def func(other):
    if(other.name == "asdf"):
        print(other.name)
'''

_flag = False

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if pygame.mouse.get_pressed()[0] == 1:
        #sceneManager.LoadScene(1)
        #audioSource.Play()
        #_animator.SetBool("FacingRight", True)
        #go.transform.rotation += 1
        #go1.transform.rotation = 45
        pass
    if pygame.mouse.get_pressed()[2] == 1:
        #audioSource.Stop()
        #_animator.SetBool("FacingRight", True)
        #_animator.SetBool("FacingRight", False)
        #_animator.SetBool("FacingRight", True)
        #go.transform.rotation = 0
        #go.DestroyFrom(testScene)
        #_flag = True
        pass

    SCREEN.fill([0,0,0])

    '''
    detected = physics.OverlapCircleAll(Vector(200,250), 16)
    #detected = physics.OverlapBoxAll(Vector(200,250), 32)
    #print(len(detected))

    #pygame.draw.circle(SCREEN, _color, [200,250], 16 ,1)
    #pygame.draw.rect(SCREEN, _color, [200-16,250-16,32,32], 1)

    if len(detected) > 0:
        _color = UniColor.red
    else:
        _color = UniColor.green

    #print(_animator.isPlaying)
    #print(_animator.currentClip)

    #go.transform.position = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    '''

    sceneManager.currentScene.Update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()