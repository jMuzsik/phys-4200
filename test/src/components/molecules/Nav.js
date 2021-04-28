import {
  Alignment,
  Navbar,
  NavbarDivider,
  NavbarGroup,
  NavbarHeading,
} from "@blueprintjs/core";


import LinkButton from "../atoms/LinkButton";

export default function Nav() {
  return (
    <Navbar className="nav">
      <NavbarGroup align={Alignment.RIGHT}>
        <NavbarHeading>Physics</NavbarHeading>
        <NavbarDivider />
        <LinkButton href="/" text="Home" className="minimal" />
        <LinkButton href="/about" text="About" className="minimal" />
      </NavbarGroup>
    </Navbar>
  );
}
