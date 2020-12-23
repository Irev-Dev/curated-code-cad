include <roundanything/polyround.scad>;

width = 120;
height = 85;
holeR = 28;
thickness = 2;
hookHeight = 10;
$fn=50;


framePoints = [[-width/2*0.9,0], [width*0.9/2,0], [0,height]];

hookBaseProfile = [
    [-width/4,0,20],
    [0,hookHeight,10],
    [width/4,0,20],
    [width/4+5,0,0],
    [-width/4-5,0,0],
];

holeProfile = [
    [-hookHeight/2,0,0.5],
    [0,hookHeight/2,0.5],
    [hookHeight/2,0,0.5],
];

module hook() {
    translate([0,thickness*1.5/2,height])rotate([90,0,0])
        linear_extrude(thickness*1.5)difference(){
            polygon(polyRound(hookBaseProfile));
            polygon(polyRound(holeProfile));
        }
}

module frameWithHoleInSide() {
    difference(){
        translate([0,width/2,0])rotate([90,0,0])linear_extrude(width)difference() {
            offset(thickness)polygon(framePoints);
            polygon(framePoints);
        }
        translate([-width,0,holeR+thickness])rotate([0,90,0])cylinder(r=holeR,h=width*2);
    }
}

union() {
    frameWithHoleInSide();
    rotate([0,0,90])frameWithHoleInSide();
    hook();
}
