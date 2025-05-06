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


class Calculator(Component):
    """A Calculator component.
Calculator is exposing a source or filter to a downstream filter
It takes the following set of properties:
  - name: 'scalars'    // name of the generated field
  - location: 'POINT'  // POINT/CELL
  - arrays: []         // Name of array to have access in formula
  - formula: fn

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; optional):
    The ID used to identify this component.

- arrays (list of strings; optional):
    List of fields you want available for your formula.

- location (string; default 'POINT'):
    Field location [POINT, CELL, COORDINATE, SCALARS, ].

- name (string; default 'scalars'):
    Field name.

- port (number; default 0):
    downstream connection port."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'Calculator'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        port: typing.Optional[NumberType] = None,
        name: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        arrays: typing.Optional[typing.Sequence[str]] = None,
        formula: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'arrays', 'location', 'name', 'port']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'arrays', 'location', 'name', 'port']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Calculator, self).__init__(children=children, **args)

setattr(Calculator, "__init__", _explicitize_args(Calculator.__init__))
