include <roundanything/polyround.scad>;
scale(1/25.4)import("praticepart.stl", convexity=3);
// import("practicepart.stl", convexity=3);

width = 120;
height = 85;
holeR = 28;
thickness = 2;
hookHeight = 10;
$fn=20;



outerKeyR = 1;
outerBraceR = 1.89;
outerBraceROnInternalSide = 1.9;

topDownArmThickness = 0.4;

overAllLength = 9.75;
overAllHeight = 4;

keyedSectionLength = 3;
keyedSectionHeight = 1.001;
sideViewR = 0.5;
sideViewArmAngle = 65;
sideViewArmThickness = 0.5;
sideViewCenterR = 0.25;
verticalDistanceBetweenYStartRadiusCenterAndIntersectionOfArm = sideViewR/sin(90-sideViewArmAngle/2);
verticalDistanceFromCenterlineOfPartSideView = keyedSectionHeight/2 - (verticalDistanceBetweenYStartRadiusCenterAndIntersectionOfArm - sideViewR);
echo(keyedSectionHeight/2);
echo((verticalDistanceBetweenYStartRadiusCenterAndIntersectionOfArm - sideViewR));
// verticalDistanceFromCenterlineOfPartSideView = 0.3;
YVerticalDelta = overAllHeight/2 - verticalDistanceFromCenterlineOfPartSideView;
horizontalComponentOfY = YVerticalDelta/tan(sideViewArmAngle/2);
echo(verticalDistanceFromCenterlineOfPartSideView);

rightPartOfYShape = mirrorPoints(
    [
      [1,0],
      [1,1]
    ], 0, [0,0]
);

function yPoints(lengthExtension=0)=[
    [keyedSectionLength-outerKeyR,0],
    [keyedSectionLength-outerKeyR,verticalDistanceFromCenterlineOfPartSideView],
    [keyedSectionLength-outerKeyR+horizontalComponentOfY,overAllHeight/2],
    [overAllLength-outerKeyR+lengthExtension,overAllHeight/2],
    [overAllLength-outerKeyR+lengthExtension,0],
];


module yInternal() {
    offset(-sideViewArmThickness)union(){
        polygon(yPoints(overAllLength));
        mirror([0,1,0])polygon(yPoints(overAllLength));
    }
}

module sideViewOuterShape() {
    linear_extrude(outerBraceR*2)difference() {
        union() {
            round2d(sideViewR)union() {
                polygon(yPoints());
                mirror([0,1,0])polygon(yPoints());
                translate([-outerKeyR,-keyedSectionHeight/2])square([overAllLength, keyedSectionHeight]);
            }
            translate([-outerKeyR,-keyedSectionHeight/2])square([keyedSectionLength, keyedSectionHeight]);
            translate([overAllLength-sideViewR-outerKeyR,0])square([sideViewR*2, overAllHeight], true);
        }
        difference(){
            round2d(sideViewR)yInternal();
            translate([0,-overAllHeight/2])
                square([keyedSectionLength+horizontalComponentOfY/1.5, overAllHeight]);
        }
        round2d(sideViewCenterR)yInternal();
    }
}

module TopDownCylinderTangentOuterShape() {
    hull(){
        cylinder(h=overAllHeight,r=outerKeyR);
        translate([overAllLength-outerBraceR-outerKeyR,0,0])cylinder(h=overAllHeight,r=outerBraceR);
    }
}

module topDownMiddleNegativeSpace() {
    translate([0,0,-0.01])linear_extrude(overAllHeight+0.02)round2d(0.25)difference(){
        offset(-topDownArmThickness)hull(){
            circle(r=outerKeyR);
            translate([overAllLength-outerBraceR-outerKeyR,0])circle(r=outerBraceR);
        }
        circle(r=outerKeyR);
        translate([overAllLength-outerBraceR-outerKeyR,0])circle(r=outerBraceROnInternalSide);
    }
}

intersection() {
    difference(){
        TopDownCylinderTangentOuterShape();
        topDownMiddleNegativeSpace();
    }
    translate([0,outerBraceR,overAllHeight/2])rotate([90,0,0])sideViewOuterShape();
}

// translate([-outerKeyR,0,0])cube([keyedSectionLength,5,5]);
// translate([-outerKeyR,0,0])round2d(sideViewCenterR)yInternal();
// sideViewOuterShape();