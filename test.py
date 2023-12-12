from UniPy import *
import pygame

_color1 = UniColor.white
_color2 = UniColor.white

animScene = Scene("Animation Transition", SCREEN)
sceneManager.AddScene(animScene)

collisionScene1 = Scene("Circle Collision", SCREEN)
sceneManager.AddScene(collisionScene1)
collisionScene2 = Scene("Box Collision", SCREEN)
sceneManager.AddScene(collisionScene2)

audioScene = Scene("Audio Play", SCREEN)
sceneManager.AddScene(audioScene)

def prev():
    sceneManager.LoadScene(sceneManager.index-1)
def next():
    sceneManager.LoadScene(sceneManager.index+1)


# Common UIs
canvas = UI("Canvas")
canvas.transform.position = Vector(WIDTH/2, HEIGHT/2)
canvas.AddComponent(Canvas(SCREEN))

button1 = UI("Button1")
button1.AddComponent(Image())
t = button1.AddComponent(Text("Prev Scene"))
t.fontColor = UniColor.black
t.fontSize = 12
button1.AddComponent(Button(action = prev))
button1.transform.parent = canvas.transform
button1.transform.position = Vector(-150, -200)

button2 = UI("Button2")
button2.AddComponent(Image())
t = button2.AddComponent(Text("Next Scene"))
t.fontColor = UniColor.black
t.fontSize = 12
button2.AddComponent(Button(action = next))
button2.transform.parent = canvas.transform
button2.transform.position = Vector(150, -200)

animScene.hierarchy.append(canvas)
animScene.hierarchy.append(button2)

collisionScene1.hierarchy.append(canvas)
collisionScene1.hierarchy.append(button1)
collisionScene1.hierarchy.append(button2)

collisionScene2.hierarchy.append(canvas)
collisionScene2.hierarchy.append(button1)
collisionScene2.hierarchy.append(button2)

audioScene.hierarchy.append(canvas)
audioScene.hierarchy.append(button1)

# Scene1 - Animation Transition
go = GameObject("TestObject")
go.AddComponent(SpriteRenderer())
go.AddComponent(Animator())
#go.AddComponent(BoxCollider(Vector(32,32)))
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
_clip2.looping = True

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
_animator.AddTransition("Left", "Right", condition2)
#_animator.AddTransition("Left", "Right", condition3)

#go.GetComponent("BoxCollider").OnTriggerEnter(func)
#go.transform.scale = Vector(-1,1) * 5

go.transform.position = Vector(200,250)

text = UI("Text")
text.AddComponent(Text("Facing Right is True"))
text.transform.parent = canvas.transform
text.transform.position = Vector(0,50)

animScene.hierarchy.append(text)
animScene.hierarchy.append(go)

# ================================================================

# Scene2 - Circle Collision
sprite = Sprite("Sprite/Character_Right1.png")
go1 = GameObject("CircleCollision")
go1.AddComponent(SpriteRenderer(sprite))
#go1.AddComponent(BoxCollider(Vector(32,32)))
go1.AddComponent(CircleCollider(radius=16))
#go1.AddComponent(Rigidbody())

go1.transform.position = Vector(200,250)
go1.transform.scale = Vector.one * 2
#go1.transform.rotation = 45

collisionScene1.hierarchy.append(go1)

# ================================================================

# Scene3 - Box Collision
go2 = GameObject("BoxCollision")
go2.AddComponent(SpriteRenderer(sprite))
go2.AddComponent(BoxCollider(Vector(32,32)))
#go2.AddComponent(CircleCollider(radius=16))
#go1.AddComponent(Rigidbody())

go2.transform.position = Vector(200,250)
go2.transform.scale = Vector.one * 2
#go1.transform.rotation = 45

collisionScene2.hierarchy.append(go2)

# ================================================================

# Scene4 - Audio
def volumeUp():
    audioSource.set_volume(audioSource.volume+0.1)
def volumeDown():
    audioSource.set_volume(audioSource.volume-0.1)
def start():
    audioSource.Play()
def stop():
    audioSource.Stop()

audioClip1 = AudioClip("Audio/bgm.wav")
go4 = GameObject("AudioSourceTest")
go4.AddComponent(AudioSource())
audioSource = go4.GetComponent("AudioSource")
audioSource.clip = audioClip1
audioSource.set_volume(1)


buttonUp = UI("ButtonUp")
buttonUp.AddComponent(Image())
t = buttonUp.AddComponent(Text("volume+"))
t.fontColor = UniColor.black
t.fontSize = 12
buttonUp.AddComponent(Button(action = volumeUp))
buttonUp.transform.parent = canvas.transform
buttonUp.transform.position = Vector(50, 0)

buttonDown = UI("ButtonDown")
buttonDown.AddComponent(Image())
t = buttonDown.AddComponent(Text("volume-"))
t.fontColor = UniColor.black
t.fontSize = 12
buttonDown.AddComponent(Button(action = volumeDown))
buttonDown.transform.parent = canvas.transform
buttonDown.transform.position = Vector(-50, 0)

buttonStart = UI("ButtonDown")
buttonStart.AddComponent(Image())
t = buttonStart.AddComponent(Text(">"))
t.fontColor = UniColor.black
t.fontSize = 12
buttonStart.AddComponent(Button(action = start))
buttonStart.transform.parent = canvas.transform
buttonStart.transform.position = Vector(50, 50)

buttonStop = UI("ButtonStop")
buttonStop.AddComponent(Image())
t = buttonStop.AddComponent(Text("[ ]"))
t.fontColor = UniColor.black
t.fontSize = 12
buttonStop.AddComponent(Button(action = stop))
buttonStop.transform.parent = canvas.transform
buttonStop.transform.position = Vector(-50, 50)

audioScene.hierarchy.append(go4)
audioScene.hierarchy.append(buttonUp)
audioScene.hierarchy.append(buttonDown)
audioScene.hierarchy.append(buttonStart)
audioScene.hierarchy.append(buttonStop)


sceneManager.LoadScene(0)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if pygame.mouse.get_pressed()[0] == 1:
        #sceneManager.LoadScene(1)
        #audioSource.Play()
        _animator.SetBool("FacingRight", True)
        text.GetComponent("Text").text = "FacingRight is False"
        go2.transform.rotation += 5
        #go1.transform.rotation = 45
        pass
    if pygame.mouse.get_pressed()[2] == 1:
        _animator.SetBool("FacingRight", False)
        text.GetComponent("Text").text = "FacingRight is True"
        #audioSource.Stop()
        #go.transform.rotation = 0
        go2.transform.rotation = 0
        #go.DestroyFrom(testScene)
        #_flag = True
        pass

    physics = Physics(sceneManager.currentScene)

    SCREEN.fill([0,0,0])

    #print(len(detected))



    if sceneManager.index == 1:
        go1.transform.position = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        detected1 = physics.OverlapCircleAll(Vector(200,150), 16)
        detected2 = physics.OverlapBoxAll(Vector(200,250), 32)
        if len(detected1) > 0:
            _color1 = UniColor.red
        else:
            _color1 = UniColor.green
        if len(detected2) > 0:
            _color2 = UniColor.red
        else:
            _color2 = UniColor.green
        pygame.draw.circle(SCREEN, _color1, [200,150], 16 ,1)
        pygame.draw.rect(SCREEN, _color2, [200-16,250-16,32,32], 1)
    if sceneManager.index == 2:
        go2.transform.position = Vector(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        detected1 = physics.OverlapCircleAll(Vector(200,150), 16)
        detected2 = physics.OverlapBoxAll(Vector(200,250), 32)
        if len(detected1) > 0:
            _color1 = UniColor.red
        else:
            _color1 = UniColor.green
        if len(detected2) > 0:
            _color2 = UniColor.red
        else:
            _color2 = UniColor.green
        pygame.draw.circle(SCREEN, _color1, [200,150], 16 ,1)
        pygame.draw.rect(SCREEN, _color2, [200-16,250-16,32,32], 1)

    sceneManager.currentScene.Update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()