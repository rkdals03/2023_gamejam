from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

camera.orthographic = True
camera.fov = 20
 
ground = Entity(
    model = 'cube',
    color = color.rgb(50,180,50),
    z=0.1,
    y=-8,
    scale = (100, 5, 10),
    collider = 'box'
)

player = PlatformerController2d()

app.run()