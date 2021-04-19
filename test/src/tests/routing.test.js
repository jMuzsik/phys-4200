// app.test.js
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Switch } from "wouter";

import "@testing-library/jest-dom/extend-expect";

import { App } from "../App";

test("full app rendering/navigating", () => {
  render(<App />);
  // verify page content for expected route
  // often you'd use a data-testid or role query, but this is also possible
  expect(screen.getByText(/Welcome to the site/i)).toBeInTheDocument();

  const leftClick = { button: 0 };
  userEvent.click(screen.getByText(/About/i), leftClick);

  // check that the content changed to the new page
  expect(screen.getByText(/you are on the about page/i)).toBeInTheDocument();
});

test("landing on a bad page", () => {
  history.push("/some/bad/route");
  render(<App />);

  expect(screen.getByText(/"404"/i)).toBeInTheDocument();
});

test("rendering a component that uses useLocation", () => {
  const route = "/some-route";
  history.push(route);
  render(<LocationDisplay />);

  expect(screen.getByTestId("location-display")).toHaveTextContent(route);
});
