import math
width = 120
extendedWidth = width*1.1
height = 85
thickness = 2.0


def makeFrame(partName, plane = 'YZ_Plane'):
    baseFrameName = "{partName}_BaseFrameName".format(partName=partName)
    App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject', baseFrameName)
    App.getDocument('Unnamed').getObject(baseFrameName).Support = (App.getDocument('Unnamed').getObject(plane),[''])
    App.getDocument('Unnamed').getObject(baseFrameName).MapMode = 'FlatFace'

    ActiveSketch = App.getDocument('Unnamed').getObject(baseFrameName)

    PointAIdx = ActiveSketch.addGeometry(Part.Point(App.Vector(1,1,0)))
    PointBIdx = ActiveSketch.addGeometry(Part.Point(App.Vector(0,2,0)))
    PointCIdx = ActiveSketch.addGeometry(Part.Point(App.Vector(0,3,0)))

    def addLine(pointIdx1, pointIdx2):
        point1 = ActiveSketch.Geometry[pointIdx1]
        point2 = ActiveSketch.Geometry[pointIdx2]
        lineIdx = ActiveSketch.addGeometry(Part.LineSegment(App.Vector(point1.X, point1.Y,0),App.Vector(point2.X,point2.Y,0)),False)
        ActiveSketch.addConstraint(Sketcher.Constraint('Coincident',lineIdx,1,pointIdx1,1))
        ActiveSketch.addConstraint(Sketcher.Constraint('Coincident',lineIdx,2,pointIdx2,1))
        return lineIdx

    LineABIdx = addLine(PointAIdx, PointBIdx)
    LineBCIdx = addLine(PointBIdx, PointCIdx)
    LineCAIdx = addLine(PointCIdx, PointAIdx)

    ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal',LineABIdx))
    ActiveSketch.addConstraint(Sketcher.Constraint('Distance',LineABIdx,width))
    ActiveSketch.addConstraint(Sketcher.Constraint('PointOnObject',LineABIdx,1,-1))
    ActiveSketch.addConstraint(Sketcher.Constraint('DistanceX',PointBIdx,1,-1,1,width/2))
    ActiveSketch.addConstraint(Sketcher.Constraint('PointOnObject',PointCIdx,1,-2))
    ActiveSketch.addConstraint(Sketcher.Constraint('Distance',PointCIdx,1,LineABIdx,height))

    baseFrameOffset = "{partName}_BaseFrameOffset".format(partName=partName)
    App.ActiveDocument.addObject("Part::Offset2D",baseFrameOffset)
    currentOffset = App.getDocument('Unnamed').getObject(baseFrameOffset)
    currentOffset.Source = App.getDocument('Unnamed').getObject(baseFrameName)
    currentOffset.Value = thickness
    currentOffset.Fill = True

    baseFrameSolid = "{partName}_BaseFrameSolid".format(partName=partName)
    App.getDocument('Unnamed').addObject('Part::Extrusion',baseFrameSolid)
    f = App.getDocument('Unnamed').getObject(baseFrameSolid)
    f.Base = currentOffset
    f.DirMode = "Normal"
    f.LengthFwd = extendedWidth
    if plane == 'YZ_Plane':
        f.Placement.Base = App.Vector(-extendedWidth/2,0,0)
    else:
        f.Placement.Base = App.Vector(0, -extendedWidth/2,0)


# makeFrame('initial')
# makeFrame('copy', 'XZ_Plane')

def makeSketch(sketchName, plane = 'YZ_Plane', points=[], constraints=[], segments={}):
    partName = sketchName
    plane = 'YZ_Plane'
    baseFrameName = sketchName
    App.getDocument('Unnamed').getObject('Body').newObject('Sketcher::SketchObject', baseFrameName)
    App.getDocument('Unnamed').getObject(baseFrameName).Support = (App.getDocument('Unnamed').getObject(plane),[''])
    App.getDocument('Unnamed').getObject(baseFrameName).MapMode = 'FlatFace'

    ActiveSketch = App.getDocument('Unnamed').getObject(baseFrameName)

    def addLine(pointIdx1, pointIdx2):
        point1 = ActiveSketch.Geometry[pointIdx1]
        point2 = ActiveSketch.Geometry[pointIdx2]
        lineIdx = ActiveSketch.addGeometry(Part.LineSegment(App.Vector(point1.X, point1.Y,0),App.Vector(point2.X,point2.Y,0)),False)
        ActiveSketch.addConstraint(Sketcher.Constraint('Coincident',lineIdx,1,pointIdx1,1))
        ActiveSketch.addConstraint(Sketcher.Constraint('Coincident',lineIdx,2,pointIdx2,1))
        return lineIdx
    
    def addArc(pointIdx1, pointIdx2):
        # radius = 1000
        point1 = ActiveSketch.Geometry[pointIdx1]
        point2 = ActiveSketch.Geometry[pointIdx2]
        centerX = (point1.X + point2.X)/2
        centerY = (point1.Y + point2.Y)/2
        radius = math.sqrt((point1.X - point2.X)**2 + (point1.Y - point2.Y)**2)/2
        # lineIdx = ActiveSketch.addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(point1.X,point1.Y,0),App.Vector(0,0,1),radius),point2.X,point2.Y),False)
        # lineIdx = ActiveSketch.addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.01,0.02,0),App.Vector(0,0,1),100),1.03,1.04),False)
        lineIdx = ActiveSketch.addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(centerX,centerY,0),App.Vector(0,0,1),radius),3.871755,0.80),False)
        # lineIdx = ActiveSketch.addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.01,0.02,0),App.Vector(0,0,1),100),1.03,1.04),False)
        ActiveSketch.addConstraint(Sketcher.Constraint('Coincident',lineIdx,1,pointIdx1,1))
        ActiveSketch.addConstraint(Sketcher.Constraint('Coincident',lineIdx,2,pointIdx2,1))
        return lineIdx

    myMap = {}
    print(myMap)

# App.getDocument('Unnamed').getObject('hookBase').addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.01,20.02,0),App.Vector(0,0,1),1000),21.03,21.04),False)
# App.getDocument('Unnamed').getObject('hookBase').addConstraint(Sketcher.Constraint('Coincident',10,1,3,1)) 
# App.getDocument('Unnamed').getObject('hookBase').addConstraint(Sketcher.Constraint('Coincident',10,2,4,1))

    for index in range(len(points)):
        xPoint = 0.5 if index == 0 else index
        yPoint = index
        pointIdx = ActiveSketch.addGeometry(Part.Point(App.Vector(xPoint,yPoint,0)))
        myMap[points[index]['name']] = pointIdx
        points[index]['index'] = pointIdx
        print(index)

    print(points)
    print(myMap)

    def getAlternateName(name):
        if name is None:
            return None
        nameParts = name.split("-")
        return nameParts[1] + '-' + nameParts[0]

    lineMap = {}
    for index in range(len(points)):
        previousIndex = len(points) - 1 if index == 0 else index - 1
        previousPointIndex = points[previousIndex]['index']
        currentPointIndex = points[index]['index']
        previousPointName = points[previousIndex]['name']
        currentPointName = points[index]['name']
        segName = previousPointName + '-' + currentPointName
        arcSegment = segments.get(segName) or segments.get(getAlternateName(segName))
        if arcSegment is None:
            lineIdx = addLine(previousPointIndex, currentPointIndex)
            lineMap["{previousPointName}-{currentPointName}".format(previousPointName=previousPointName, currentPointName=currentPointName)] = lineIdx
            print(lineIdx)
        else:
            radius = 100
            lineIdx = addArc(previousPointIndex, currentPointIndex)
            print(lineIdx)
            lineMap["{previousPointName}-{currentPointName}".format(previousPointName=previousPointName, currentPointName=currentPointName)] = lineIdx
            print('MAKE ARC!!!')
        

    print(lineMap)


    def findLineIndex(lineName = ""):
        if lineName is None:
            return None
        alternateName = getAlternateName(lineName)
        return lineMap.get(lineName) or lineMap.get(alternateName)

    for constraint in constraints:
        line = constraint.get('line')
        point = constraint.get('point')
        conType = constraint['type']
        lineIdx = findLineIndex(line)
        pointIdx = myMap.get(point)
        print('contype', conType, 'line and index', line, lineIdx, 'point and index', point, pointIdx)
        if conType == 'Horizontal':
            idx = ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal',lineIdx))
        elif conType == 'Distance':
            distance = constraint['value']
            ActiveSketch.addConstraint(Sketcher.Constraint('Distance',lineIdx,distance))
        elif conType == 'OnXAxis':
            ActiveSketch.addConstraint(Sketcher.Constraint('PointOnObject',lineIdx,1,-1))
        elif conType == 'OriginXDistance':
            xAxisIdx = -1
            distance = constraint['value']
            ActiveSketch.addConstraint(Sketcher.Constraint('DistanceX',pointIdx,1,xAxisIdx,1,distance))
        elif conType == 'OnYAxis':
            yAxisIdx = -2
            ActiveSketch.addConstraint(Sketcher.Constraint('PointOnObject',pointIdx,1,yAxisIdx))
        elif conType == 'perpendicularDistance':
            distance = constraint['value']
            ActiveSketch.addConstraint(Sketcher.Constraint('Distance',pointIdx,1,lineIdx,distance))
        elif conType == 'HorizontalPoints':
            points = constraint['points']
            idx = ActiveSketch.addConstraint(Sketcher.Constraint('Horizontal',myMap.get(points[0]),1,myMap.get(points[1]),1))
        elif conType == 'Tangents':
            tangents = constraint['tangents']
            for points in tangents:
                line1Idx  = findLineIndex(points[0] + '-' + points[1])
                line2Idx  = findLineIndex(points[1] + '-' + points[2])
                ActiveSketch.addConstraint(Sketcher.Constraint('Tangent',line1Idx,line2Idx))
        elif conType == 'radii':
            radii = constraint['radii']
            for radius in radii:
                lineIdx = findLineIndex(radius[0])
                ActiveSketch.addConstraint(Sketcher.Constraint('Radius', lineIdx, radius[1]))

            # lines = constraint['lines']
            # line1Idx = lineIdx = findLineIndex(lines[0])
            # line2Idx = lineIdx = findLineIndex(lines[1])
            # ActiveSketch.addConstraint(Sketcher.Constraint('Tangent',line1Idx,line2Idx))

def makeFrame2(partName, plane = 'YZ_Plane'):
    points = [
        {
            'name': 'baseR',
        },
        {
            'name': 'baseL',
        },
        {
            'name': 'top',
        },
    ]

    constraints = [
        {
            'type': 'Horizontal',
            'line': 'baseR-baseL'
        },
        {
            'type': 'Distance',
            'value': width,
            'line': 'baseR-baseL'
        },
        {
            'type': 'OnXAxis',
            'line': 'baseR-baseL'
        },
        {
            'type': 'OriginXDistance',
            'value': width/2,
            'point': 'baseR',
        },
        {
            'type': 'OnYAxis',
            'point': 'top',
        },
        {
            'type': 'perpendicularDistance',
            'value': height,
            'point': 'top',
            'line': 'baseR-baseL'
        },
    ]
    baseFrameName = "{partName}_BaseFrameName".format(partName=partName)
    makeSketch(baseFrameName, plane, points, constraints)

    baseFrameOffset = "{partName}_BaseFrameOffset".format(partName=partName)
    App.ActiveDocument.addObject("Part::Offset2D",baseFrameOffset)
    currentOffset = App.getDocument('Unnamed').getObject(baseFrameOffset)
    currentOffset.Source = App.getDocument('Unnamed').getObject(baseFrameName)
    currentOffset.Value = thickness
    currentOffset.Fill = True

    baseFrameSolid = "{partName}_BaseFrameSolid".format(partName=partName)
    App.getDocument('Unnamed').addObject('Part::Extrusion',baseFrameSolid)
    f = App.getDocument('Unnamed').getObject(baseFrameSolid)
    f.Base = currentOffset
    f.DirMode = "Normal"
    f.LengthFwd = extendedWidth
    if plane == 'YZ_Plane':
        f.Placement.Base = App.Vector(-extendedWidth/2,0,0)
    else:
        f.Placement.Base = App.Vector(0, -extendedWidth/2,0)


points = [
    {
        'name': 'baseR',
        'constraint': 'AcuteTangent',
    },
    {
        'name': 'baseL',
        'constraint': 'AcuteTangent',
    },
    {
        'name': 'bottomFilletL',
        'constraint': 'Tangent',
    },
    {
        'name': 'TopFilletL',
        'constraint': 'Tangent',
    },
    {
        'name': 'TopFilletR',
        'constraint': 'Tangent',
    },
    {
        'name': 'bottomFilletR',
        'constraint': 'Tangent',
    },
]

constraints = [
        {
            'type': 'radii',
            'radii': [
                ['baseL-bottomFilletL', 5],
                ['baseR-bottomFilletR', 5],
                ['TopFilletL-TopFilletR', 5],
            ]
        },
        {
            'type': 'Horizontal',
            'line': 'baseR-baseL',
        },
        {
            'type': 'HorizontalPoints',
            'points': ['bottomFilletL', 'bottomFilletR'],
        },
        {
            'type': 'HorizontalPoints',
            'points': ['TopFilletL', 'TopFilletR'],
        },
        {
            'type': 'Tangents',
            'tangents': [
                ['baseR', 'baseL', 'bottomFilletL'],
                ['baseL', 'bottomFilletL', 'TopFilletL'],
                ['bottomFilletL', 'TopFilletL', 'TopFilletR'],
                ['TopFilletL', 'TopFilletR', 'bottomFilletR'],
                ['TopFilletR', 'bottomFilletR', 'baseR'],
                ['bottomFilletR', 'baseR', 'baseL'],
            ],
        },
        # {
        #     'type': 'Distance',
        #     'value': width,
        #     'line': 'baseR-baseL'
        # },
        # {
        #     'type': 'OnXAxis',
        #     'line': 'baseR-baseL'
        # },
        # {
        #     'type': 'OriginXDistance',
        #     'value': width/2,
        #     'point': 'baseR',
        # },
        # {
        #     'type': 'OnYAxis',
        #     'point': 'top',
        # },
        # {
        #     'type': 'perpendicularDistance',
        #     'value': height,
        #     'point': 'top',
        #     'line': 'baseR-baseL'
        # },
    ]

segments = {
    'bottomFilletR-baseR': 'arc',
    'baseL-bottomFilletL': 'arc',
    'TopFilletL-TopFilletR': 'arc',
}


# makeFrame2('initial')
# makeFrame('copy', 'XZ_Plane')

makeSketch('hookBase', 'YZ_Plane', points, constraints, segments)

App.ActiveDocument.recompute()
