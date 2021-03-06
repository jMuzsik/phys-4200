import { useRef, useEffect } from "react";
import * as d3 from "d3";

export default function useD3(renderChartFn, dependencies) {
  const ref = useRef();

  useEffect(() => {
    ref.current.innerHTML = "";
    renderChartFn(d3.select(ref.current));
    return () => {};
  }, dependencies);

  return ref;
}
