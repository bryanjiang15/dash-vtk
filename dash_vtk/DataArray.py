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


class DataArray(Component):
    """A DataArray component.
DataArray is creating a vtkDataArray for the container fields
It takes the following set of properties:
  - type: 'Float32Array', 'Float64Array', 'Uint16Array', ...
  - values: [number, number, ...]
  - numberOfComponents: 1,
  - registration: 'addArray', 'setScalars', ...

Keyword arguments:

- id (string; optional):
    The ID used to identify this component.

- name (string; default 'scalars'):
    Field name.

- numberOfComponents (number; default 1):
    Number of components / Tuple size.

- registration (string; default 'addArray'):
    Name of the method to call on the fieldData (addArray, setScalars,
    setVectors...).

- type (string; default 'Float32Array'):
    Typed array name.

- values (list of numbers; optional):
    Actual values to use inside our array."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_vtk'
    _type = 'DataArray'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        type: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        values: typing.Optional[typing.Sequence[NumberType]] = None,
        numberOfComponents: typing.Optional[NumberType] = None,
        registration: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'name', 'numberOfComponents', 'registration', 'type', 'values']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'name', 'numberOfComponents', 'registration', 'type', 'values']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DataArray, self).__init__(**args)

setattr(DataArray, "__init__", _explicitize_args(DataArray.__init__))
