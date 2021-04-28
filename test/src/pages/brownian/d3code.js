import * as d3 from "d3";

export default (svg, data, dots) => {
  var width = 960;
  var height = 500;

  var gasMoleculeCount = 3000;
  var dustCount = 10;

  var realtimeContext = document
    .querySelector("#realtime")
    .getContext("2d", { alpha: true });

  var historicalContext = document
    .querySelector("#historical")
    .getContext("2d", { alpha: true });

  realtimeContext.transform(1, 0, 0, 1, width / 2, height / 2);
  historicalContext.transform(1, 0, 0, 1, width / 2, height / 2);

  var radius = function (node) {
    return node.radius;
  };

  var gasMolecules = d3.range(gasMoleculeCount).map(function (d) {
    var randomAngle = Math.random() * 2 * Math.PI;
    return {
      radius: 0.5,
      x: Math.random() * width - width / 2,
      y: Math.random() * height - height / 2,
      vx: 5 * Math.cos(randomAngle),
      vy: 5 * Math.sin(randomAngle),
    };
  });

  var dustParticles = d3.range(dustCount).map(function (d) {
    return {
      radius: 3,
      x: (Math.random() * width - width / 2) / 2,
      y: (Math.random() * height - height / 2) / 2,
      vx: 0,
      vy: 0,
    };
  });

  var nodes = dustParticles.concat(gasMolecules);

  var recycle = function (alpha) {
    var node;
    var i;
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

  d3.forceSimulation(nodes)
    .alphaDecay(0)
    .velocityDecay(5e-4)
    .force(
      "collide",
      d3.forceCollide().radius(radius).strength(1).iterations(1)
    )
    .force("recycle", recycle)
    .on("tick", render);

  realtimeContext.lineWidth = 1;
  realtimeContext.fillStyle = "red";

  historicalContext.lineWidth = 5;
  historicalContext.strokeStyle = "rgba(128, 0, 255, 0.02)";

  function render() {
    var i;
    var particle;

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
      var r = particle.radius;
      realtimeContext.moveTo(particle.x + r, particle.y);
      realtimeContext.arc(particle.x, particle.y, r, 0, 2 * Math.PI);
    }
    realtimeContext.fill();
  }
};
