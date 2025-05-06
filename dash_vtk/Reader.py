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


class Reader(Component):
    """A Reader component.
Reader is exposing a reader to a downstream filter
It takes the following set of properties:
  - vtkClass: vtk.js reader class name
  - url: string
  - parseAsText: string
  - parseAsArrayBuffer: base64String

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID used to identify this component.

- parseAsArrayBuffer (string; optional):
    set binary data to process from base64 string.

- parseAsText (string; optional):
    set text data to process.

- port (number; default 0):
    downstream connection port.

- renderOnUpdate (boolean; default True):
    Automatically render on data loaded.

- resetCameraOnUpdate (boolean; default True):
    Automatically reset camera on data loaded.

- url (string; optional):
    set of url to fetch data from.

- vtkClass (string; default ''):
    vtkClass name."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'Reader'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        port: typing.Optional[NumberType] = None,
        vtkClass: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        parseAsText: typing.Optional[str] = None,
        parseAsArrayBuffer: typing.Optional[str] = None,
        renderOnUpdate: typing.Optional[bool] = None,
        resetCameraOnUpdate: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'parseAsArrayBuffer', 'parseAsText', 'port', 'renderOnUpdate', 'resetCameraOnUpdate', 'url', 'vtkClass']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'parseAsArrayBuffer', 'parseAsText', 'port', 'renderOnUpdate', 'resetCameraOnUpdate', 'url', 'vtkClass']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Reader, self).__init__(children=children, **args)

setattr(Reader, "__init__", _explicitize_args(Reader.__init__))
