height = 85.0
width = 120.0
thickness = 2.0
diameter = 22.0
holeDia = 28.0
hookHeight = 10.0

frame_pts = [(-width*0.95/2,0),(width*0.95/2,0),(0,height)]

hook_pts = [(-width/2.5,0), (0,hookHeight), (width/2.5,0),]
hook_tgts = [(1,0),(1,0)]

hook_hole_pts = [(-hookHeight/2,0),(0,hookHeight/2),(hookHeight/2,0)]

def frame(shouldRotate = False):
    return (
        cq.Workplane("YZ")
        .polyline(frame_pts)
        .close()
        .extrude(width/2,both=True)
        .faces('|X')
        .shell(thickness)
        .transformed((0,90,0),(0,holeDia+thickness,0))
        .circle(holeDia)
        .cutThruAll()
    )

def hook():
    return (
        cq.Workplane("YZ",origin=(-thickness*1.5/2,0,height+thickness/2))
        .spline(hook_pts,tangents=hook_tgts)
        .close()
        .extrude(thickness*1.5)
        .polyline(hook_hole_pts)
        .close()
        .cutThruAll()
        .faces('|(0,1,1)').edges('>Z')
        .fillet(thickness/2)
    )

result = (
    frame()
    .union(frame().rotateAboutCenter((0,0,1),90))
    .union(hook())
)