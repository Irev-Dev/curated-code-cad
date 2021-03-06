width = 120
extendedWidth = width*1.1
height = 85
thickness = 2.0

def makeSketch(sketchName, plane = 'YZ_Plane', points=[], constraints=[]):
    partName = sketchName
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

    myMap = {}
    for index in range(len(points)):
        xPoint = 0.5 if index == 0 else index
        yPoint = index
        pointIdx = ActiveSketch.addGeometry(Part.Point(App.Vector(xPoint,yPoint,0)))
        myMap[points[index]['name']] = pointIdx
        points[index]['index'] = pointIdx


    lineMap = {}
    for index in range(len(points)):
        previousIndex = len(points) - 1 if index == 0 else index - 1
        previousPointIndex = points[previousIndex]['index']
        currentPointIndex = points[index]['index']
        lineIdx = addLine(previousPointIndex, currentPointIndex)
        previousPointName = points[previousIndex]['name']
        currentPointName = points[index]['name']
        lineMap["{previousPointName}-{currentPointName}".format(previousPointName=previousPointName, currentPointName=currentPointName)] = lineIdx

    def findLineIndex(lineName = ""):
        if lineName is None:
            return None
        nameParts = lineName.split("-")
        alternateName = nameParts[1] + '-' + nameParts[0]
        return lineMap.get(lineName) or lineMap.get(alternateName)

    for constraint in constraints:
        line = constraint.get('line')
        point = constraint.get('point')
        conType = constraint['type']
        lineIdx = findLineIndex(line)
        pointIdx = myMap.get(point)
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

def makeFrame(partName, plane = 'YZ_Plane'):
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

makeFrame('initial')
makeFrame('copy', 'XZ_Plane')

App.ActiveDocument.recompute()
