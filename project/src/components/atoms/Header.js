import { useLocation } from "react-router-dom";

const images = [
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102332564/Portrait-of-Sir-Isaac-New-001.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=884bd2da5b38f39e83359aee9211899a",
    "Newton",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102338410/Niels-Bohr-002.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=917c09ac325c4fe61b585d5d166d3cd2",
    "Neils Bohr",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102341447/Galileo-Galilei-1564-1642-003.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=7b19151d3018de0be1f0cfc0c0794380",
    "Galileo",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102344333/Albert-Einstein-004.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=339113851b95c2e81eaf68c8f5ce71b7",
    "Einstein",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102346975/Portrait-of-James-Clerk-M-005.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=530832c57a2fadd442062ae6fc7b488c",
    "Maxwell",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102351856/Michael-Faraday-006.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=1b8ef626f99e01d8c471a3f5dd9d6762",
    "Faraday",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102354328/Marie-Curie-In-Laboratory-007.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=8bdf6e9d233b666e69473f8ddd94bc76",
    "Curie",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102358488/Richard-Feynman-with-Ring-008.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=e529f7796b865124b0b79784f4c92d35",
    "Feynman",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102360057/Ernest-Rutherford-009.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=6753bb4f39231f405aab1c93ec21cab2",
    "Rutherford",
  ],
  [
    "https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/5/9/1368102363130/Paul-Dirac-010.jpg?width=1010&quality=45&auto=format&fit=max&dpr=2&s=06c33289f920ed5b47eb999944d7dc8b",
    "Dirac",
  ],
];
function Img({ src, alt }) {
  return <img src={src} alt={alt} />;
}
export default function Header() {
  const location = useLocation()[0];

  return (
    <header className="header">
      <div className="images">
        {images.map(([src, alt], i) => (
          <Img src={src} alt={alt} key={i} />
        ))}
      </div>
      <div data-testid="location-display">{location}</div>
    </header>
  );
}
