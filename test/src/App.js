import { Route, Switch } from "wouter";
import { H1, H3 } from "@blueprintjs/core";

import Layout from "./components/Layout";
import Main from "./components/molecules/Main";
import AnimatedRoute from "./components/atoms/AnimatedRoute";

import "./App.css";

function App() {
  return (
    <Layout>
      <Switch>
        <Route path="/">
          <Main />
        </Route>
        <Route path="/about">
          <Main>
            <AnimatedRoute location="/about">
              <H3>you are on the about page</H3>
            </AnimatedRoute>
          </Main>
        </Route>
        <Route>
          <H1>404</H1>
        </Route>
      </Switch>
    </Layout>
  );
}

export default App;
