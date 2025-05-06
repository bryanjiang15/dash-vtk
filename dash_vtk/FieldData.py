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


class FieldData(Component):
    """A FieldData component.
FieldData is exposing a FieldData to a downstream element

Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'FieldData'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        **kwargs
    ):
        self._prop_names = ['children']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FieldData, self).__init__(children=children, **args)

setattr(FieldData, "__init__", _explicitize_args(FieldData.__init__))
