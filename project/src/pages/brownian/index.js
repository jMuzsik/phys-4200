import { useRef, useEffect, useState } from "react";

import ParticleForm from "./ParticleForm";
import d3Code from "./d3Code";

export default function BrownianWrapper() {
  const [options, setOptions] = useState({
    gasMoleculeCount: localStorage.getItem("gasMoleculeCount"),
    dustCount: localStorage.getItem("dustCount"),
  });

  return (
    <div className="graph-wrapper">
      <Brownian options={options} />
      <ParticleForm setOptions={setOptions} />
    </div>
  );
}

function Brownian({ options }) {
  const realtimeCanvas = useRef();
  const historicalCanvas = useRef();

  useEffect(() => {
    d3Code(realtimeCanvas.current, historicalCanvas.current, options);
  }, [options.gasMoleculeCount, options.dustCount]);

  return (
    <div className="brownian-motion-container">
      <div className="brownian-motion">
        <canvas
          id="realtime"
          ref={realtimeCanvas}
          width={650}
          height={500}
          style={{ zIndex: 2 }}
        />
        <canvas
          id="historical"
          ref={historicalCanvas}
          width={650}
          height={500}
          style={{ zIndex: 1 }}
        />
      </div>
    </div>
  );
}
