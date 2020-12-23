const { polygon, cylinder } = require('@jscad/modeling').primitives
const { extrudeLinear } = require('@jscad/modeling').extrusions
const { expand } = require('@jscad/modeling').expansions
const { union, subtract } = require('@jscad/modeling').booleans
const { translateY, translateZ, rotateX, rotateY, rotateZ } = require('@jscad/modeling').transforms

let width = 120
let extendedWidth = width*1.1
let height = 85
let holeR = 28
let thickness = 2
let hookHeight = 10

const door = () => {
    let shape
    shape = cylinder({radius: holeR, height: width*2})
    shape = rotateY(Math.PI/2, shape)
    shape = translateZ(holeR+thickness,shape)
    return shape
}
    
const topHook = () => {
    const points = [
        [-width/4-30,-0.1],
        [width/4+30,-0.1],
        [width/4,0],
        [0,hookHeight],
        [-width/4,0],
    ]
    const hookHolePoints = [
        [hookHeight/2,0],
        [0,hookHeight/2],
        [-hookHeight/2,0],
    ]
    let hookHole = polygon({ points: hookHolePoints })
    hookHole = expand({delta: -1, corners: 'round', segments: 100}, hookHole)
    hookHole = expand({delta: 1, corners: 'round', segments: 100}, hookHole)
    let shape = polygon({ points })
    shape = expand({delta: 100.1, corners: 'round', segments: 100}, shape)
    shape = expand({delta: -100, corners: 'round', segments: 100}, shape)
    shape = subtract(shape,hookHole)
    shape = extrudeLinear({height: thickness*1.5, twistAngle: 0, twistSteps: 1}, shape)
    shape = rotateX(Math.PI/2, shape)
    shape = translateY(thickness*1.5/2, shape)
    shape = translateZ(height, shape)
    return shape
}

const frameShell = () => {
    let shape
    shape = polygon({points: [[-width/2,0], [width/2,0], [0,height]]})
    let outer = expand({delta: thickness, corners: 'round'}, shape)
    shape = subtract(outer, shape)
    shape = extrudeLinear({height: extendedWidth, twistAngle: 0, twistSteps: 1}, shape)
    shape = rotateX(Math.PI/2, shape)
    shape = translateY(extendedWidth/2, shape)
    return shape
}

module.exports = {
    main:  () => {
        let shape
        shape = subtract(frameShell(), door())
        let rotatedCopy = rotateZ(Math.PI/2, shape)
        shape = union(shape, rotatedCopy)
        shape = union(shape, topHook())
        return shape
    }
}