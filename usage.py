import dash_vtk
import dash
from dash.dependencies import Input, Output
from dash import html, callback, no_update

import dash_vtk.Pick

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"width": "100%", "height": "calc(100vh - 16px)"},
    children=[
        dash_vtk.View(
            id="view",
            #cameraFocalPoint=[0, 10, 0],
            pickingModes=["hover", "click"],
            children=[
                dash_vtk.GeometryRepresentation(
                    property={
                        "color": [0.4, 0.4, 0.4],
                    },
                    actor={
                        "position": [0.5, 0.2, 0.4],
                        "scale": [0.3, 0.3, 0.3],
                    },
                    children=[
                        dash_vtk.Reader(
                            vtkClass="vtkOBJReader",
                            url="https://kitware.github.io/vtk-js-datasets/data/obj-mtl/star-wars-vader-tie-fighter.obj",
                        ),
                        dash_vtk.GeometryRepresentation(
                            property={
                                "color": [1, 0, 0],
                            },
                            actor={
                                "position": [1, 0.2, 0.4],
                                "scale": [0.3, 0.3, 0.3],
                            },
                        )
                    ],
                ),
                dash_vtk.Model(
                    id="rep",
                    property={
                        "pointSize": 10,
                    },
                    colorDataRange=[0, 3],
                    # showScalarBar=True,
                    # scalarBarTitle="Temperature",
                    mapper={
                        "colorByArrayName": "Temperature",
                        "scalarMode": 3,
                        "interpolateScalarsBeforeMapping": True,
                    },
                    children=[
                        dash_vtk.PolyData(
                            id="square",
                            points=[0, 0, 0, 10, 0, 0, 10, 10, 0, 0, 10, 0],
                            polys=[4, 0, 1, 2, 3],
                            children=[
                                dash_vtk.PointData(
                                    children=[
                                        dash_vtk.DataArray(
                                            name="Temperature", values=[0, 3, 2, 1]
                                        )
                                    ]
                                )
                            ],
                        ),
                    ],
                    picks=[
                        dash_vtk.Pick(
                            id=f"pick1",
                            vtkClass = "vtkSphereSource",
                            vtkClassState = {
                                "radius": 0.1,
                            },
                            axisIds=[0, 1, 3],
                            offsets=[0, 0, 0],
                        ),
                        dash_vtk.Pick(
                            id=f"pick2",
                            vtkClass = "vtkSphereSource",
                            vtkClassState = {
                                "radius": 0.1,
                            },
                            axisIds=[1, 2, 3],
                            offsets=[0, 0, 0],
                        ),
                        dash_vtk.Pick(
                            id=f"pick3",
                            vtkClass = "vtkSphereSource",
                            vtkClassState = {
                                "radius": 0.1,
                            },
                            axisIds=[2, 3, 0],
                            offsets=[0, 0, 0],
                        ),
                        dash_vtk.Pick(
                            id=f"pick4",
                            vtkClass = "vtkSphereSource",
                            vtkClassState = {
                                "radius": 0.1,
                            },
                            axisIds=[3, 0, 1],
                            offsets=[0, 0, 0],
                        ),
                    ]
                ),
            ],
        ),
        html.Div(id="output"),
    ],
)

@callback(
    Output("square", "points"),
    Output("view", "focalPoint"),
    Input("view", "clickInfo"),
)
def move_square(click_info):
    if click_info is None:
        return no_update, no_update

    # Extract the click position
    x, y, z = click_info.get("worldPosition", [0, 0, 0])

    # Update the square's points based on the click position
    new_points = [
        x, y, z,
        x + 1, y, z,
        x + 1, y + 1, z,
        x, y + 1, z,
    ]
    return no_update, [x, y, z]

if __name__ == "__main__":
    app.run(debug=True)
