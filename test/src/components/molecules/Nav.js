import {
  Alignment,
  Navbar,
  NavbarDivider,
  NavbarGroup,
  NavbarHeading,
} from "@blueprintjs/core";

import { useLocation } from "wouter";

import LinkButton from "../atoms/LinkButton";

export default function Nav() {
  const setLocation = useLocation()[1];
  return (
    <Navbar>
      <NavbarGroup align={Alignment.RIGHT}>
        <NavbarHeading>Physics</NavbarHeading>
        <NavbarDivider />
        <LinkButton
          href="/"
          onClick={() => setLocation("/")}
          text="Home"
          className="minimal"
        />
        <LinkButton
          href="/about"
          onClick={() => setLocation("/about")}
          text="About"
          className="minimal"
        />
      </NavbarGroup>
    </Navbar>
  );
}
