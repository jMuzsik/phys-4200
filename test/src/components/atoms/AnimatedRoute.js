import { useLocation } from "react-router-dom";
import { CSSTransition } from "react-transition-group";

const duration = 300;

export default ({ match, children }) => {
  console.log(match)
  console.log(children)
  return (
    <CSSTransition
      in={match !== null}
      timeout={duration}
      classNames="page"
      unmountOnExit
    >
      {children}
    </CSSTransition>
  );
};
