height = 85.0
width = 120.0
thickness = 2.0
diameter = 22.0
holeDia = 28.0
hookHeight = 10.0

def turn90(shape, shouldRotate):
    if shouldRotate:
        return shape.rotateAboutCenter((0,0,1),90)
    return shape

def frame(shouldRotate = False):
    temp = (
        cq.Workplane("YZ")
        .moveTo(-width*0.95/2,0)
        .lineTo(width*0.95/2,0)
        .lineTo(0,height)
        .close()
        .extrude(width)
        .faces('|X')
        .shell(thickness)
        .translate((-width/2,0,0))
    )
    return turn90(temp, shouldRotate)

def hookBody():
    return (
        cq.Workplane("YZ")
        .moveTo(-width/4,1)
        .lineTo(0,hookHeight)
        .lineTo(width/4,1)
        .lineTo(width/4+5,0)
        .lineTo(-width/4-5,0)
        .close()
        .extrude(thickness*1.5)
        .edges("|X exc (<Y or >Y)")
        .fillet(10)
        .translate((-thickness*1.5/2,0,height))
    )

def hookVoid():
    return (
        cq.Workplane("YZ")
        .moveTo(-hookHeight/2,0)
        .lineTo(0,hookHeight/2)
        .lineTo(hookHeight/2,0)
        .close()
        .extrude(thickness*2)
        .edges("|X")
        .fillet(0.5)
        .translate((-thickness,0,height))
    )

def door(shouldRotate = False):
    temp = (
        cq.Workplane("YZ")
        .circle(holeDia)
        .extrude(width*4)
        .translate((-width*2,0,holeDia+thickness))
    )
    return turn90(temp, shouldRotate)

result = (
    frame()
    .union(frame(True))
    .union(hookBody())
    .cut(
        hookVoid()
        .union(door())
        .union(door(True))
    )
)