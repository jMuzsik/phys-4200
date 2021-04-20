import { Route, Router, Switch } from "wouter";
import { H1, H3 } from "@blueprintjs/core";

import Layout from "./components/Layout";
import Main from "./components/molecules/Main";
import AnimatedRoute from "./components/atoms/AnimatedRoute";

import "./App.css";
import "./styles/Layout.css";
import "./styles/transitions.css";

function App() {
  return (
    <Layout>
      <Router>
        <Route path="/">
          <Main />
        </Route>
        <Route path="/about">
          <Main>
            <AnimatedRoute location="/about">
              <div>
                <H3>you are on the about page</H3>
                <H3>you are on the about page</H3>
                <H3>you are on the about page</H3>
                <H3>you are on the about page</H3>
              </div>
            </AnimatedRoute>
          </Main>
        </Route>
        <Route>
          <H1>404</H1>
        </Route>
      </Router>
    </Layout>
  );
}

export default App;
