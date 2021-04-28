import { zeros } from "./utils";

const EPSILON_0 = 8.854187817e-12;

function calcRadius(x1, y1, x2, y2) {
  return Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
}

function calcPotential(q, r) {
  const bottom = 4 * Math.PI * EPSILON_0 * r;
  if (bottom !== 0) {
    return q / bottom;
  }
  return 0;
}

// Input values into array
function inputValuesIntoArray(arr, coords, amount, sign) {
  for (let i = 0; i < amount; i++) {
    arr.push({ x: coords[0], y: coords[1], sign });
  }
}

export default function createGridData(pointCharges) {
  const gridSize = 100;
  const weightFactor = 0.7e8;

  // Array of values to be returned
  const returnArr = [];

  // Go through entire grid, calculating the electric potential at each point
  // Points t have a higher than normal potential are to be returned with a
  // corresponding weight (more values to be added to finalArr)
  // ie. If the potential is very strong at a point, then add a corresponding
  //     amount of points
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      const p = pointCharges.reduce(
        (totalPotential, { x, y, charge }) =>
          (totalPotential += calcPotential(charge, calcRadius(i, j, x, y))),
        0
      );
      if (p > 0.7e8) {
        const weightSizePos = Math.ceil(p / weightFactor);
        inputValuesIntoArray(returnArr, [i, j], weightSizePos, "pos");
      } else if (p < -0.7e8) {
        const weightSizeNeg = Math.abs(Math.ceil(p / weightFactor));
        inputValuesIntoArray(returnArr, [i, j], weightSizeNeg, "neg");
      }
    }
  }
  return returnArr;
}
