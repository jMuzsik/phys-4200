import { Button, Classes } from "@blueprintjs/core";
import { Link } from "wouter";

export default ({ href, className, onClick, text, icon }) => {
  return (
    <Link href={href}>
      <div title={href}>
        <Button className={Classes[className]} onClick={onClick} icon={icon}>
          {text}
        </Button>
      </div>
    </Link>
  );
};
