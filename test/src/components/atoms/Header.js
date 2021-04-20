import { H1 } from "@blueprintjs/core";
import { useLocation } from "react-router-dom";

export default function Header({ children }) {
  const location = useLocation()[0];

  return (
    <header className="header">
      <H1>Welcome to the site</H1>
      <div data-testid="location-display">{location}</div>
    </header>
  );
}
