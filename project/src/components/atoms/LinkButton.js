import { Button, Classes } from "@blueprintjs/core";
import { Link } from "react-router-dom";

function LinkButton({ href, className, text, icon }) {
  return (
    <Link
      to={(location) => ({
        ...location,
        pathname: href,
        state: { from: location.pathname },
      })}
    >
      <div title={href}>
        <Button className={Classes[className]} icon={icon}>
          {text}
        </Button>
      </div>
    </Link>
  );
}

export default LinkButton;
