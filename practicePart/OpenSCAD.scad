include <roundanything/polyround.scad>;

$fn=20;

outerKeyR = 1;
keyWidth = 0.35;
keyDistanceFromRCenter = 0.77;
keyAngle = 120;

outerBraceR = 1.89;
internalKeyR = 0.55;
internalBraceD = 2.9;
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
YVerticalDelta = overAllHeight/2 - verticalDistanceFromCenterlineOfPartSideView;
horizontalComponentOfY = YVerticalDelta/tan(sideViewArmAngle/2);

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
    union() {
        round2d(sideViewR)union() {
            polygon(yPoints());
            mirror([0,1,0])polygon(yPoints());
            translate([-outerKeyR,-keyedSectionHeight/2])square([overAllLength, keyedSectionHeight]);
        }
        translate([-outerKeyR,-keyedSectionHeight/2])square([keyedSectionLength, keyedSectionHeight]);
        translate([overAllLength-sideViewR-outerKeyR,0])square([sideViewR*2, overAllHeight], true);
    }
}

module sideViewInnerShape() {
    difference(){
        round2d(sideViewR)yInternal();
        // removing the tip so that it can be union with the same shape but with smaller radius
        translate([0,-overAllHeight/2])
            square([keyedSectionLength-outerKeyR+horizontalComponentOfY/2, overAllHeight]);
    }
    round2d(sideViewCenterR)yInternal();
}

module sideViewShape() {
    difference() {
        sideViewOuterShape();
        sideViewInnerShape();
    }
}

module TopDownCylinderTangentOuterShape() {
    translate([0,0,-overAllHeight/2])hull(){
        cylinder(h=overAllHeight,r=outerKeyR);
        translate([overAllLength-outerBraceR-outerKeyR,0,0])cylinder(h=overAllHeight,r=outerBraceR);
    }
}

module topDownMiddleNegativeSpace() {
    translate([0,0,-overAllHeight/2-0.01])linear_extrude(overAllHeight+0.02)round2d(0.25)difference(){
        offset(-topDownArmThickness)hull(){
            circle(r=outerKeyR);
            translate([overAllLength-outerBraceR-outerKeyR,0])circle(r=outerBraceR);
        }
        circle(r=outerKeyR);
        translate([overAllLength-outerBraceR-outerKeyR,0])circle(r=outerBraceROnInternalSide);
    }
}

module keyWayNegative() {
    union() {
        translate([0,0,-overAllHeight])cylinder(r=internalKeyR, h=overAllHeight*2);
        rotate([0,0,180-keyAngle])translate([0,-keyWidth/2,-overAllHeight])cube([keyDistanceFromRCenter,keyWidth,overAllHeight*2]);
    }
}

module shapeBeforeGeneralFillet() {
    intersection() {
        difference(){
            TopDownCylinderTangentOuterShape();
            topDownMiddleNegativeSpace();
            translate([overAllLength-outerBraceR-outerKeyR,0,-overAllHeight])cylinder(d=internalBraceD, h=overAllHeight*2);
        }
        translate([0,outerBraceR,0])rotate([90,0,0])linear_extrude(outerBraceR*2)sideViewShape();
    }
}
difference() {
    shapeBeforeGeneralFillet();
    keyWayNegative();
}
