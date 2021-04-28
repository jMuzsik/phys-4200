import { useState } from "react";
import {
  Card,
  FormGroup,
  NumericInput,
  Button,
  Intent,
  H2,
} from "@blueprintjs/core";

function handleSubmit(ev, data, hooks, pointCharges) {
  ev.preventDefault();
  hooks.setPointCharge(pointCharges.concat(data));
  hooks.formFields.forEach((hook) => hook(undefined));
  document.querySelectorAll('.bp3-input').forEach(input => input.value = 0)
}

const valid = (d, low, high) => d >= low && d <= high && typeof d === "number";

function checkIfValid(charge, x, y) {
  const chargeValid = valid(charge, -5, 5);
  const xValid = valid(x, 0, 100);
  const yValid = valid(y, 0, 100);
  return chargeValid && xValid && yValid;
}

export default function ChargeForm({ setPointCharge, pointCharges }) {
  const [charge, setCharge] = useState(undefined);
  const [x, setX] = useState(undefined);
  const [y, setY] = useState(undefined);

  const validSubmission = checkIfValid(charge, x, y);

  return (
    <Card className="charge-form" title="Add a Charge Form">
      <H2>Add a Charge Form</H2>
      <form
        onSubmit={(ev) =>
          handleSubmit(
            ev,
            { charge, x, y },
            { setPointCharge, formFields: [setCharge, setX, setY] },
            pointCharges
          )
        }
      >
        <div className="input-fields">
          <FormGroup
            helperText="Input a number between -5 and 5."
            label="Charge"
            labelFor="charge-input"
          >
            <NumericInput
              id="charge-input"
              defaultValue={0}
              required
              max="5"
              min="-5"
              value={charge}
              onValueChange={(num) => setCharge(num)}
            />
          </FormGroup>
          <FormGroup
            helperText="x value on grid (0 to 100)"
            label="X"
            labelFor="x-input"
          >
            <NumericInput
              id="x-input"
              defaultValue={0}
              required
              max="100"
              min="0"
              value={x}
              onValueChange={(num) => setX(num)}
            />
          </FormGroup>
          <FormGroup
            helperText="y value on grid (0 to 100)"
            label="Y"
            labelFor="y-input"
          >
            <NumericInput
              id="y-input"
              defaultValue={0}
              required
              max="100"
              min="0"
              value={y}
              onValueChange={(num) => setY(num)}
            />
          </FormGroup>
        </div>
        <Button
          type="submit"
          text="Submit"
          intent={Intent.PRIMARY}
          disabled={!validSubmission}
        />
      </form>
    </Card>
  );
}
