# AUTO GENERATED FILE - DO NOT EDIT

#' @export
vtkPick <- function(children=NULL, id=NULL, actor=NULL, axisIds=NULL, colorDataRange=NULL, colorMapPreset=NULL, cubeAxesStyle=NULL, mapper=NULL, offsets=NULL, property=NULL, scalarBarStyle=NULL, scalarBarTitle=NULL, showCubeAxes=NULL, showScalarBar=NULL, vtkClass=NULL, vtkClassState=NULL) {
    
    props <- list(children=children, id=id, actor=actor, axisIds=axisIds, colorDataRange=colorDataRange, colorMapPreset=colorMapPreset, cubeAxesStyle=cubeAxesStyle, mapper=mapper, offsets=offsets, property=property, scalarBarStyle=scalarBarStyle, scalarBarTitle=scalarBarTitle, showCubeAxes=showCubeAxes, showScalarBar=showScalarBar, vtkClass=vtkClass, vtkClassState=vtkClassState)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Pick',
        namespace = 'dash_vtk',
        propNames = c('children', 'id', 'actor', 'axisIds', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'offsets', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar', 'vtkClass', 'vtkClassState'),
        package = 'dashVtk'
        )

    structure(component, class = c('dash_component', 'list'))
}
