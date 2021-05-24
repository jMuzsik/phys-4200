import {
  Alignment,
  Navbar,
  NavbarDivider,
  NavbarGroup,
} from "@blueprintjs/core";

import LinkButton from "../atoms/LinkButton";

export default function Nav() {
  return (
    <Navbar className="nav">
      <NavbarGroup align={Alignment.RIGHT}>
        <LinkButton href="/" text="Potential" className="minimal" />
        <NavbarDivider />
        <LinkButton href="/brownian" text="Brownian" className="minimal" />
        <NavbarDivider />
        <LinkButton href="/about" text="About" className="minimal" />
      </NavbarGroup>
    </Navbar>
  );
}
