let size = 120
let height = 85
let holeDia = 28
let thickness = 2
let hookHeight = 10

const hole = () => Translate([0,0,holeDia+2], Rotate([1,0,0], 90,Translate([0,0,-size],Cylinder(holeDia, size*2))))

const triPrism = (length, width) => Extrude(
    Polygon([[-width/2,0], [width/2,0], [0,height]]),
    [0,0,length]
)

const frame = () => Difference(Offset(triPrism(size, size*0.9), thickness), [Translate([0,0,-10], triPrism(size*2, size*0.9))])

Difference(
    Union([
        Translate([0, size/2,0], Rotate([1,0,0], 90, frame())),
        Translate([-size/2, 0,0], Rotate([0,0,1], 90, Rotate([1,0,0], 90, frame()))),
    ]),
    [
        hole(),
        Rotate([0,0,1],90,hole()),
    ]
)

const toothProfile = new Sketch ([-40,0]).Fillet(20)
    .LineTo([0,hookHeight]).Fillet(20)
    .LineTo([40,0]).Fillet(20)
    .LineTo([45,0])
    .LineTo([-45,0])
    .End(true).Face()
const holeProfile = new Sketch ([-hookHeight/2,0]).Fillet(0.5)
    .LineTo([0,hookHeight/2]).Fillet(0.5)
    .LineTo([hookHeight/2,0]).Fillet(0.5).End(true).Face()

Translate([0,thickness*1.5/2,height],
    Rotate([1,0,0], 90,
        Difference(
            Extrude(toothProfile, [0,0,thickness*1.5]),
            [Extrude(holeProfile, [0,0,thickness*1.5])]
        )
    )
)