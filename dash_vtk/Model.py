# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class Model(Component):
    """A Model component.
GeometryRepresentation is responsible to convert a vtkPolyData into rendering
It takes the following set of properties:
  - actor: Properties to assign to the vtkActor
  - mapper: Properties to assign to the vtkMapper
  - property: Properties to assign to the vtkProperty (actor.getProperty())
  - colorMapPreset: Name of the preset to use for controlling the color mapping
  - colorDataRange: Range to use for the color scale

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID used to identify this component.

- actor (dict; optional):
    Properties to set to the actor.

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

- picks (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

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
    Show hide scalar bar for that representation."""
    _children_props = ['picks', 'picks']
    _base_nodes = ['picks', 'picks', 'children']
    _namespace = 'dash_vtk'
    _type = 'Model'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        actor: typing.Optional[dict] = None,
        mapper: typing.Optional[dict] = None,
        property: typing.Optional[dict] = None,
        colorMapPreset: typing.Optional[str] = None,
        colorDataRange: typing.Optional[typing.Sequence[NumberType]] = None,
        showCubeAxes: typing.Optional[bool] = None,
        cubeAxesStyle: typing.Optional[dict] = None,
        showScalarBar: typing.Optional[bool] = None,
        scalarBarTitle: typing.Optional[str] = None,
        scalarBarStyle: typing.Optional[dict] = None,
        picks: typing.Optional[typing.Union[typing.Sequence[ComponentType], ComponentType]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'actor', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'picks', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'actor', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'picks', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Model, self).__init__(children=children, **args)

setattr(Model, "__init__", _explicitize_args(Model.__init__))
