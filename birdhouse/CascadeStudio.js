let width      = Slider("Width"      , 120, 100, 200);
let height     = Slider("Height"     ,  85, 100, 100);
let holeR      = Slider("Hole Radius",  28,   1,  30);
let thickness  = Slider("Thickness"  ,   2,   1,  15);
let hookHeight = Slider("Hook Height",  10,   3,  15);

const hole = () => Translate([0,0,holeR+2], Rotate([1,0,0], 90,Translate([0,0,-width],Cylinder(holeR, width*2))))

const triPrism = (length, width) => Extrude(
    Polygon([[-width/2,0], [width/2,0], [0,height]]),
    [0,0,length]
)

const frame = () => Difference(Offset(triPrism(width, width*0.9), thickness), [Translate([0,0,-10], triPrism(width*2, width*0.9))])

Difference(
    Union([
        Translate([0, width/2,0], Rotate([1,0,0], 90, frame())),
        Translate([-width/2, 0,0], Rotate([0,0,1], 90, Rotate([1,0,0], 90, frame()))),
    ]),
    [
        hole(),
        Rotate([0,0,1],90,hole()),
    ]
)

const hookBaseProfile = new Sketch ([-width/4,0]).Fillet(20)
    .LineTo([0,hookHeight]).Fillet(20)
    .LineTo([width/4,0]).Fillet(20)
    .LineTo([width/4+5,0])
    .LineTo([-width/4-5,0])
    .End(true).Face()
const holeProfile = new Sketch ([-hookHeight/2,0]).Fillet(0.5)
    .LineTo([0,hookHeight/2]).Fillet(0.5)
    .LineTo([hookHeight/2,0]).Fillet(0.5).End(true).Face()


Translate([0,thickness*1.5/2,height],
    Rotate([1,0,0], 90,
        Difference(
            Extrude(hookBaseProfile, [0,0,thickness*1.5]),
            [Extrude(holeProfile, [0,0,thickness*1.5])]
        )
    )
)
