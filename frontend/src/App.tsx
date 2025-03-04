import { useState } from "react";
import Home from "./component/Home";
import "./App.css";
import Login from "./component/Login";


function App() {
  const [isAuthenticated, setAuthenticated] = useState(false);
  const [token, setToken] = useState("");
  return (
    <div className="p-3 mb-2 min-vh-100  bg-dark-subtle text-dark-emphasis">
      {isAuthenticated ? (
        <Home setToken={setToken} token={token} />
      ) : (
        <Login setAuthenticated={setAuthenticated} setToken={setToken} />
      )}
    </div>
  );
}

export default App;
