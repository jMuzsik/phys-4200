import { H1 } from "@blueprintjs/core";

export default function Content({ children, title }) {
  return (
    <article className="content">
      <H1>{title}</H1>
      {children}
    </article>
  );
}
