# Curated Code Cad ⚙️ 👩‍🔧

<img src="https://raw.githubusercontent.com/Irev-Dev/repo-images/main/images/CURATED-CODE-CAD-BANNER2.jpg">

#### [See the web page version](https://kurthutten.com/blog/curated-code-cad/)

You like 3d modelling, but don't like using a GUI. Good for you! But which modeller do you use??
You'll have to figure that out for yourself, but here are some options.

## Special mention

### [OpenScad](http://www.openscad.org/)
- [Repo](https://github.com/openscad/openscad)
- [Community](http://www.openscad.org/community.html)
- [Docs](http://www.openscad.org/documentation.html)
- License: GPL-2
- ~Online editor~

The rest of the packages are in alphabetical order, but OpenScad gets a special mention because it's the OG. Many of the projects below were inspired by OpenScad and is the most well-known choice. If you're new to code-cad this is the safest choice, even if only from tutorials and content perspective.

### [OpenCascade](https://www.opencascade.com/)
- [Repo](https://github.com/tpaviot/oce)
- [Community](https://dev.opencascade.org/)
- [Docs](https://old.opencascade.com/doc/occt-6.9.1/refman/html/index.html)
- License: LGPL-2.1
- ~Online editor~

It's a c++ library that a number the projects below wrap.

## Contributing

Know of a package that we missed? tell us with an issue or open up a PR.
The description for each package is pretty minimal at the moment. If you'd like to add more detail to any of them please go ahead.

## Here they are:

### [CadQuery](https://cadquery.readthedocs.io/en/latest/intro.html)
- [Repo](https://github.com/CadQuery/cadquery)
- [Community](https://discord.gg/qz3uAdF)
- [Docs](https://cadquery.readthedocs.io/en/latest/intro.html)
- License: Apache, 2.0
- ~Online editor~

CadQuery is a Python library that wraps and extends [OpenCascade](https://github.com/tpaviot/oce). It aims to let you model as "close as possible to how you’d describe the object to a human" .


    OpenCASCADE (OCCT) is a BRep kernel, which is a very powerful way to represent geometry. This is in contrast to OpenSCAD which uses the CSG kernel. Both approaches are great and people should use what they want, but I prefer working with BRep.
    Related to "close as possible to how you’d describe the object to a human" is the idea of "capturing design intent". For example, by using selectors instead of picking specific edges manually, the user can be sure the edges they intended to have fillets are always filleted, even if other aspects of the design changes.


### [CascadeStudio](https://zalo.github.io/CascadeStudio/)
- [Repo](https://github.com/zalo/CascadeStudio)
- ~Community~ repo says to use github issues
- ~Docs~
- License: MIT
- [Online editor](https://zalo.github.io/CascadeStudio/)

A javascript wrapper for [OpenCascade](https://github.com/tpaviot/oce) that runs in the browser. (OpenCascade can run in the browser when compiled to web-assembly).

### [Curv](http://www.curv3d.org/)
- [Repo](https://github.com/curv3d/curv)
- [Community](https://groups.google.com/d/forum/curv) (mailing list)
- [Docs](https://github.com/curv3d/curv/tree/master/docs)
- License: Apache, 2.0
- ~Online editor~

Curv is a programming language for creating art using mathematics. It’s a 2D and 3D geometric modelling tool that supports full colour, animation and 3D printing. It was inspired by OpenScad and [shadertoy](https://www.shadertoy.com/).

### [FreeCAD](https://www.freecadweb.org/)
- [Repo](https://github.com/FreeCAD/FreeCAD)
- [Community](https://forum.freecadweb.org/)
- [Docs](https://wiki.freecadweb.org/Getting_started)
- License: LGPLv2
- ~Online editor~

FreeCad is a more traditional CAD package that supports python scripting, Both for modelling as well as controlling the FreeCAD GUI itself. Not only that it has a built in [OpenScad workbench](https://wiki.freecadweb.org/OpenSCAD_Module) as well as an external [CadQurey workbench](https://wiki.freecadweb.org/CadQuery_Workbench), making it the best in this list at interoperability.
 
### [ImplicitCAD](http://www.implicitcad.org/)
- [Repo](https://github.com/colah/ImplicitCAD)
- ~Community~
- [Docs](http://www.implicitcad.org/docs/tutorial)
- License: AGPL-3
- [Online editor](http://www.implicitcad.org/editor)

Inspired by OpenScad with a very similar language, implemented in Haskell and includes the ability to write definitions in Haskell, instead of just OpenSCAD, and is part of an 'almost stack' of tools including ExplicitCAD (for a GUI), and HSlice (for an STL slicer).

### [JSCAD](www.jscad.xyz)
- [Repo](https://github.com/jscad/OpenJSCAD.org)
- [Community](https://openjscad.nodebb.com/)
- [Docs](https://openjscad.org/dokuwiki/doku.php?id=jscad_quick_reference)
- License: MIT
- [Online editor](https://openjscad.org/)

JSCAD (formally know as OpenJSCAD) provides a programmer’s approach to develop 3D models. In particular, this functionality is tuned towards creating precise models for 3D printing.

JSCAD provides the ability to:
- Create and manipulate 3D models, as well as 2D models
- Use JavaScript programming concepts, and libraries
- Save 3D models as STL (and other) formats

JSCAD is available as a:
- [Website](www.jscad.xyz)
- Command line application for backend processing
- User application
- Set of packages (libraries) for building custom applications

JSCAD allows anyone to create 3D (or 2D) designs by combining simple shapes. And any shape can be rotated, moved, scaled, etc. Complex shapes can be saved as parts, which can used later. And the final design can be exported into various standard formats, i.e. STL, DXF, SVG, etc.

### [libfive](http://libfive.com/)
- [Repo](https://github.com/libfive/libfive)
- [Community](https://lists.gnu.org/archive/html/guile-user/2016-08/msg00027.html) (mailing list)
- [Docs](https://libfive.com/examples/)
- License: Mozilla Public License 2.0 and GPL-2 or later
- ~Online editor~

libfive is a software library and set of tools for solid modelling, especially suited for parametric and procedural design. lisp based language, (so (you (((((can expect ) lots of brakets))))).

### [pythonOCC](http://www.pythonocc.org/)
- [Repo](https://github.com/tpaviot/pythonocc-core)
- ~Community~
- [Docs](http://www.pythonocc.org/category/documentation/)
- License: LGPL-3
- [Online editor](https://mybinder.org/v2/gh/tpaviot/pythonocc-binderhub/7.4.0)

Python-based, Also uses [OpenCascade](https://github.com/tpaviot/oce).

### [RapCAD](https://gilesbathgate.com/category/rapcad/)
- [Repo](https://github.com/GilesBathgate/RapCAD)
- ~Community~
- ~Docs~
- License: GPL-3
- ~Online editor~

Another project inspired by OpenScad. The author considers key differences to be procedural vs functional programming language style, (i.e variables can be modified) and the use of arbitrary precision arithmetic throughout (meaning there are no unexpected double/float rounding errors). There is a handy [feature matrix](https://github.com/GilesBathgate/RapCAD/blob/master/doc/feature_matrix.asciidoc) between RapCAD, OpenScad and ImplicitCad.

### [SolidPython](https://solidpython.readthedocs.io/en/latest/)
- [Repo](https://github.com/SolidCode/SolidPython)
- ~Community~
- [Docs](https://solidpython.readthedocs.io/en/latest/)
- License: GPL-2 or later
- ~Online editor~

Python-based library that wraps OpenScad, i.e. it outputs OpenScad code.

## Node editors / other

Not quiet Code-Cad, but they do embody much of the same thought process.

### [BlocksCAD](https://www.blockscad3d.com)
- [Repo](https://github.com/einsteinsworkshop/blockscad) I'm not 100% sure its connected to blockscad3d.com or not
- [Community](https://www.blockscad3d.com)
- [Docs](https://www.blockscad3d.com/training-resources)
- License: GPL-3
- [Online editor](https://www.blockscad3d.com)

### [DynFreeCAD](https://github.com/infeeeee/DynFreeCAD)
- [Repo](https://github.com/infeeeee/DynFreeCAD)
- [Community](https://forum.dynamobim.com/)
- [Docs](https://github.com/infeeeee/DynFreeCAD/wiki)
- License: MIT
- ~Online editor~

Works with FreeCad

### [Sverchok](https://github.com/nortikin/sverchok)
- [Repo](https://github.com/nortikin/sverchok)
- ~Community~
- [Docs](http://nikitron.cc.ua/sverch/html/main.html)
- License: GPL-3
- ~Online editor~

Add-on for blender. Sverchok is a powerful parametric tool for architects, allowing geometry to be programmed visually with nodes. 

## Proprietary

### [ShapeScript](https://apps.apple.com/us/app/shapescript/id1441135869?mt=12)

Mac App
