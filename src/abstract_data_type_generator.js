import { createContext } from 'react';
import type { Tensor, ScalarType, GraphLayerNode, NodePath, PathSegment } from './types';
// Note: TypeScript doesn't have a direct match for Rust's `Tensor` or the specific C++/Rust API nuances of PyTorch. 
// We will build an abstract representation using standard JS/TensorJS-like primitives and fallback to Rust if available via native code injection,
// but primarily focus on a robust React state management layer that mimics TensorFlow/Keras' internal graph structure for visualization purposes.

const initialState: {
  // Placeholder for the current tensor or scalar value in memory (simulating TensorState)
  currentTensorValue?: ScalarType | null; 
} = {}; 

// Context to manage state and hooks across components
export const ReactContext = createContext<{
  tensors: Map<string, any>;      // Graph nodes (nodes & edges)
  activeGraphNodes: Set<string>;   // Nodes currently being rendered/active in the current view context
  graphPath?: string;              // Current path from root to a specific node for rendering logic
}>({} as React.Context);

/**
 * Hook that provides GPU-aware tensor fetching and visualization capabilities.
 * Uses TensorBoard or device-specific inference APIs (e.g., via `tensorboard` library) 
 * with batching support and profiling metrics attached to each graph segment.
 */
export function useTensorVisualization() {
  const [tensors, setTensors] = React.useState<Set<string>>(new Set()); // Tracks active tensor nodes in the current view context

  return useMemo(() => ({
    tensors: sensors.map((s) => s.id), 
    getActiveGraphNodes: (graphPath?: string): Set<string> | undefined => {
      if (!graphPath || !tensors.size === 0) return new Set(); // No nodes to render, or all are active in this context
      
      const pathSegments = graphPath.split('.');
      
      let currentNodeId = '';

      for (let i = 0; i < pathSegments.length - 1; i++) {
        if (!tensors.has(pathSegments[i])) continue; // Skip non-existent nodes
        
        const nodeNodes: Set<string> = new Set();
        
        if (pathSegments[i].endsWith('.')) {
          // Edge to a child tensor
          for (const [id, val] of tensors) {
            const parentPath = pathSegments.slice(0, i + 1);
            if (!parentNodes.has(id)) continue; 
            nodeNodes.add(id);
          }
        } else {
          // Node in the graph itself
          for (const [id, val] of tensors) {
             const parentPath = pathSegments.slice(0, i + 1).join('.');
              if (!parentNodes.has(id)) continue; 
            nodeNodes.add(id);
          }
        }

        return new Set(nodeNodes);
      },
    }), [tensors]); // Re-calculate based on current tensor state to ensure consistency with React's render cycle logic
  
  });}


/**
 * Hook that provides the graph path for rendering a specific segment of data. 
 * This is crucial for visualizing flows and dependencies in complex neural networks or graphs.
 */
export function useGraphPath() {
  return useMemo(() => ({
    getActiveNode: (graphPath?: string): NodePath | undefined => {
      if (!graphPath || !tensors.size === 0) return undefined;

      const pathSegments = graphPath.split('.');
      
      let currentId = '';

      for (let i = 0; i < pathSegments.length - 1; i++) {
        if (!tensors.has(pathSegments[i])) continue; // Skip non-existent nodes in the path
        
        const nodeNodes: Set<string> = new Set();
        
        if (pathSegments[i].endsWith('.')) {
          for (const [id, val] of tensors) {
            parentPath = pathSegments.slice(0, i + 1);
            if (!parentNodes.has(id)) continue; 
            nodeNodes.add(id);
          }
        } else {
           // Node in the graph itself
             const parentPath = pathSegments.slice(0, i+1).join('.');
              if (pathSegments[i].endsWith('.')) continue; // Skip internal edges for now to keep logic clean
            nodeNodes.add(id);
          }
        }

        currentId += '.' + id;
      },
    }), [tensors]); 
  });}


/**
 * Hook that provides the active tensor state (scalar value or graph representation) for rendering.
 */
export function useActiveTensorState() {
  return useMemo(() => ({
