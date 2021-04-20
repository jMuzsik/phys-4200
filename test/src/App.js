import {
  Route,
  BrowserRouter as Router,
  Switch,
  useLocation,
} from "react-router-dom";
import { H1, H3 } from "@blueprintjs/core";
import { SwitchTransition, CSSTransition } from "react-transition-group";

import Layout from "components/Layout";
import Main from "components/molecules/Main";

import "styles/Layout.css";
import "styles/transitions.css";

function Inner() {
  const location = useLocation();
  console.log(location.pathname);
  console.log(location.state.from);
  return (
    <SwitchTransition>
      <CSSTransition timeout={300} classNames="fade" key={location.key}>
        <Switch location={location}>
          <Route exact path="/">
            <Main />
          </Route>
          <Route exact path="/about">
            <H1>this is the about page</H1>
          </Route>
          <Route path="*">
            <H1>404</H1>
          </Route>
        </Switch>
      </CSSTransition>
    </SwitchTransition>
  );
}

function App() {
  console.log("what");
  return (
    <Router>
      <Layout>
        <Inner />
      </Layout>
    </Router>
  );
}

export default App;