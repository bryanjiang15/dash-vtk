# AUTO GENERATED FILE - DO NOT EDIT

export vtk_pickgroup

"""
    vtk_pickgroup(;kwargs...)
    vtk_pickgroup(children::Any;kwargs...)
    vtk_pickgroup(children_maker::Function;kwargs...)


A PickGroup component.
PickGroup is responsible for creating glyphs at specified pick positions
It takes the following set of properties:
  - axisIds: Array of axis ids to use for the pick group
  - offsets: Array of offsets to use for the pick group
  - property: Properties to assign to the vtkProperty (actor.getProperty())
  - colorMapPreset: Name of the preset to use for controlling the color mapping
  - colorDataRange: Range to use for the color scale
Keyword arguments:
- `children` (Array of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)
- `id` (String; optional): The ID used to identify this component.
- `actor` (Dict; optional): Properties to set to the actor
- `axisIdList` (Array of Array of Realss; optional)
- `colorDataRange` (Array of Reals; optional): Data range use for the colorMap
- `colorMapPreset` (String; optional): Preset name for the lookup table color map
- `cubeAxesStyle` (Dict; optional): Configure cube Axes style by overriding the set of properties defined
https://github.com/Kitware/vtk-js/blob/HEAD/Sources/Rendering/Core/CubeAxesActor/index.js#L703-L719
- `mapper` (Dict; optional): Properties to set to the actor
- `offsetList` (Array of Array of Realss; optional)
- `property` (Dict; optional): Properties to set to the actor.property
- `scalarBarStyle` (Dict; optional): Configure scalar bar style by overriding the set of properties defined
https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ScalarBarActor/index.js#L776-L796
- `scalarBarTitle` (String; optional): Use given string as title for scalar bar. By default it is empty (no title).
- `showCubeAxes` (Bool; optional): Show/Hide Cube Axes for the given representation
- `showScalarBar` (Bool; optional): Show hide scalar bar for that representation
- `vtkClass` (String; optional)
- `vtkClassState` (Dict; optional)
"""
function vtk_pickgroup(; kwargs...)
        available_props = Symbol[:children, :id, :actor, :axisIdList, :colorDataRange, :colorMapPreset, :cubeAxesStyle, :mapper, :offsetList, :property, :scalarBarStyle, :scalarBarTitle, :showCubeAxes, :showScalarBar, :vtkClass, :vtkClassState]
        wild_props = Symbol[]
        return Component("vtk_pickgroup", "PickGroup", "dash_vtk", available_props, wild_props; kwargs...)
end

vtk_pickgroup(children::Any; kwargs...) = vtk_pickgroup(;kwargs..., children = children)
vtk_pickgroup(children_maker::Function; kwargs...) = vtk_pickgroup(children_maker(); kwargs...)

