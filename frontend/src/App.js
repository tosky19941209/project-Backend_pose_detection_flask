import logo from './logo.svg';
import './App.css';
import Track from './Front/Track'
import "./style/bootstrap/css/bootstrap.min.css"
// import "./pages/bootstrap/js/bootstrap.min.js"
function App() {
  return (
    <div className="App">
      <header className="App-header" style={{
        backgroundImage:'url("./asset.jpg")',
        backgroundSize : "cover"
      }}>
        <Track></Track>
      </header>
    </div>
  );
}

export default App;
