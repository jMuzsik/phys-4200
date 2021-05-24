import * as d3 from "d3";

export default (
  realtimeCanvas,
  historicalCanvas,
  { gasMoleculeCount, dustCount }
) => {
  let width = 650;
  let height = 500;

  const realtimeContext = realtimeCanvas.getContext("2d");
  const historicalContext = historicalCanvas.getContext("2d");
  // reset the canvas's
  realtimeContext.clearRect(0, 0, 500, 650);
  historicalContext.clearRect(0, 0, 500, 650);

  realtimeContext.transform(1, 0, 0, 1, width / 2, height / 2);
  historicalContext.transform(1, 0, 0, 1, width / 2, height / 2);

  let radius = function (node) {
    return node.radius;
  };

  let gasMolecules = d3.range(gasMoleculeCount).map(function (d) {
    let randomAngle = Math.random() * 2 * Math.PI;
    return {
      radius: 0.5,
      x: Math.random() * width - width / 2,
      y: Math.random() * height - height / 2,
      // initial trajectory of the gas molecules
      vx: 5 * Math.cos(randomAngle),
      vy: 5 * Math.sin(randomAngle),
    };
  });

  let dustParticles = d3.range(dustCount).map(function (d) {
    return {
      radius: 3,
      x: (Math.random() * width - width / 2) / 2,
      y: (Math.random() * height - height / 2) / 2,
      // no trajectory for the dust particles to start
      vx: 0,
      vy: 0,
    };
  });

  // each element is a node in the canvas
  let nodes = dustParticles.concat(gasMolecules);

  let recycle = function () {
    let node;
    let i;
    for (i = 0; i < nodes.length; i++) {
      node = nodes[i];
      if (Math.abs(node.x) > width / 2 - node.radius) {
        node.vx *= -1;
      }
      if (Math.abs(node.y) > height / 2 - node.radius) {
        node.vy *= -1;
      }
    }
  };

  // force simulation utilises verlet integration, through the forceSimulation API
  // https://en.wikipedia.org/wiki/Verlet_integration

  d3.forceSimulation(nodes)
    .alphaDecay(0)
    .velocityDecay(5e-4)
    .force(
      "collide",
      // calls the radius function which simply tells you the size of the
      // colliding gas molecule - altering the trajectory of the dust particle accordingly
      d3.forceCollide().radius(radius).strength(1).iterations(1)
    )
    // necessary to assure a constant stream of gas molecules
    .force("recycle", recycle)
    // repeat over and over and over
    // render basically controls the movement of the particles during each tick
    .on("tick", render);

  realtimeContext.lineWidth = 1;
  realtimeContext.fillStyle = "red";

  historicalContext.lineWidth = 5;
  historicalContext.strokeStyle = "rgba(128, 0, 255, 0.02)";

  function render() {
    let i;
    let particle;

    realtimeContext.clearRect(-width / 2, -height / 2, width, height);

    historicalContext.beginPath();
    for (i = 0; i < dustCount; i++) {
      particle = dustParticles[i];
      historicalContext.moveTo(particle.x, particle.y);
      historicalContext.lineTo(particle.x + 1, particle.y + 1);
    }
    historicalContext.stroke();

    realtimeContext.beginPath();
    for (i = 0; i < gasMoleculeCount; i++) {
      particle = gasMolecules[i];
      realtimeContext.moveTo(particle.x, particle.y);
      realtimeContext.lineTo(particle.x + 1, particle.y);
    }
    realtimeContext.stroke();

    realtimeContext.beginPath();
    for (i = 0; i < dustCount; i++) {
      particle = dustParticles[i];
      let r = particle.radius;
      realtimeContext.moveTo(particle.x + r, particle.y);
      realtimeContext.arc(particle.x, particle.y, r, 0, 2 * Math.PI);
    }
    realtimeContext.fill();
  }
};
