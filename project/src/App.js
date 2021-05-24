import {
  Route,
  BrowserRouter as Router,
  Switch,
  useLocation,
} from "react-router-dom";
import { SwitchTransition, CSSTransition } from "react-transition-group";

import Layout from "components/Layout";
import Main from "components/molecules/Main";

import Potential from "pages/potential";
import Brownian from "pages/brownian";

import "./index.css";
import "styles/Layout.css";
import "styles/transitions.css";
import "styles/forms.css";

function Inner() {
  const location = useLocation();
  return (
    <SwitchTransition>
      <CSSTransition timeout={300} classNames="fade" key={location.key}>
        <Switch location={location}>
          <Route exact path="/">
            <Main title="Potential">
              <Potential />
            </Main>
          </Route>
          <Route exact path="/about">
            <Main title="About">
              <h3>Not much to see here</h3>
            </Main>
          </Route>
          <Route exact path="/brownian">
            <Main title="Brownian">
              <Brownian />
            </Main>
          </Route>
          <Route path="*">
            <Main title="About">
              <h3>404</h3>
            </Main>
          </Route>
        </Switch>
      </CSSTransition>
    </SwitchTransition>
  );
}

function App() {
  return (
    <Router>
      <Layout>
        <Inner />
      </Layout>
    </Router>
  );
}

export default App;
