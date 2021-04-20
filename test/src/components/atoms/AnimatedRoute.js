import { useRoute } from "wouter";
import { CSSTransition } from "react-transition-group";

const duration = 300;

export default ({ location }) => {
  const [match] = useRoute(location);

  return (
    <div className="transition-container">
      <CSSTransition
        in={match != null}
        timeout={duration}
        classNames="page"
        unmountOnExit
      >
        <div className="page">
          <h1>I'm a fade Transition!</h1>
        </div>
      </CSSTransition>
    </div>
  );
};
