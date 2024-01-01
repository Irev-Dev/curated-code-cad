width = 120.0
base = width * 0.95
thickness = 2.0
hole_diameter = 36.0
hook_length = 80.0
hook_height = 10.0
hook_hole = 6.0

with BuildPart() as birdhouse:
    with BuildSketch(Plane.ZX, Plane.ZY) as roof:
        RegularPolygon(base / 2, 3, align=(Align.MIN, Align.CENTER))
        fillet(roof.vertices(), radius=1)
        offset(amount=-thickness, mode=Mode.SUBTRACT)
    extrude(amount=width / 2, both=True)
    with Locations(
        birdhouse.faces().sort_by(Axis.X)[0], birdhouse.faces().sort_by(Axis.Y)[0]
    ):
        Hole(hole_diameter / 2)
    with BuildSketch(Plane.YZ) as hook:
        Triangle(a=hook_length / 2, b=hook_height, C=90, align=(Align.MAX, Align.MIN))
        RegularPolygon(hook_hole, 4, mode=Mode.SUBTRACT)
        mirror(about=Plane.YZ)
    with Locations((0, 0, birdhouse.part.bounding_box().max.Z - thickness)):
        add(extrude(amount=thickness / 2, both=True, mode=Mode.PRIVATE))
