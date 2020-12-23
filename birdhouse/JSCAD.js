const { polygon, cylinder } = require('@jscad/modeling').primitives
const { extrudeLinear } = require('@jscad/modeling').extrusions
const { expand } = require('@jscad/modeling').expansions
const { union, subtract } = require('@jscad/modeling').booleans
const { translateY, translateZ, rotateX, rotateY, rotateZ } = require('@jscad/modeling').transforms

const getParameterDefinitions = () => {
    return [
        { name: 'width', type: 'slider', initial: 120, min: 50, max: 250, step: 5, caption: 'Width' },
        { name: 'height', type: 'slider', initial: 85, min: 40, max: 150, step: 5, caption: 'Height' },
        { name: 'holeR', type: 'slider', initial: 28, min: 10, max: 40, step: 2, caption: 'Door Radius' },
        { name: 'thickness', type: 'slider', initial: 2, min: 0.5, max: 5, step: 0.5, caption: 'Wall Thickness' },
        { name: 'hookHeight', type: 'slider', initial: 10, min: 8, max: 14, step: 2, caption: 'Hook Height' },
    ]
}

const door = ({
    width,
    holeR,
    thickness,
}) => {
    let shape
    shape = cylinder({radius: holeR, height: width*2})
    shape = rotateY(Math.PI/2, shape)
    shape = translateZ(holeR+thickness,shape)
    return shape
}
    
const topHook = ({
    width,
    height,
    thickness,
    hookHeight,
}) => {
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

const frameShell = ({
    width,
    height,
    thickness,
}) => {
    const extendedWidth = width*1.1
    let shape
    shape = polygon({points: [[-width/2,0], [width/2,0], [0,height]]})
    let outer = expand({delta: thickness, corners: 'round'}, shape)
    shape = subtract(outer, shape)
    shape = extrudeLinear({height: extendedWidth, twistAngle: 0, twistSteps: 1}, shape)
    shape = rotateX(Math.PI/2, shape)
    shape = translateY(extendedWidth/2, shape)
    return shape
}

const main = (params) => {
    let shape
    shape = subtract(frameShell(params), door(params))
    let rotatedCopy = rotateZ(Math.PI/2, shape)
    return union(shape, rotatedCopy, topHook(params))
}

module.exports = { main, getParameterDefinitions }
