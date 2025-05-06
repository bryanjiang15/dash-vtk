import React, { createContext, useContext } from 'react';

// Create a context for modelPoints
export const ModelPointsContext = createContext(null);

export function useModelPoints() {
  return useContext(ModelPointsContext);
}