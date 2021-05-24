import Wrapper from "./atoms/Wrapper";
import Header from "./atoms/Header";
import Nav from "./molecules/Nav";
import Footer from "./atoms/Footer";

export default function Layout({ children }) {
  return (
    <Wrapper>
      <Header />
      <Nav />
      {children}
      <Footer />
    </Wrapper>
  );
}
