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
    ActiveSketch.addConstraint(Sketcher.Constraint('DistanceX',1,1,-1,1,width/2))
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


makeFrame('initial')
makeFrame('copy', 'XZ_Plane')

App.ActiveDocument.recompute()
