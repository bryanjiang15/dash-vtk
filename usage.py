import random
import dash_vtk
import dash
from dash.dependencies import Input, Output, State
from dash import html, callback, no_update, Patch

import dash_vtk.Pick

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"width": "100%", "height": "calc(100vh - 16px)"},
    children=[
        dash_vtk.View(
            id="view",
            background=[0.8, 0.9, 0.97],
            pickingModes=["hover", "click"],
            children=[
                dash_vtk.GeometryRepresentation(
                    id="ship",
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
                # dash_vtk.Model(
                #     id="rep",
                #     property={
                #         "pointSize": 10,
                #     },
                #     colorDataRange=[0, 3],
                #     # showScalarBar=True,
                #     # scalarBarTitle="Temperature",
                #     mapper={
                #         "colorByArrayName": "Temperature",
                #         "scalarMode": 3,
                #         "interpolateScalarsBeforeMapping": True,
                #     },
                #     children=[
                #         dash_vtk.PolyData(
                #             id="square",
                #             points=[0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
                #             polys=[4, 0, 1, 2, 3],
                #             children=[
                #                 dash_vtk.PointData(
                #                     children=[
                #                         dash_vtk.DataArray(
                #                             name="Temperature", values=[0, 3, 2, 1]
                #                         )
                #                     ]
                #                 )
                #             ],
                #         ),
                #     ],
                #     picks=[
                #         dash_vtk.PickGroup(
                #             id="picks",
                #             axisIdList=[[0, 1, 3] for i in range(100)],
                #             offsetList=[[0, 0+i/100, 0] for i in range(100)],
                #         )
                #     ]
                # ),
                html.Div(
                    id="picks",
                    children=[
                        dash_vtk.GeometryRepresentation(
                            id=f"Pick1",
                            property={
                                "color": [1, 0, 0],
                                "opacity": 0.5,
                            },
                            actor={
                                "visibility": True,
                            },
                            children=[
                                dash_vtk.Algorithm(
                                    id="Pick1Algorithm",
                                    vtkClass="vtkSphereSource",
                                    state={"center": [1, 0, 0], "radius": 0.1},
                                )
                            ]
                        ),
                        dash_vtk.GeometryRepresentation(
                            id=f"Pick2",
                            children=[
                                dash_vtk.Algorithm(
                                    vtkClass="vtkSphereSource",
                                    state={"center": [0, 0, 0], "radius": 0.1},
                                )
                            ]
                        ),
                        dash_vtk.GeometryRepresentation(
                            id=f"Pick3",
                            children=[
                                dash_vtk.Algorithm(
                                    vtkClass="vtkSphereSource",
                                    state={"center": [0, 1, 0], "radius": 0.1},
                                )
                            ]
                        ),
                        dash_vtk.GeometryRepresentation(
                            id=f"Pick4",
                            children=[
                                dash_vtk.Algorithm(
                                    vtkClass="vtkSphereSource",
                                    state={"center": [0, 0, 1], "radius": 0.1},
                                )
                            ]
                        ),
                    ]
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
                            points=[0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
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
                        dash_vtk.PickGroup(
                            id="picks",
                            axisIdList=[[0, 1, 3] for i in range(100)],
                            offsetList=[[0, 0+i/100, 0] for i in range(100)],
                        )
                    ]
                ),
                
            ],
        ),
        html.Div(id="output"),
    ],
)

@callback(
    #Output("square", "points"),
    Output("Pick1", "property"),
    Input("view", "clickInfo"),
)
def move_square(click_info):
    if click_info is None:
        return no_update

    # Extract the click position
    x, y, z = click_info.get("worldPosition", [0, 0, 0])

    # Update the square's points based on the click position
    new_points = [
        x, y, z,
        x + 1, y, z,
        x + 1, y + 1, z,
        x, y + 1, z,
    ]
    patch = Patch()
    patch["color"] = [0, 0, 1]

    return {"color": [0, 0, 1], "opacity": 0.6}

if __name__ == "__main__":
    app.run(debug=True)
