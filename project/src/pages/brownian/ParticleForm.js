import { useState } from "react";
import {
  Card,
  FormGroup,
  NumericInput,
  Button,
  Intent,
  H2,
} from "@blueprintjs/core";

function refreshPage() {
  window.location.reload(false);
}

function handleSubmit(ev, data, hooks) {
  ev.preventDefault();
  localStorage.setItem('gasMoleculeCount', data.gasMoleculeCount);
  localStorage.setItem('dustCount', data.dustCount);
  refreshPage();
}

const valid = (d, low, high) => d >= low && d <= high && typeof d === "number";

function checkIfValid(dust, gas) {
  const dustValid = valid(dust, 1, 100);
  const gasValid = valid(gas, 1, 50000);
  return dustValid && gasValid;
}

export default function PotentialForm({ setOptions }) {
  const [dustCount, setDust] = useState(1);
  const [gasMoleculeCount, setGas] = useState(1);

  const validSubmission = checkIfValid(dustCount, gasMoleculeCount);

  return (
    <Card className="charge-form" title="Set Options Form">
      <H2>Set Options Form</H2>
      <form
        onSubmit={(ev) =>
          handleSubmit(
            ev,
            { gasMoleculeCount, dustCount },
            { setOptions, formFields: [setDust, setGas] }
          )
        }
      >
        <div className="input-fields">
          <FormGroup
            helperText="Input a number between 1 and 100."
            label="Dust Amount"
            labelFor="dust-input"
          >
            <NumericInput
              id="dust-input"
              defaultValue={0}
              required
              max="100"
              min="1"
              value={dustCount}
              onValueChange={(num) => setDust(num)}
            />
          </FormGroup>
          <FormGroup
            helperText="Gas Molecule Amount"
            label="Gas Molecules"
            labelFor="gas-input"
          >
            <NumericInput
              id="gas-input"
              defaultValue={0}
              required
              max="50000"
              min="1"
              value={gasMoleculeCount}
              onValueChange={(num) => setGas(num)}
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
