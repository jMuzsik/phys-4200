import { H1 } from "@blueprintjs/core";

export default function Content({ children }) {
  return (
    <article className="content">
      <H1>Main Area</H1>
      {children}
    </article>
  );
}
