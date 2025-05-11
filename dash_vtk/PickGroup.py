# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PickGroup(Component):
    """A PickGroup component.
PickGroup is responsible for creating glyphs at specified pick positions
It takes the following set of properties:
  - axisIds: Array of axis ids to use for the pick group
  - offsets: Array of offsets to use for the pick group
  - property: Properties to assign to the vtkProperty (actor.getProperty())
  - colorMapPreset: Name of the preset to use for controlling the color mapping
  - colorDataRange: Range to use for the color scale

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID used to identify this component.

- actor (dict; optional):
    Properties to set to the actor.

- axisIdList (list of list of numberss; optional)

- colorDataRange (list of numbers; default [0, 1]):
    Data range use for the colorMap.

- colorMapPreset (string; default 'erdc_rainbow_bright'):
    Preset name for the lookup table color map.

- cubeAxesStyle (dict; optional):
    Configure cube Axes style by overriding the set of properties
    defined
    https://github.com/Kitware/vtk-js/blob/HEAD/Sources/Rendering/Core/CubeAxesActor/index.js#L703-L719.

- mapper (dict; optional):
    Properties to set to the actor.

- offsetList (list of list of numberss; optional)

- property (dict; optional):
    Properties to set to the actor.property.

- scalarBarStyle (dict; optional):
    Configure scalar bar style by overriding the set of properties
    defined
    https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ScalarBarActor/index.js#L776-L796.

- scalarBarTitle (string; default ''):
    Use given string as title for scalar bar. By default it is empty
    (no title).

- showCubeAxes (boolean; default False):
    Show/Hide Cube Axes for the given representation.

- showScalarBar (boolean; default False):
    Show hide scalar bar for that representation.

- vtkClass (string; default 'vtkSphereSource')

- vtkClassState (dict; default {  radius: 0.05,  center: [0, 0, 0],})"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'PickGroup'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, actor=Component.UNDEFINED, mapper=Component.UNDEFINED, property=Component.UNDEFINED, colorMapPreset=Component.UNDEFINED, colorDataRange=Component.UNDEFINED, showCubeAxes=Component.UNDEFINED, cubeAxesStyle=Component.UNDEFINED, showScalarBar=Component.UNDEFINED, scalarBarTitle=Component.UNDEFINED, scalarBarStyle=Component.UNDEFINED, vtkClass=Component.UNDEFINED, vtkClassState=Component.UNDEFINED, axisIdList=Component.UNDEFINED, offsetList=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'actor', 'axisIdList', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'offsetList', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar', 'vtkClass', 'vtkClassState']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'actor', 'axisIdList', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'offsetList', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar', 'vtkClass', 'vtkClassState']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(PickGroup, self).__init__(children=children, **args)
