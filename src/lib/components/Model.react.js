import React, { use, useEffect, useState } from 'react';
import { createContext, useContext, useRef } from 'react';
import PropTypes from 'prop-types';

import { GeometryRepresentation as VtkItem, Algorithm, View } from '../AsyncReactVTK.js';
import Pick from './Pick.react.js';
import { ModelPointsContext } from '../contexts/ModelPointsContext.js';
import PickGroup from './PickGroup.react.js';
/**
 * GeometryRepresentation is responsible to convert a vtkPolyData into rendering
 * It takes the following set of properties:
 *   - actor: Properties to assign to the vtkActor
 *   - mapper: Properties to assign to the vtkMapper
 *   - property: Properties to assign to the vtkProperty (actor.getProperty())
 *   - colorMapPreset: Name of the preset to use for controlling the color mapping
 *   - colorDataRange: Range to use for the color scale
 */


export default function Model(props) {
  const [modelPoints, setModelPoints] = useState(ReshapeModelPoints(props.children.props._dashprivate_layout.props.points));

  useEffect(() => {  
    setModelPoints(ReshapeModelPoints(props.children.props._dashprivate_layout.props.points));
  }, [props.children.props]);

  function renderPicks() {
    return props.picks.map((pick) => {
      
      const pickProps = pick.props._dashprivate_layout.props;
      
      return <PickGroup {...pickProps} key={pickProps.id} />;
    });
  }

  return (
    <React.Suspense fallback={null}>
      <ModelPointsContext.Provider value={modelPoints}>
        <div>
          <VtkItem {...props} />
          {renderPicks()}
        </div>
      </ModelPointsContext.Provider>
    </React.Suspense>
  );
};

Model.defaultProps = {
  colorMapPreset: 'erdc_rainbow_bright',
  colorDataRange: [0, 1],
  showCubeAxes: false,
  showScalarBar: false,
  scalarBarTitle: '',
};

// Model.dashChildrenUpdate = true;

Model.propTypes = {
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

  picks: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.node),
    PropTypes.node,
  ]),
};

function ReshapeModelPoints(points) {
  // Reshape the points to be a list of tuples
  if (points.length % 3 !== 0) {
    throw new Error('Points array length must be a multiple of 3');
  }

  const reshapedPoints = [];
  for (let i = 0; i < points.length; i += 3) {
    reshapedPoints.push([points[i], points[i + 1], points[i + 2]]);
  }
  return reshapedPoints;
}