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


class View(Component):
    """A View component.
View is responsible to render vtk.js data.
It takes the following set of properties:
  - `background`: [0.2, 0.3, 0.4]
  - `cameraPosition`: [0, 0, 1]
  - `cameraViewUp`: [0, 1, 0]
  - `cameraParallelProjection`: false
  - `showOrientationAxes`: true

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional):
    List of representation to show.

- id (string; optional):
    The ID used to identify this component.

- background (list; default [0.2, 0.3, 0.4]):
    The color of the view background using 3 floating numbers between
    0-1 of Red, Green, Blue component.

- cameraParallelProjection (boolean; default False):
    Use parallel projection (default: False).

- cameraPosition (list; default [0, 0, 1]):
    Initial camera position from an object in [0,0,0].

- cameraViewUp (list; default [0, 1, 0]):
    Initial camera position from an object in [0,0,0].

- className (string; optional):
    Allow user to provide custom className associated to root element.

- clickInfo (dict; optional):
    Read-only prop. To use this, make sure that `pickingModes`
    contains `click`. This prop is updated when an element in the map
    is clicked. This contains the picking info describing the object
    being clicked on.

- focalPoint (list; default [0, 0, 0]):
    Initial camera focal point from an object in [0,0,0].

- hoverInfo (dict; optional):
    Read-only prop. To use this, make sure that `pickingModes`
    contains `hover`. This prop is updated when an element in the map
    is hovered. This contains the picking info describing the object
    being hovered.

- interactorSettings (list; default [  {    button: 1,    action: 'Rotate',  },  {    button: 2,    action: 'Pan',  },  {    button: 3,    action: 'Zoom',    scrollEnabled: True,  },  {    button: 1,    action: 'Pan',    shift: True,  },  {    button: 1,    action: 'Zoom',    alt: True,  },  {    button: 1,    action: 'ZoomToMouse',    control: True,  },  {    button: 1,    action: 'Roll',    alt: True,    shift: True,  },]):
    Configure the interactions.

- pickingModes (list of strings; optional):
    List of picking listeners to bind. The supported values are
    `click` and `hover`. By default it is disabled (empty array).

- showOrientationAxes (boolean; default True):
    Show/Hide orientation axes.

- triggerRender (number; default 0):
    Property use to trigger a render when changing.

- triggerResetCamera (number; default 0):
    Property use to trigger a resetCamera when changing."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'View'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        background: typing.Optional[typing.Sequence] = None,
        interactorSettings: typing.Optional[typing.Sequence] = None,
        cameraPosition: typing.Optional[typing.Sequence] = None,
        cameraViewUp: typing.Optional[typing.Sequence] = None,
        cameraParallelProjection: typing.Optional[bool] = None,
        focalPoint: typing.Optional[typing.Sequence] = None,
        triggerRender: typing.Optional[NumberType] = None,
        triggerResetCamera: typing.Optional[NumberType] = None,
        pickingModes: typing.Optional[typing.Sequence[str]] = None,
        clickInfo: typing.Optional[dict] = None,
        hoverInfo: typing.Optional[dict] = None,
        showOrientationAxes: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'background', 'cameraParallelProjection', 'cameraPosition', 'cameraViewUp', 'className', 'clickInfo', 'focalPoint', 'hoverInfo', 'interactorSettings', 'pickingModes', 'showOrientationAxes', 'style', 'triggerRender', 'triggerResetCamera']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'background', 'cameraParallelProjection', 'cameraPosition', 'cameraViewUp', 'className', 'clickInfo', 'focalPoint', 'hoverInfo', 'interactorSettings', 'pickingModes', 'showOrientationAxes', 'style', 'triggerRender', 'triggerResetCamera']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(View, self).__init__(children=children, **args)

setattr(View, "__init__", _explicitize_args(View.__init__))
