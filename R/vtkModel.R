# AUTO GENERATED FILE - DO NOT EDIT

#' @export
vtkModel <- function(children=NULL, id=NULL, actor=NULL, colorDataRange=NULL, colorMapPreset=NULL, cubeAxesStyle=NULL, mapper=NULL, picks=NULL, property=NULL, scalarBarStyle=NULL, scalarBarTitle=NULL, showCubeAxes=NULL, showScalarBar=NULL) {
    
    props <- list(children=children, id=id, actor=actor, colorDataRange=colorDataRange, colorMapPreset=colorMapPreset, cubeAxesStyle=cubeAxesStyle, mapper=mapper, picks=picks, property=property, scalarBarStyle=scalarBarStyle, scalarBarTitle=scalarBarTitle, showCubeAxes=showCubeAxes, showScalarBar=showScalarBar)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Model',
        namespace = 'dash_vtk',
        propNames = c('children', 'id', 'actor', 'colorDataRange', 'colorMapPreset', 'cubeAxesStyle', 'mapper', 'picks', 'property', 'scalarBarStyle', 'scalarBarTitle', 'showCubeAxes', 'showScalarBar'),
        package = 'dashVtk'
        )

    structure(component, class = c('dash_component', 'list'))
}
