# AUTO GENERATED FILE - DO NOT EDIT

#' @export
vtkPickGroup <- function(children=NULL, id=NULL, actor=NULL, axisIdList=NULL, colorDataRange=NULL, colorMapPreset=NULL, cubeAxesStyle=NULL, mapper=NULL, offsetList=NULL, property=NULL, scalarBarStyle=NULL, scalarBarTitle=NULL, showCubeAxes=NULL, showScalarBar=NULL, vtkClass=NULL, vtkClassState=NULL) {
    
    props <- list(children=children, id=id, actor=actor, axisIdList=axisIdList, colorDataRange=colorDataRange, colorMapPreset=colorMapPreset, cubeAxesStyle=cubeAxesStyle, mapper=mapper, offsetList=offsetList, property=property, scalarBarStyle=scalarBarStyle, scalarBarTitle=scalarBarTitle, showCubeAxes=showCubeAxes, showScalarBar=showScalarBar, vtkClass=vtkClass, vtkClassState=vtkClassState)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PickGroup',
        namespace = 'dash_vtk',
        propNames = c('children', 'id', 'actor', 'axisIdList', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'offsetList', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar', 'vtkClass', 'vtkClassState'),
        package = 'dashVtk'
        )

    structure(component, class = c('dash_component', 'list'))
}
