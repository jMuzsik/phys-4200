import { useEffect, useState } from "react";

import useD3 from "lib/hooks/useD3";
import createGridData from "lib/math/diff";
import d3Code from "./d3Code";

import ParticleForm from "./ParticleForm";

export default function HistogramWrapper() {
  const [data, setData] = useState([]);
  const [pointCharges, setPointCharge] = useState([]);

  useEffect(() => {
    setData(createGridData(pointCharges));
    return () => {
      setData([]);
    };
  }, [pointCharges.length]);

  return (
    <div className="graph-wrapper">
      <Histogram data={data} pointCharges={pointCharges} />
      <ParticleForm setPointCharge={setPointCharge} pointCharges={pointCharges} />
    </div>
  );
}

function Histogram({ data, pointCharges }) {
  const ref = useD3(
    (svg) => {
      d3Code(svg, data, pointCharges);
    },
    [data.length]
  );

  return (
    <svg
      id="my_dataviz"
      ref={ref}
      style={{
        padding: 25,
        margin: 25,
        width: 400,
        height: 400,
      }}
    ></svg>
  );
}
