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


class ImageData(Component):
    """An ImageData component.
ImageData is exposing a vtkImageData to a downstream filter
It takes the following set of properties:
  - dimensions: [nx, ny, nz],
  - origin: [0, 0, 0]
  - spacing: [1, 1, 1]
  - direction: [
      1, 0, 0,
      0, 1, 0,
      0, 0, 1
    ]

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID used to identify this component.

- dimensions (list of numbers; default [1, 1, 1]):
    Number of points along x, y, z.

- direction (list of numbers; default [  1, 0, 0,  0, 1, 0,  0, 0, 1,]):
    3x3 matrix use to orient the image data.

- origin (list of numbers; default [0, 0, 0]):
    World coordinate of the lower left corner of your vtkImageData
    (i=0, j=0, k=0).

- port (number; default 0):
    downstream connection port.

- spacing (list of numbers; default [1, 1, 1]):
    Spacing along x, y, z between points in world coordinates."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'ImageData'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        port: typing.Optional[NumberType] = None,
        dimensions: typing.Optional[typing.Sequence[NumberType]] = None,
        spacing: typing.Optional[typing.Sequence[NumberType]] = None,
        origin: typing.Optional[typing.Sequence[NumberType]] = None,
        direction: typing.Optional[typing.Sequence[NumberType]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'dimensions', 'direction', 'origin', 'port', 'spacing']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'dimensions', 'direction', 'origin', 'port', 'spacing']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ImageData, self).__init__(children=children, **args)

setattr(ImageData, "__init__", _explicitize_args(ImageData.__init__))
