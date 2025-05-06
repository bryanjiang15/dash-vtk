# AUTO GENERATED FILE - DO NOT EDIT

export vtk_model

"""
    vtk_model(;kwargs...)
    vtk_model(children::Any;kwargs...)
    vtk_model(children_maker::Function;kwargs...)


A Model component.
GeometryRepresentation is responsible to convert a vtkPolyData into rendering
It takes the following set of properties:
  - actor: Properties to assign to the vtkActor
  - mapper: Properties to assign to the vtkMapper
  - property: Properties to assign to the vtkProperty (actor.getProperty())
  - colorMapPreset: Name of the preset to use for controlling the color mapping
  - colorDataRange: Range to use for the color scale
Keyword arguments:
- `children` (Array of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)
- `id` (String; optional): The ID used to identify this component.
- `actor` (Dict; optional): Properties to set to the actor
- `colorDataRange` (Array of Reals; optional): Data range use for the colorMap
- `colorMapPreset` (String; optional): Preset name for the lookup table color map
- `cubeAxesStyle` (Dict; optional): Configure cube Axes style by overriding the set of properties defined
https://github.com/Kitware/vtk-js/blob/HEAD/Sources/Rendering/Core/CubeAxesActor/index.js#L703-L719
- `mapper` (Dict; optional): Properties to set to the actor
- `picks` (Array of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)
- `property` (Dict; optional): Properties to set to the actor.property
- `scalarBarStyle` (Dict; optional): Configure scalar bar style by overriding the set of properties defined
https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ScalarBarActor/index.js#L776-L796
- `scalarBarTitle` (String; optional): Use given string as title for scalar bar. By default it is empty (no title).
- `showCubeAxes` (Bool; optional): Show/Hide Cube Axes for the given representation
- `showScalarBar` (Bool; optional): Show hide scalar bar for that representation
"""
function vtk_model(; kwargs...)
        available_props = Symbol[:children, :id, :actor, :colorDataRange, :colorMapPreset, :cubeAxesStyle, :mapper, :picks, :property, :scalarBarStyle, :scalarBarTitle, :showCubeAxes, :showScalarBar]
        wild_props = Symbol[]
        return Component("vtk_model", "Model", "dash_vtk", available_props, wild_props; kwargs...)
end

vtk_model(children::Any; kwargs...) = vtk_model(;kwargs..., children = children)
vtk_model(children_maker::Function; kwargs...) = vtk_model(children_maker(); kwargs...)

