import { useRoute } from "wouter";
import { Transition } from "react-transition-group";

export default AnimatedRoute = ({ children, location }) => {
  const correctLocation = useRoute(location)[0];

  return <Transition in={correctLocation}>{children}</Transition>;
};
