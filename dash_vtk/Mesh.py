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


class Mesh(Component):
    """A Mesh component.
Mesh is exposing a vtkPolyData to a downstream filter
It takes the following set of properties:
  - state: { mesh: { ...polydata-props }, field: { ...dataArray } }

Keyword arguments:

- id (string; optional):
    The ID used to identify this component.

- port (number; default 0):
    downstream connection port.

- state (dict; default {  mesh: { points: [] },}):
    State of the mesh."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'Mesh'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        port: typing.Optional[NumberType] = None,
        state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'port', 'state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'port', 'state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Mesh, self).__init__(**args)

setattr(Mesh, "__init__", _explicitize_args(Mesh.__init__))
