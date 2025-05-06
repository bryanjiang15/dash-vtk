import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { useModelPoints } from '../contexts/ModelPointsContext';

import { GeometryRepresentation as VtkItem, Algorithm} from '../AsyncReactVTK';

/**
 * GeometryRepresentation is responsible to convert a vtkPolyData into rendering
 * It takes the following set of properties:
 *   - actor: Properties to assign to the vtkActor
 *   - mapper: Properties to assign to the vtkMapper
 *   - property: Properties to assign to the vtkProperty (actor.getProperty())
 *   - colorMapPreset: Name of the preset to use for controlling the color mapping
 *   - colorDataRange: Range to use for the color scale
 */
export default function Pick(props) {
  const modelPoints = useModelPoints();
  const { axisIds, offsets } = props;
  const [pickPosition, setPickPosition] = useState(null);
  const [vtkClassState, setVtkClassState] = useState(props.vtkClassState);

  useEffect(() => {
    function calculatePickPosition() {
      const origin = modelPoints[axisIds[0]];
      const xAxis = modelPoints[axisIds[1]].map((val, idx) => val - origin[idx]);
      const yAxis = modelPoints[axisIds[2]].map((val, idx) => val - origin[idx]);
      const zAxis = origin.map((val, idx) => val + (xAxis[1] * yAxis[2] - xAxis[2] * yAxis[1]));

      let position = [...origin];
      position = position.map((val, idx) => val + offsets[0] * xAxis[idx] + offsets[1] * yAxis[idx] + offsets[2] * (zAxis[idx] - origin[idx]));
      return position;
    }
    
    const newPickPosition = calculatePickPosition();
    setPickPosition(newPickPosition);
    setVtkClassState((prevState) => ({
      ...prevState,
      center: newPickPosition,
    }));
  }, [modelPoints, axisIds, offsets]); // Recalculate when dependencies change

  return (
    <React.Suspense fallback={null}>
      <VtkItem 
        id={props.id}
        property={props.property}
        actor={props.actor}
        mapper={props.mapper}
      >
        <Algorithm
          vtkClass={props.vtkClass}
          state={vtkClassState}
        />
      </VtkItem>
    </React.Suspense>
  );
};

Pick.defaultProps = {
  colorMapPreset: 'erdc_rainbow_bright',
  colorDataRange: [0, 1],
  showCubeAxes: false,
  showScalarBar: false,
  scalarBarTitle: '',
  vtkClass: 'vtkSphereSource',
  vtkClassState: {
    radius: 0.05,
    center: [0, 0, 0],
  },
};

Pick.propTypes = {
  /**
   * The ID used to identify this component.
   */
  id: PropTypes.string,

  /**
   * Properties to set to the actor
   */
  actor: PropTypes.object,

  /**
   * Properties to set to the actor
   */
  mapper: PropTypes.object,

  /**
   * Properties to set to the actor.property
   */
  property: PropTypes.object,

  /**
   * Preset name for the lookup table color map
   */
  colorMapPreset: PropTypes.string,

  /**
   * Data range use for the colorMap
   */
  colorDataRange: PropTypes.arrayOf(PropTypes.number),

  /**
   * Show/Hide Cube Axes for the given representation
   */
  showCubeAxes: PropTypes.bool,

  /**
   * Configure cube Axes style by overriding the set of properties defined
   * https://github.com/Kitware/vtk-js/blob/HEAD/Sources/Rendering/Core/CubeAxesActor/index.js#L703-L719
   */
  cubeAxesStyle: PropTypes.object,

  /**
   * Show hide scalar bar for that representation
   */
  showScalarBar: PropTypes.bool,

  /**
   * Use given string as title for scalar bar. By default it is empty (no title).
   */
  scalarBarTitle: PropTypes.string,

  /**
   * Configure scalar bar style by overriding the set of properties defined
   * https://github.com/Kitware/vtk-js/blob/master/Sources/Rendering/Core/ScalarBarActor/index.js#L776-L796
   */
  scalarBarStyle: PropTypes.object,

  children: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.node),
    PropTypes.node,
  ]),

  vtkClass: PropTypes.string,
  vtkClassState: PropTypes.object,
  axisIds: PropTypes.arrayOf(PropTypes.number),
  offsets: PropTypes.arrayOf(PropTypes.number),
};