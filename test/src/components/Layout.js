import Wrapper from "./atoms/Wrapper";
import Header from "./atoms/Header";
import Nav from "./molecules/Nav";
import Ad from "./atoms/Ad";
import Sidebar from "./atoms/Sidebar";
import Footer from "./atoms/Footer";

export default function Layout({ children }) {
  return (
    <Wrapper>
      <Header />
      <Nav />
      <Sidebar />
      {children}
      <Ad>Advertising</Ad>
      <Footer />
    </Wrapper>
  );
}
